def get_average_score(scores):
    total = sum(scores)
    subj_count = len(scores)
    avg_score = total / subj_count
    
    return avg_score


def compute_grades(avg_score):
    if avg_score >= 80:
        grade = "Grade A"
    elif avg_score >= 60:
        grade = "Grade B"
    elif avg_score >= 50:
        grade = "Grade C"
    else:
        grade = "Grade F"
    
    return grade

student_scores = [55, 64, 75, 80, 65]

average_score = get_average_score(student_scores)

grade = compute_grades(average_score)

print(f"Average Score: {average_score}")
print(f"Grade: {grade}")