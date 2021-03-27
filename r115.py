input_data=input()
row = int(input_data[1])
column = int(ord(input_data[0]))-int(ord('a')) + 1
movrow = [1, -1, 1, -1, -2, -2, 2, 2]
movcol = [2, 2, -2, -2, -1, 1, -1, 1]

count = 0

for i in range(8):
  changerow = row + movrow[i]
  changecol = column + movcol[i]
  if changerow > 0 and changerow <= 8 and changecol > 0 and changecol <= 8:
    count += 1

print(count) 
