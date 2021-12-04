file = open('3.txt')
numbers = []
for line in file:
  numbers.append(line.rstrip())
oxygen = numbers
co2 = numbers
position = 0
for column in range(len(numbers[0])):
  if len(oxygen) > 1:
    zeros = 0
    ones = 0
    new_oxygen = []
    for n in oxygen:
      if n[position] == '0':
        zeros += 1
      elif n[position] =='1':
        ones += 1
    if zeros > ones:
      for n in oxygen:
        if n[position] =='0':
          new_oxygen.append(n)
    else:
      for n in oxygen:
        if n[position] =='1':
          new_oxygen.append(n)
    oxygen = new_oxygen
  position += 1
position = 0
for column in range(len(numbers[0])):
  if len(co2) > 1:
    zeros = 0
    ones = 0
    new_co2 = []
    for n in co2:
      if n[position] == '0':
        zeros += 1
      elif n[position] =='1':
        ones += 1
    if zeros > ones:
      for n in co2:
        if n[position] =='1':
          new_co2.append(n)
    else:
      for n in co2:
        if n[position] =='0':
          new_co2.append(n)
    co2 = new_co2
  position += 1
life = int(oxygen[0], 2) * int(co2[0], 2)
print(life)