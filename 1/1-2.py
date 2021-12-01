file = open('1.txt')
numbers = []
index = 0
larger = 0
for line in file:
  numbers.append(int(line))
for n in numbers:
  if index < 3:
    index += 1
    continue
  elif n > numbers[index-3]:
    larger += 1
  index += 1
print(larger)