file = open('2.txt')
instructions = []
for line in file:
  instructions.append(str(line.rstrip('\n')))
horizontal = 0
depth = 0
aim = 0
value = 0
move = ''
for i in instructions:
  value = int(i[-1])
  move = str(i[:-2])
  if move == 'forward':
    horizontal += value
    depth += (aim * value)
  elif move == 'down':
    aim += value
  elif move == 'up':
    aim -= value
final = horizontal * depth
print(final)