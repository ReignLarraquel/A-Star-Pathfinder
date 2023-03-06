def isEmpty(field, x, y):
   if(x >= 0 and x < length and y >= 0 and y < length and field[x][y] != '#'):
      return True
   return False

def addEmptySpace(currentx, currenty):
   if(isEmpty(field, currentx+1, currenty)): #right
      pass
   if(isEmpty(field, currentx, currenty+1)): #down
      pass
   if(isEmpty(field, currentx-1, currenty)): #left
      pass
   if(isEmpty(field, currentx, currenty-1)): #up
      pass

maze = open("maze.txt", "r")
length = int(maze.readline())
field = maze.read().split("\n")
maze.close()
adjlist = {

}
for i in range(length):
   print(field[i])

for j in range(length):
   for k in range(length):
      if(field[j][k] == 'S'):
         startnodey = j
         startnodex = k
      elif(field[j][k] == 'G'):
         endnodey = j
         endnodex = k
         
      if(isEmpty(field, j, k)):
         
         addEmptySpace(j, k)