a=int(input())
b=int(input())
c=int(input())
d=int(input())
e=int(input())
if a < 0 or a > 100 or b < 0 or b > 100 or c < 0 or c > 100 or d < 0 or d > 100 or e < 0 or e > 100:
    print(None)
    exit()

grade=round(((a+b+c+d+e)/5), 1)

if 100>=grade>=90:
    print(f"Average grade = {grade} -> A")
elif 90>grade>=80:
    print(f"Average grade = {grade} -> B")
elif 80>grade>=70:
    print(f"Average grade = {grade} -> C")
elif 70>grade>=60:
    print(f"Average grade = {grade} -> D")
else:
    print(f"Average grade = {grade} -> F")