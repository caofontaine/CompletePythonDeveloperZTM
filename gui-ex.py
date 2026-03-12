#Exercise!
#Display the image below to the right hand side where the 0 is going to be ' ', and the 1 is going to be '*'. This will reveal an image!
picture = [
  [0,0,0,1,0,0,0],
  [0,0,1,1,1,0,0],
  [0,1,1,1,1,1,0],
  [1,1,1,1,1,1,1],
  [0,0,0,1,0,0,0],
  [0,0,0,1,0,0,0]
]

new_picture = []

for i in range(len(picture)):
    row = []
    for j in range(len(picture[i])):
        if picture[i][j] == 1:
            row.append('*')
        else:
            row.append(' ')
    new_picture.append(row)
        
print(new_picture)

#Solution
for image in picture:
  for pixel in image:
    if (pixel):
      print('*', end ="")
    else:
      print(' ', end ="")
  print('')