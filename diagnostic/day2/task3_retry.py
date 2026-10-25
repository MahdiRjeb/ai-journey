with open("expenses.csv") as f:
  next(f)
  total = {}
  for line in f:
    category,amount=line.strip().split(",")
    total[category]=total.get(category,0)+float(amount)

for category, amount in total.items():
    print(category, amount)
