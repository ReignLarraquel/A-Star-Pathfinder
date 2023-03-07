# MCO 1: MAZE BOT
#
# Authors:
#   - Arevalo, Jose Joaquin A.
#   - Austria, Rafael Antonio M.
#   - Larraquel, Reign Elaiza D.
#   - Mercado, Bruce B.

#---------------------------------#

import color

# Global Variable
# Value is incremented every time a state is explored
statesExplored = 0

# Returns the indices for the Start state
def getStart(maze):
    for i in range(len(maze)): # Rows
        for j in range(len(maze)): # Columns
            if maze[i][j] == 'S':
                # Returns two values: the row and column of the Start state
                return (i, j)

# Returns the indices for the Goal state
def getEnd(maze):
    for i in range(len(maze)): # Rows
        for j in range(len(maze)): # Columns
            if maze[i][j] == 'G':
                # Returns two values: the row and column of the Goal state
                return (i, j)

# Function that checks if the current location is inside the maze and is not a wall
def isEmptySpace(maze, length, node):
    # Checks if the node is out of bounds
    if node[0] == -1 or node[1] == -1:
        return False
    if node[0] > length - 1 or node[1] > length - 1:
        return False
    
	# Checks if the node is a wall
    if maze[node[0]][node[1]] == '#':
        return False

	# If the node is not a wall and is inside the maze, return True
    return True

# Function that returns the heuristic value of the current node
# Using Manhattan Distance
def heuristic(node, goal):
   # Formula: |x1 - x2| + |y1 - y2|
   return abs(node[0] - goal[0]) + abs(node[1]-goal[1])

# Function that returns the neighbors of the current node
# The neighbors are the empty spaces around the current node
def getNeighbors(maze, length, node):
	# List of coordinates of the neighbors
    coords = [(node[0]-1, node[1]), # Left
              (node[0]+1, node[1]), # Right
              (node[0], node[1]-1), # Up
              (node[0], node[1]+1)] # Down
    
	# List of neighbors, the empty spaces around the current node
    neighbors = []
    
	# For each coordinate, check if it is an empty space
    for coord in coords:
		# If it is an empty space, add it to the list of neighbors
        if isEmptySpace(maze, length, coord):
            neighbors.append(coord)

	# Return the list of neighbors
    return neighbors

# Function that displays the maze in its initial state
def displayMaze(maze, length):
    for i in range(length):
        for j in range(length):
            print(maze[i][j], end = " ")
        print()
    print()

# Function that displays the maze in its final state
def newMaze(maze, length, explored, optimalPath):
    for i in range(length):
        for j in range(length):
            if (i, j) == getStart(maze):
                print(color.GREEN + "S", end = " ") # Start
            elif (i, j) == getEnd(maze):
                print(color.GREEN + "G", end = " ") # Goal
            elif (i, j) in optimalPath:
                print(color.BLUE + "■", end = " ") # Optimal path
            elif (i, j) in explored:
                print(color.RED + "■", end = " ") # Explored states
            elif isEmptySpace(maze, length, (i, j)):
                print(color.LIGHT_GRAY + ".", end = " ") # Empty space
            else:
                print(color.DARK_GRAY + "#", end = " ") # Wall
        print()
    print()

# Function that implements the A* algorithm
def aStar(maze, length, start, goal):
    global statesExplored # Global variable
    
	# Set of frontier states
    frontier = set([start]) 
    
	# Set of explored states
    explored = set([]) 

	# To get the distance, we use the formula f = g + h
	# Where 'f' is the total cost, 
	# 'g' is the distance from the start to the current node, 
	# and 'h' is the distance from the current node to the goal (heuristic)

    # Sets the fcosts (total cost)
    fCosts = {}
    fCosts[start] = 0 # fcost of start is 0

    # Sets the gcosts (distance from the start to the current node)
    gCosts = {}
    gCosts[start] = 0 # gcost of start is 0


    # gcosts of start's neighbors is always 1
    for neighbor in getNeighbors(maze, length, start):
        gCosts[neighbor] = 1

	
    # Set parent
    parents = {}
    parents[start] = start #parent of start is itself

    # Keep on exploring while the frontier is not empty
    while len(frontier) > 0:
        ctr = 1
        currNode = None

        # Get the node with the lowest fcost
        for node in frontier:
            if currNode == None or (fCosts[node] < fCosts[currNode]):
                currNode = node

        # Increment the number of states explored
        statesExplored += 1

        # Check if the current node is the goal
        if currNode == goal:
            # The coordinates which shows the optimal path
            optimalPath = [] 

            # Set node to the goal
            node = goal

            # Stores the coordinates of the optimal path from the goal to the start to the list
            while node != parents[node]:
                optimalPath.append(node)
                node = parents[node]
            
            # Add the start state to the list
            optimalPath.append(start)
            # Reverse the list to get the path from the start to the goal
            optimalPath.reverse()

            # Display the maze in its final state
            newMaze(maze, length, explored, optimalPath)
            print("End found!")

            # Exit loop and return the optimal path
            return optimalPath

        #calculate currnode's neighbors
        for neighbor in getNeighbors(maze, length, currNode):
            if neighbor not in frontier and neighbor not in explored:
                frontier.add(neighbor)
                parents[neighbor] = currNode
                gCosts[neighbor] = gCosts[parents[neighbor]] + 1
                fCosts[neighbor] = gCosts[neighbor] + heuristic(neighbor, goal)

            elif neighbor in frontier:
                if gCosts[currNode] < gCosts[neighbor]:
                    fCosts[neighbor] = gCosts[currNode] + heuristic(neighbor, goal)
                    parents[neighbor] = currNode

        # Remove the current node from the frontier and add it to the explored set
        frontier.remove(currNode)
        explored.add(currNode)
    
    # If the frontier is empty, no path is found
    newMaze(maze, length, explored, optimalPath)
    return None

def main():
    # File Handline
    file = open("maze.txt", "r")
    length = int(file.readline())
    maze = file.read().split("\n")
    file.close()

    # Gets the value for the Start state and Goal state
    start = getStart(maze)
    goal = getEnd(maze)

    print("     MAZE BOT")
    print("===================")
    print("Algothrim: A*")
    print()

    print("Initial state:")
    displayMaze(maze, length)

    print()

    print("Using A* Algorithm:")
    path = aStar(maze, length, start, goal)

    if path is None:
        print("No path found!")

    print("States explored:", statesExplored)
    print("Optimal path:", len(path), "steps")

if __name__ == '__main__':
    main()