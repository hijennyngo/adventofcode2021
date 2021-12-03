# UNFINISHED!!

file = open('3-sample.txt')
oxygen = ''
co2 = ''
counter = {0:0, 1:0}
position = 0
numbers = []
oxygen_list = []
co2_list = []

# count number of positions in the row
positions = len(file.readline().rstrip())

# append lines into numbers list
for line in file:
  numbers.append(line.rstrip())

# counter increment for value depending on position 
for n in numbers:
  if n[position] == '0':
    counter[0] += 1
  elif n[position] == '1':
    counter[1] +=1
# increment position after finished counting
position =+ 1

# check which value is larger and append to new oxygen list
if int(counter[0]) > int(counter[1]):
  for n in numbers:
    if n[0] == '0':
      oxygen_list.append(n)
elif int(counter[1]) > int(counter[0]):
  for n in numbers:
    if n[0] == '1':
      oxygen_list.append(n)

print(oxygen_list)
#life = oxygen * co2