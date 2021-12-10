file = open('8.txt')
values = []
for line in file:
  values.append(line.split("|")[1][1:].rstrip("\n"))
ones = 0
fours = 0
sevens = 0
eights = 0
for value in values:
  digits = value.split(" ")
  for digit in digits:
  	if len(digit) == 2:
  	  ones += 1
  	elif len(digit) == 4:
  	  fours += 1
  	elif len(digit) == 3:
  	  sevens += 1
  	elif len(digit) == 7:
  	  eights += 1
print(ones + fours + sevens + eights)