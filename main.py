maze = open("maze.txt", "r")
length = int(maze.readline())
field = maze.read().split("\n")
maze.close()
for i in range(length):
   print(field[i])
for j in range(length):
   for k in range(length):
      if(field[j][k] == 'S'):
         startnodey = j
         startnodex = k
      if(field[j][k] == 'G'):
         endnodey = j
         endnodex = k

def isBorder(x, y):
   if(x >= 0 and x < length and y >= 0 and y < length):
      return True
   return False

def gsearcher():
   bot = []
   currentx = startnodex
   currenty = startnodey
   while(bot[currentx][currenty] != field[endnodex][endnodey]):
      if(isBorder(currentx+1, currenty)):
         currentx += 1
         bot[currentx][currenty]
         print('right')
      if(isBorder(currentx, currenty+1)):
         currenty += 1
         print('down')
      if(isBorder(currentx-1, currenty)):
         currentx -= 1
         print('left')
      if(isBorder(currentx, currenty)):
         currenty -= 1
         print('up')
