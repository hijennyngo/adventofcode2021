file = open('3.txt')
numbers = []
for line in file:
  numbers.append(line.rstrip())
oxygen = numbers
co2 = numbers
for column in range(len(numbers[0])):
  if len(oxygen) > 1:
    zeros = []
    ones = []
    for n in oxygen:
      if n[column] == '0':
        zeros.append(n)
      elif n[column] =='1':
        ones.append(n)
    if len(zeros) > len(ones):
      oxygen = zeros
    else:
      oxygen = ones
for column in range(len(numbers[0])):
  if len(co2) > 1:
    zeros = []
    ones = []
    for n in co2:
      if n[column] == '0':
        zeros.append(n)
      elif n[column] =='1':
        ones.append(n)
    if len(zeros) > len(ones):
      co2 = ones
    else:
      co2 = zeros
life = int(oxygen[0], 2) * int(co2[0], 2)
print(life)