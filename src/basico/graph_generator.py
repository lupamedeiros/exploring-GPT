# Import necessary libraries
import matplotlib.pyplot as plt
import random

# Generate random numbers
random_numbers = [random.randint(1, 100) for _ in range(30)]

# Create plot using matplotlib
plt.plot(random_numbers)

# Customize plot
plt.title('Random Numbers Plot')
plt.xlabel('Index')
plt.ylabel('Value')
plt.grid(True)

# Save plot as PNG or PDF
plt.savefig('random_numbers_plot.png')

# Write all code to a file
with open('graph_generator.py', 'r') as f:
    code = f.read()
with open('graph_generator.py', 'w') as f:
    f.write(code)
