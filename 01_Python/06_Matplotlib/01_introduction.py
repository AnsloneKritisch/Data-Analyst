# Matplotlib is a plotting library for the Python programming language and its numerical mathematics extension NumPy. It provides an object-oriented API for embedding plots into applications using general-purpose GUI toolkits like Tkinter, wxPython, Qt, or GTK.

# Matplotlib is widely used in the scientific community for creating static, animated, and interactive visualizations in python. It is particularly useful for creating two-dimensional plots, histograms, power spectra, bar charts, errorcharts, scatterplots, etc. with a very high degree of customization.


# to use matplotlib in python, we need to install the matplotlib package.
# pip install matplotlib

import matplotlib.pyplot as plt

x = [1, 2, 3 , 4 , 5 ]
y = [2, 4, 6 , 8 , 10]

# plt.plot(x, y)
# plt.show()

# if i want to change name of my plot 

plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.title('Line Plot')
plt.plot(x, y , color = 'red' , linestyle = '-.' , marker = 'o' , markerfacecolor = 'green' , markersize = 12)
plt.grid(True)
plt.show()
