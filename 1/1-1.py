file = open('1.txt')
original = None
larger = 0
for line in file:
  if original == None:
    original = int(line)
    continue
  elif int(line) > original:
    larger += 1
  original = int(line)
print(larger)