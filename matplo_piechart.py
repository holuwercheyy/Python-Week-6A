import matplotlib.pyplot as plt

# Student's daily activities
activities = ['Sleeping', 'Studying', 'Eating', 'Exercising', 'Leisure']
hours = [8, 6, 2, 2, 6]
plt.figure(figsize=(8, 5))
plt.pie(hours, labels=activities, autopct='%1.1f%%', startangle=90)
plt.title("How a Student Spends 24 Hours")
plt.show()
