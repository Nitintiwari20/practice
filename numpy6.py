import numpy as np

# Creating marks array
marks = np.array([
    [78, 85, 90],
    [67, 72, 80],
    [88, 91, 95],
    [45, 60, 55]
])

print("Student Marks:\n")
print(marks)

# Total marks of each student
total_marks = np.sum(marks, axis=1)

print("\nTotal Marks:")
print(total_marks)

# Average marks of each student
average_marks = np.mean(marks, axis=1)

print("\nAverage Marks:")
print(average_marks)

# Highest marks in each subject
highest_marks = np.max(marks, axis=0)

print("\nHighest Marks in each Subject:")
print(highest_marks)

# Lowest marks in each subject
lowest_marks = np.min(marks, axis=0)

print("\nLowest Marks in each Subject:")
print(lowest_marks)

# Students who scored more than 80 average
top_students = average_marks > 80

print("\nTop Students (Average > 80):")
print(top_students)

# Bonus marks added
updated_marks = marks + 5

print("\nMarks after Bonus:")
print(updated_marks)