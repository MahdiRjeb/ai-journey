# Python: strings and files

## Strings
- `s.strip()`: removes spaces and line breaks at both ends
- `s.lower()` / `s.upper()`: change the case
- `s.replace("old", "new")`: replace text
- `s.split(",")`: cut a string into a list at each comma
- `"-".join(my_list)`: glue a list into one string
- `word[0]` first character, `word[-1]` last, `word[1:4]` characters 1 to 3 (the end is excluded)
- `f"{name} is {age}"`: put variables inside text
- `"th" in "python"`: True or False

Strings can't be changed in place. Every method returns a new string, so I keep it: `s = s.strip()`.

## Reading a file
```python
with open("scores.csv") as f:
    next(f)                      # skip the header
    for line in f:
        name, points = line.strip().split(",")
```
- `with open(...) as f` opens the file and closes it automatically
- `for line in f` gives one line at a time, each ending with a line break
- Lines are text, so I use `float()` or `int()` before adding numbers

## Writing a file
```python
with open("out.txt", "w") as f:
    f.write("first line\n")
```
- `"w"` creates the file or **overwrites** it
- `\n` is the line break

## Pattern: total per category
```python
totals = {}
with open("scores.csv") as f:
    next(f)
    for line in f:
        name, points = line.strip().split(",")
        totals[name] = totals.get(name, 0) + float(points)
```
It is the dictionary counting pattern with a file in front of it.

## Mistakes to avoid
- `FileNotFoundError`: I ran Python from the wrong folder. I `cd` into the folder with the file first.
- Forgetting `strip()`: the line break stays inside the text.
- Forgetting `float()`: `+` glues text instead of adding numbers.
- Forgetting `next(f)`: the header line crashes `float()`.

## Still to practice
Writing all of this from a blank file, without looking.