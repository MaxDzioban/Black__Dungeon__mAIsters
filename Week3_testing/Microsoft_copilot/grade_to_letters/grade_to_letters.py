def calculate_grade(a, b, c, d, e):
    if a > 100 or a < 0 or b > 100 or b < 0 or c > 100 or c < 0 or d > 100 or d < 0 or e > 100 or e < 0:
        return None

    grade=round(((a+b+c+d+e)/5), 1)

    if 100>=grade>=90:
        return f"Average grade = {grade} -> A"
    elif 90>grade>=80:
        return f"Average grade = {grade} -> B"
    elif 80>grade>=70:
        return f"Average grade = {grade} -> C"
    elif 70>grade>=60:
        return f"Average grade = {grade} -> D"
    else:
        return f"Average grade = {grade} -> F"
