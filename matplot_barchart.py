import matplotlib.pyplot as plt

students = [1, 2, 3, 4, 5, 6, 7, 8, 9, 9.5, 11, 12]
scores = [10, 20, 25, 30, 40, 43, 45, 48, 50, 54, 58, 60]

plt.bar(students, scores, color='skyblue')
plt.title("Student Scores")
plt.xlabel("Students")
plt.ylabel("Scores")
plt.show()
