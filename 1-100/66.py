# Create a tuple of student names and their scores, then find the student with the highest score.
# Create a tuple of student names and their scores
student_scores = (("Alice", 95), ("Bob", 89), ("Charlie", 78), ("David", 92), ("Eve", 88))

# Find the student with the highest score
highest_score_student = max(student_scores, key=lambda student: student[1])

# Print the student with the highest score
print("Student with the Highest Score:")
print("Name:", highest_score_student[0])
print("Score:", highest_score_student[1])
