import matplotlib.pyplot as plt  # Import the plotting library

# 1. Define the data for the pie chart
labels = ['A', 'B', 'C', 'D', 'E']                # Categories to display
sizes = [10, 20, 30, 40, 50]                      # Corresponding values for each category
colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral', 'red']  # Slice colors

# 2. Highlight one slice by "exploding" it slightly
explode = (0.1, 0, 0, 0, 0)  # Only 'A' slice is offset from center by 0.1

# 3. Create the pie chart
plt.pie(
    sizes,                   # Data values
    labels=labels,           # Category labels
    colors=colors,           # Colors for each slice
    explode=explode,         # Which slices to offset
    autopct='%1.1f%%',       # Show percent value with one decimal place
    shadow=True,             # Draw a shadow for a 3D effect
    startangle=90            # Rotate start of chart so first slice is at 12 o'clock
)

# 4. Display the chart
plt.show()
