#### Data Visualization With Seaborn
# Seaborn is a Python visualization library based on Matplotlib that provides a high-level interface for drawing attractive and informative statistical graphics. Seaborn helps in creating complex visualizations with just a few lines of code. In this lesson, we will cover the basics of Seaborn, including creating various types of plots and customizing them. 

# to install seaborn
# pip install seaborn

import seaborn as sns
import matplotlib.pyplot as plt

# Basic Plotting 

# load dataset are kind of dummy datasets already present in seaborn to test the functionality
tips = sns.load_dataset("tips")
print(tips)

# creating scatter plot 
sns.scatterplot(x="total_bill", y="tip", data=tips)
plt.show()

# creating line plot 
sns.lineplot(x="size", y="total_bill", data=tips)
plt.show()

# catogorial plots
sns.barplot(x="day", y="total_bill", data=tips)
plt.title("Total Bill by Day")
plt.show()

# box plot
sns.boxplot(x="day", y="total_bill", data=tips)
plt.show()

# violen plot
sns.violinplot(x="day", y="total_bill", data=tips)
plt.show()

# swarm plot
sns.swarmplot(x="day", y="total_bill", data=tips)
plt.show()

# histogram
sns.histplot(tips["total_bill"], bins=10 , kde=True)
plt.show()

# kde plot
sns.kdeplot(tips["total_bill"],fill=True)
plt.show()

# Pair Plot
sns.pairplot(tips)
plt.show()

# Heat Map
corr = tips[["total_bill", "tip", "size"]].corr()
sns.heatmap(corr, annot=True , cmap="coolwarm")
plt.show()