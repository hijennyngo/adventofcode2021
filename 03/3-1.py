file = open('3.txt')
numbers = []
for line in file:
  numbers.append(line.rstrip())
gamma = ''
epsilon = ''
for column in range(len(numbers[0])):
  zeros = 0
  ones = 0
  for n in numbers:
    if n[column] == '0':
      zeros += 1
    elif n[column] =='1':
      ones += 1
  if zeros > ones:
    gamma += '0'
    epsilon += '1'
  else:
    gamma += '1'
    epsilon += '0'
power = int(gamma, 2) * int(epsilon, 2)
print(power)