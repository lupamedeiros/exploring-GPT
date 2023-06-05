# Flight Search Tests

import unittest
from flight_search import search_flights


class TestFlightSearch(unittest.TestCase):
    
    def test_search_flights(self):
        # Test search_flights function with valid inputs
        departure_location = 'New York'
        arrival_location = 'Los Angeles'
        travel_dates = '2023-06-01'
        preferred_airlines = 'Delta, United'
        layover_time = '2h'
        departure_time = '12:00'
        budget = '500'
        results = search_flights(departure_location, arrival_location, travel_dates, preferred_airlines, layover_time, departure_time, budget)
        self.assertTrue(len(results) > 0)
        
        # Test search_flights function with invalid inputs
        departure_location = 'New York'
        arrival_location = 'Los Angeles'
        travel_dates = '2023-06-01'
        preferred_airlines = 'Delta, United'
        layover_time = '2h'
        departure_time = '12:00'
        budget = '100'
        results = search_flights(departure_location, arrival_location, travel_dates, preferred_airlines, layover_time, departure_time, budget)
        self.assertTrue(len(results) == 0)
        
        # Test search_flights function with edge case inputs
        departure_location = 'New York'
        arrival_location = 'Los Angeles'
        travel_dates = '2023-06-01'
        preferred_airlines = 'Delta, United'
        layover_time = '30m'
        departure_time = '06:00'
        budget = '1000'
        results = search_flights(departure_location, arrival_location, travel_dates, preferred_airlines, layover_time, departure_time, budget)
        self.assertTrue(len(results) > 0)
        
if __name__ == '__main__':
    unittest.main()
