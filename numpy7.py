import numpy as np

# Student names
students = np.array(["Aman", "Riya", "Karan", "Neha", "Vikas"])

# Marks in 3 subjects
marks = np.array([
    [78, 85, 90],
    [92, 88, 79],
    [65, 70, 72],
    [89, 91, 95],
    [55, 60, 58]
])

# Total marks
total = np.sum(marks, axis=1)

# Average marks
average = np.mean(marks, axis=1)

# Highest scorer
topper_index = np.argmax(total)

print("===== SMART EXAM ANALYZER =====\n")

for i in range(len(students)):
    print(f"Student: {students[i]}")
    print(f"Marks: {marks[i]}")
    print(f"Total: {total[i]}")
    print(f"Average: {average[i]:.2f}")

    if average[i] >= 75:
        print("Performance: Excellent ⭐")
    elif average[i] >= 60:
        print("Performance: Good 👍")
    else:
        print("Performance: Needs Improvement 📚")

    print("-" * 35)

print("\n🏆 TOPPER DETAILS")
print(f"Topper: {students[topper_index]}")
print(f"Total Marks: {total[topper_index]}")