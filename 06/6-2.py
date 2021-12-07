# LOL this takes too long

file = open('6.txt')
content = file.read()
lanternfish = map(int, content.split(","))
for i in range(256):
  for index, fish in enumerate(lanternfish):
    if fish == 0:
      lanternfish[index] = 6
      lanternfish.append(9)
    else:
      lanternfish[index] -= 1
print(len(lanternfish))