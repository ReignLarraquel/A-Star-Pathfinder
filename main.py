statesExplored = 1
# Returns the indices for the Start state and the Goal state
def getStart(maze):
    for i in range(len(maze)):
        for j in range(len(maze)):
            if maze[i][j] == 'S':
                return (i, j)

def getEnd(maze):
    for i in range(len(maze)):
        for j in range(len(maze)):
            if maze[i][j] == 'G':
                return (i, j)

# Function that checks if the current location is inside the maze and is not a wall
def isEmptySpace(maze, length, node):
    if node[0] == -1 or node[1] == -1:
        return False
    if node[0] > length - 1 or node[1] > length - 1:
        return False
    if maze[node[0]][node[1]] == '#':
        return False

    return True

def heuristic(node, goal):
   return abs(node[0] - goal[0]) + abs(node[1]-goal[1])

def getNeighbors(maze, length, node):
    coords = [(node[0]-1, node[1]),
              (node[0]+1, node[1]),
              (node[0], node[1]-1),
              (node[0], node[1]+1)]
    neighbors = []
    for coord in coords:
        if isEmptySpace(maze, length, coord):
            neighbors.append(coord)

    return neighbors

def draw(currNode, maze, length):
    pass

def aStar(maze, length, start, goal):
    global statesExplored
    frontier = set([start])
    explored = set([])

    #set fcosts
    fCosts = {}
    fCosts[start] = 0 #fcost of start is 0

    #set gcosts
    gCosts = {}
    gCosts[start] = 0 #gcost of start is 0

    #gcosts of start's neighbors is always 1
    for neighbor in getNeighbors(maze, length, start):
        gCosts[neighbor] = 1

    #set parent
    parents = {}
    parents[start] = start #parent of start is itself

    #keep on exploring while the frontier is not empty
    while len(frontier) > 0:
        currNode = None

        for node in frontier:
            if currNode == None or (fCosts[node] < fCosts[currNode]):
                currNode = node

        statesExplored += 1

        draw(currNode, maze, length)

        if currNode == goal:
            optimalPath = []
            print("End found!")

            node = goal
            while node != parents[node]:
                optimalPath.append(node)
                node = parents[node]
            optimalPath.append(start)
            optimalPath.reverse()

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

        frontier.remove(currNode)
        explored.add(currNode)

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

    path = aStar(maze, length, start, goal)

    if path is None:
        print("No path found!")
    else:
        print(path)


    print("states explored:", statesExplored)

if __name__ == '__main__':
    main()