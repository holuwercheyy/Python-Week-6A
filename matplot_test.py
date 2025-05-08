import matplotlib.pyplot as plt

# Sample data
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 9.5, 11]
y = [10, 20, 25, 30, 40, 43, 45, 48, 50, 54, 58]

# Create a line plot
plt.plot(x, y)
plt.title("Simple Line Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid(True)
plt.savefig("line_plot.png")
plt.show()