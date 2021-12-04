file = open('3.txt')
numbers = []
for line in file:
  numbers.append(line.rstrip())
gamma = ''
epsilon = ''
position = 0
for column in range(len(numbers[0])):
  zeros = 0
  ones = 0
  for n in numbers:
    if n[position] == '0':
      zeros += 1
    elif n[position] =='1':
      ones += 1
  if zeros > ones:
    gamma += '0'
    epsilon += '1'
  else:
    gamma += '1'
    epsilon += '0'
  position += 1
power = int(gamma, 2) * int(epsilon, 2)
print(power)