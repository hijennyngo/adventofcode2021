file = open('6.txt')
content = file.read()
lanternfish = map(int, content.split(","))
lf_dict = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0}
for fish in lanternfish:
  if fish == 0:
    lf_dict[0] += 1
  elif fish == 1:
    lf_dict[1] += 1
  elif fish == 2:
    lf_dict[2] += 1
  elif fish == 3:
    lf_dict[3] += 1
  elif fish == 4:
    lf_dict[4] += 1
  elif fish == 5:
    lf_dict[5] += 1
  elif fish == 6:
    lf_dict[6] += 1
  elif fish == 7:
    lf_dict[7] += 1
  elif fish == 8:
    lf_dict[8] += 1
for i in range(256):
  lf_dict[7] += lf_dict[0]
  lf_dict[9] += lf_dict[0]
  lf_dict[0] = lf_dict[1]
  lf_dict[1] = lf_dict[2]
  lf_dict[2] = lf_dict[3]
  lf_dict[3] = lf_dict[4]
  lf_dict[4] = lf_dict[5]
  lf_dict[5] = lf_dict[6]
  lf_dict[6] = lf_dict[7]
  lf_dict[7] = lf_dict[8]
  lf_dict[8] = lf_dict[9]
  lf_dict[9] = 0
print(sum(lf_dict.values()))