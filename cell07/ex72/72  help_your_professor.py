def average(scores_dict):
    total_score = sum(scores_dict.values())
    num_students = len(scores_dict)
    
    if num_students > 0:
        return total_score / num_students
    else:
        return 0
students_scores = {
    "Kaka": 85,
    "Cristiano Ronaldo": 92,
    "Lionel Messi": 78,
    "Mitree Kumsu": 88,
    "์New": 95
}

class_average = average(students_scores)
print("Class Average:", class_average)