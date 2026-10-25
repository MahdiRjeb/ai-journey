with open("grades.csv") as f:
  next(f)
  total =0
  best_grade=0
  best_name=""
  number_of_students=0
  for line in f:
    name,grade = line.strip().split(",")
    grade = float(grade)
    total=total+grade
    number_of_students=number_of_students+1
    if grade>best_grade:
      best_grade=grade
      best_name=name

print("Average:", total / number_of_students)
print("Best:", best_name, f"({best_grade})")
    