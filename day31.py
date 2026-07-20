# Module 6: Advanced Matplotlib & Subplots 
import matplotlib.pyplot as plt

#Task 2: Multiple Graphs 
# 1. Plot two lines
x = [1, 2, 3, 4, 5]
line1 = [10, 20, 30, 40, 50]
line2 = [5, 15, 25, 35, 45]

plt.plot(x, line1)
plt.plot(x, line2)

# 2. Add labels
plt.xlabel("X Values")
plt.ylabel("Y Values")

# 3. Add legend
plt.legend()
plt.title("Two Lines Comparison")
plt.show()

#Task 3: Figure Customization
# 1. Change figure size
plt.figure(figsize=(8, 5))
x = [1, 2, 3, 4, 5]
y = [10, 20, 15, 30, 25]
plt.plot(x, y)

# 2. Add title
plt.title("Customized Line Graph")

# 3. Add grid
plt.grid(True)
plt.show()

#Task 4: Subplot Practice 
# 1. Create 2 subplots
plt.subplot(1, 2, 1)
x = [1, 2, 3, 4, 5]
y1 = [10, 20, 30, 40, 50]
plt.plot(x, y1)
plt.title("Graph 1")

plt.subplot(1, 2, 2)
y2 = [5, 15, 25, 35, 45]
plt.plot(x, y2)
plt.title("Graph 2")
plt.show()

# 2. Create 4 subplots
plt.subplot(2, 2, 1)
plt.plot(x, y1)
plt.title("Graph 1")


plt.subplot(2, 2, 2)
plt.plot(x, y2)
plt.title("Graph 2")


plt.subplot(2, 2, 3)
plt.bar(x, y1)
plt.title("Graph 3")


plt.subplot(2, 2, 4)
plt.scatter(x, y2)
plt.title("Graph 4")
plt.show()

# 3. Compare graphs
plt.subplot(1, 2, 1)
plt.plot(x, y1)
plt.title("Line 1")

plt.subplot(1, 2, 2)
plt.plot(x, y2)
plt.title("Line 2")
plt.show()

#Task 5: Histogram Practice 
import random
# 1. Create histogram
data = [10, 20, 20, 30, 30, 30, 40, 40, 50, 60]
plt.hist(data)
plt.title("Simple Histogram")
plt.xlabel("Values")
plt.ylabel("Frequency")
plt.show()

# 2. Analyze distribution
data = [10, 12, 15, 18, 20, 22, 25, 25, 28, 30, 32, 35, 40, 45, 50]
plt.hist(data, bins=5)
plt.title("Data Distribution")
plt.xlabel("Values")
plt.ylabel("Frequency")
plt.show()

# 3. Use random dataset
random_data = [random.randint(1, 100) for i in range(50)]
plt.hist(random_data, bins=10)
plt.title("Random Data Distribution")
plt.xlabel("Values")
plt.ylabel("Frequency")
plt.show()

#Task 6: Save Graphs
# 1. Save line graph
x = [1, 2, 3, 4, 5]
y = [10, 20, 30, 40, 50]
plt.plot(x, y)
plt.title("Line Graph")
plt.savefig("line_graph.png")
plt.show()

# 2. Save histogram
data = [10, 12, 15, 18, 20, 22, 25, 25, 28, 30, 32, 35, 40, 45, 50]
plt.hist(data, bins=5)
plt.title("Histogram")
plt.savefig("histogram.png")
plt.show()


# 3. Save subplot figure
plt.subplot(1, 2, 1)
plt.plot(x, y)
plt.title("Line Graph")
plt.subplot(1, 2, 2)
plt.hist(data, bins=5)
plt.title("Histogram")
plt.savefig("subplot_figure.png")
plt.show()