import matplotlib.pyplot as plt

# Temperature changes during the day
times = ['Morning', 'Noon', 'Evening', 'Night']
temperatures = [20, 30, 25, 18]  # Temperatures in degrees Celsius
plt.figure(figsize=(8, 5))
plt.plot(times, temperatures, marker='o', color='red')
plt.title("Temperature Changes During the Day")
plt.xlabel("Time of Day")
plt.ylabel("Temperature (°C)")
plt.grid(True)
plt.show()