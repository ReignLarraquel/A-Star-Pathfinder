# Open maze.txt Files
maze = open("maze.txt", "r")

length = maze.readline() # Get the length of the maze

for i in range(int(length)): # Rows of the maze
   for j in range(int(length)): # Columns of the maze

      # Read one character at a time
      symbol = maze.read(1) 

      # Check if the character is a dot, wall, start, or goal
      # The print statements is just to remove the error
      if(symbol == '.'):
         print(".")
         # Code for empty space

      elif(symbol == '#'):
         print("#")
         # Code for wall

      elif(symbol == 'S'):
         print("S")
         # Code for start

      elif(symbol == 'G'):
         print("G")
         # Code for goal

# Close the file
maze.close()