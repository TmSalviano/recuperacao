
def compute_grade(grade: float):
    try:
        if grade > 1.0:
            return "Bad Score"
        elif grade >= 0.9:
            return "A"
        elif grade >= 0.8:
            return "B"
        elif grade >= 0.7:
            return "C"
        elif grade >= 0.6:
            return "D"
        elif grade < 0.6:
            return "F"
    except:
        return "Bad Score"

grade = compute_grade(float(input("Points: ")))
print("Grande " + grade)