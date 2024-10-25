
def grade_categorizer():
    score = int(input("Enter score:"))
# validation
    if score < 0 or score > 100:
        return "Invalid score!"
    else:
#categorize
        if score >= 90:
            grade = "A"
        elif score >= 80:
            grade = "B"
        elif score >= 70:
            grade = "C"
        elif score >= 60:
            grade = "D"
        else:
            grade = "F"
        return grade
print(grade_categorizer())