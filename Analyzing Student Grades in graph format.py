import matplotlib.pyplot as plt

# Define a list of student grades
student_grades = [85, 90, 55, 72, 60, 40, 78, 93, 65, 50]

# Calculate statistics
total_students = len(student_grades)
average_grade = sum(student_grades) / total_students
highest_grade = max(student_grades)
lowest_grade = min(student_grades)
num_passed = sum(grade >= 50 for grade in student_grades)
num_failed = total_students - num_passed
pass_percentage = (num_passed / total_students) * 100
fail_percentage = (num_failed / total_students) * 100

# Print statistics
print("Statistics:")
print("Total number of students:", total_students)
print("Average grade:", average_grade)
print("Highest grade:", highest_grade)
print("Lowest grade:", lowest_grade)
print("Number of students who passed:", num_passed)
print("Number of students who failed:", num_failed)
print("Percentage of students who passed: {:.2f}%".format(pass_percentage))
print("Percentage of students who failed: {:.2f}%".format(fail_percentage))

# Create bar graph
labels = ['Passed', 'Failed']
values = [num_passed, num_failed]

plt.bar(labels, values, color=['green', 'red'])
plt.title('Number of Students Who Passed vs Failed')
plt.xlabel('Category')
plt.ylabel('Number of Students')
plt.show()
