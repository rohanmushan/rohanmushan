#Create a dictionary of student names and their scores, then find the average score
stud_scores={'Akash': 85,'Mahendra': 92,'Rohan': 78,'Atipra': 95,'Ram': 88}
avg_score=sum(stud_scores.values()) / len(stud_scores)
print("Student Scores: ")
for name, score in stud_scores.items():
    print(f"{name}: {score}")
print("\nAverage Score:", avg_score)
