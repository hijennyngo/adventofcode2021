file = open('6.txt')
content = file.read()
lanternfish = map(int, content.split(","))
lf_dict = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0}
for fish in lanternfish:
  lf_dict[fish] += 1
for i in range(256):
  lf_dict[7] += lf_dict[0]
  lf_dict[9] += lf_dict[0]
  for n in range(9):
    lf_dict[n] = lf_dict[n+1]
  lf_dict[9] = 0
print(sum(lf_dict.values()))