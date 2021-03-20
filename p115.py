inputdata = input()

row = int(inputdata[1])
column = int(ord(inputdata[0]) - ord('a')) + 1

steps = [(-2,-1),(-2,1),(2,-1),(2,1),(-1,-2),(-1,2),(1,-2),(1,2)]

count = 0

for step in steps:
  nrow = row + step[1]
  ncolumn = column + step[0]
  if nrow >= 1 and nrow <= 8 and ncolumn >= 1 and ncolumn <= 8:
    count += 1

print(count)
