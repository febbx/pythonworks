# 3. Given a dictionary where the keys are student names and the values are their scores, write a program to calculate the average score.

students_scores={"malu":40,"aswathy":50,"kareena":75,"vignesh":40,"ananthu":95}

total_score=sum(students_scores.values())

no_of_students=len(students_scores)

avg_score=(total_score/no_of_students)

print("Average score:",avg_score)