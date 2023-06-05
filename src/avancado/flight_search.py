# Flight Search

# Gather information on user's preferences and restrictions
departure_location = input("What is your departure location?")
arrival_location = input("What is your arrival location?")
travel_dates = input("What are your travel dates?")
preferred_airlines = input("What are your preferred airlines?")
layover_time = input("What is your preferred layover time?")
departure_time = input("What is your preferred departure time?")
budget = input("What is your budget?")

# Search for best flight options

import requests
from bs4 import BeautifulSoup

url = f"https://www.google.com/flights?hl=en#flt={departure_location}.{arrival_location}.{travel_dates};c:{preferred_airlines};e:1;sd:1;t:f"

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Filter results based on user's preferences

results = []

for result in soup.find_all('div', class_='gws-flights-results__result-item'):
    price = result.find('div', class_='gws-flights-results__price').text
    airline = result.find('div', class_='gws-flights-results__carriers').text
    departure_time = result.find('div', class_='gws-flights-results__times').find_all('div')[0].text
    arrival_time = result.find('div', class_='gws-flights-results__times').find_all('div')[1].text
    layover = result.find('div', class_='gws-flights-results__duration').text
    if airline in preferred_airlines and layover <= layover_time and departure_time >= departure_time and price <= budget:
        results.append({'price': price, 'airline': airline, 'departure_time': departure_time, 'arrival_time': arrival_time, 'layover': layover})

# Present filtered results to user and assist in booking selected flight

for i, result in enumerate(results):
    print(f"{i+1}. {result['airline']} - {result['departure_time']} to {result['arrival_time']} - {result['price']}")

selected_flight = input("Which flight would you like to book?")

# Assist user in booking selected flight

flight_code = results[int(selected_flight)-1]['flight_code']
booking_url = f"https://www.google.com/flights?hl=en#flt={flight_code};c:{preferred_airlines};e:1;sd:1;t:f"

print(f"To book your flight, please visit {booking_url}")

# Continuously monitor flight prices and notify user if a cheaper option becomes available before the trip

original_price = results[int(selected_flight)-1]['price']

while True:
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    cheapest_price = soup.find('div', class_='gws-flights-results__price').text
    if cheapest_price < original_price:
        # Notify user via email or text message
        break
