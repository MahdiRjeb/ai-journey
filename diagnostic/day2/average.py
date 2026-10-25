with open("grades.csv") as f:
  next(f)
  total={}
  max=0
  for line in f:
    name,grade=line.strip().split(",")
    total[name]=total.get(grade,0)+float(grade)
    count=count+total[name]
    if total[name]>max:
      max=total[name]

  AVG=total/len(total)
  print(AVG)
  print(max)


  #c'est faux !!!!!