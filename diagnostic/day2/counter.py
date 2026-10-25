with open("lines.txt") as f:
  count_lines=0
  count_words=0
  for line in f:
    count_lines=count_lines + 1
    count_words = count_words + len(line.split())

print("lines : ",count_lines)
print("words : ",count_words)




