f = open('1.txt')
original = None
larger = 0
for line in f:
  if original == None:
    original = int(line)
    continue
  elif int(line) > original:
    larger = larger + 1
  original = int(line)
print(larger)