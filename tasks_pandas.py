import pandas as pd

data = {
    "Name": ['Alice', 'Bob', 'Charlie', 'Luqman', 'Samson', 'George'],
    "Age": [24, 30, 22, 28, 23, 27],
    "Score": [85, 90, 95, 88, 48, 75]
}
df = pd.DataFrame(data)
df['Passed'] = df['Score'] > 50
passed_students = df[df['Passed']]


average_score = passed_students['Score'].mean()
print(f"\nAverage score of students who passed: {average_score:.2f}")

print("All students:")
print(df)
print("\nStudents who passed:")
print(passed_students)
