import matplotlib.pyplot as plt

ages = [20, 21, 20, 23, 24, 22, 20, 21, 22, 25, 23, 23, 23, 21, 24, 24, 24, 24, 25, 25, 27]

plt.hist(ages, bins=5, color='purple')
plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.show()
 