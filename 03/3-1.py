import numpy
file = open('3.txt')
gamma = ''
epsilon = ''
matrix = []
for line in file:
  matrix.append(list(line.rstrip()))
transposed_matrix = numpy.transpose(matrix)
for position in transposed_matrix:
  zeros = 0
  ones = 0
  for value in position:
    if value == '0':
      zeros += 1
    elif value =='1':
      ones += 1
  if zeros > ones:
    gamma += '0'
    epsilon += '1'
  else:
    gamma += '1'
    epsilon += '0'
power = int(gamma, 2) * int(epsilon, 2)
print(power)