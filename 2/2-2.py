file = open('2.txt')
instructions = []
for line in file:
  instructions.append(str(line.rstrip('\n')))
horizontal = 0
depth = 0
aim = 0
for i in instructions:
  move = str(i[:-2])
  value = int(i[-1])
  if move == 'forward':
    horizontal += value
    depth += (aim * value)
  elif move == 'down':
    aim += value
  elif move == 'up':
    aim -= value
final = horizontal * depth
print(final)