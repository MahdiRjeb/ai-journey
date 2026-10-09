phone_book = {"aaaa": 2222222, "oledfjg": 23333444, "FFF": 55555}
print(phone_book["aaaa"])
print(phone_book.get("ssss", "unknown"))
print(phone_book.items())

text = "mississippi"
count = {}
for letter in text:
    count[letter] = count.get(letter, 0) + 1
print(count)                  # {'m': 1, 'i': 4, 's': 4, 'p': 2}

my_list = [3, 1, 3, 2, 1, 5]
unique = set(my_list)
print(len(unique))            # 4
print(sorted(unique))         # [1, 2, 3, 5]

grades = {"Sara": 15, "Ali": 12, "Nour": 18}
total = 0
for note in grades.values():
    total = total + note
print(total / len(grades))    # 15.0

best_name = None
best_grade = 0
for name, note in grades.items():
    if note > best_grade:
        best_grade = note
        best_name = name
print(best_name, best_grade)  # Nour 18