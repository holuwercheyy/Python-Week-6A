import matplotlib.pyplot as plt

activities = ['Sleeping', 'Eating', 'Coding', 'Gaming', 'Singing']
hours = [7, 2, 8, 4, 3]

plt.pie(hours, labels=activities, autopct='%1.1f%%')
plt.title("Daily Activities")
plt.show()