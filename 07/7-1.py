file = open('7.txt')
content = file.read()
crabs = sorted(map(int, content.split(",")))
values = len(crabs)
mid_index = (values - 1) // 2
if (values % 2):
  median = crabs[mid_index]
else:
  median = (crabs[mid_index] + crabs[mid_index + 1]) / 2
fuel = 0
for crab in crabs:
  fuel += abs(crab - median)
print(fuel)