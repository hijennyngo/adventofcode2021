file = open('2.txt')
instructions = []
for line in file:
  instructions.append(str(line.rstrip('\n')))
horizontal = 0
depth = 0
value = 0
move = ''
for i in instructions:
  value = int(i[-1])
  move = str(i[:-2])
  if move == 'forward':
  	horizontal += value
  elif move == 'down':
  	depth += value
  elif move == 'up':
  	depth -= value
final = horizontal * depth
print(final)