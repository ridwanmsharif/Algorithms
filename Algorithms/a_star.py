from __future__ import print_function
 
# In order to use the A* Path finding algoritm,
# We'll need a graoth to traverse through
# We define this graph as a class
class AStarGraph(object):
 	
 	# Defining boundaries for the graph
 	# Bounding search to a 8x8 co-ordinate plane
	def __init__(self):
		self.barriers = []
		self.barriers.append([(0,0),(1,0),(2,0),(3,0),(4,0),(5,0),(6,0),(7,0),
							  (0,1),(0,2),(0,3),(0,4),(0,5),(0,6),(0,7),(0,8),
							  (8,0),(8,1),(8,2),(8,3),(8,4),(8,5),(8,7),(8,7),
							  (1,8),(2,8),(3,8),(4,8),(5,8),(6,8),(7,8),(8,8)])

	# Add user defined barriers list
	def add_baririers(self, list_barriers):
		self.barriers.append(list_barriers)
 	
 	# Using Euclidean displacement as heuristics
	def heuristic(self, start, goal):
		dx = abs(start[0] - goal[0])
		dy = abs(start[1] - goal[1])
		return (dx + dy)

	# Find all neighbours of particular node input (co-ordinate)
	# Neighbours defined as surrounding coordinates in range
	def get_vertex_neighbours(self, pos):
		n = []

		for dx, dy in [(1,0),(-1,0),(0,1),(0,-1),(1,1),(-1,1),(1,-1),(-1,-1)]:
			x2 = pos[0] + dx
			y2 = pos[1] + dy

			if x2 < 0 or x2 > 8 or y2 < 0 or y2 > 8:
				continue

			n.append((x2, y2))

		return n

	# Calculating cost to each traversal/move
	# If move touches barrier, move is not allowed
	# To dissallow move, its cost is assigned to 1000
	# Thus ensuring it is indeed ignored during search 
	def move_cost(self, a, b):
		for barrier in self.barriers:
			if b in barrier:
				return 1000 
		return 1 

# Carries out the A* search taking start and end nodes and a graph
# Nodes are 2-element fixed lists (x, y) co-ordinates
# Grapgh is an instance of the AStarGraph class
def AStarSearch(start, end, graph):
    
    # Build Cost Dictionaries
	G = {} # Movement cost to each position from the start position
	F = {} # Movement cost of start to end going via this position 
 
	# Initialize starting values
	G[start] = 0 
	F[start] = graph.heuristic(start, end)
 
	closedVertices = list()
	openVertices = list([start])
	cameFrom = {}
 
	while len(openVertices) > 0:
		current = None
		currentFscore = None
		# Find Node with lowest F score
		for pos in openVertices:
			if current is None or F[pos] < currentFscore:
				currentFscore = F[pos]
				current = pos
 
		# Base Case if reached
		if current == end:
			path = [current]

			while current in cameFrom:
				current = cameFrom[current]
				path.append(current)
			path.reverse()

			return path, F[end]
 
		# Mark the current vertex as closed
		openVertices.remove(current)
		closedVertices.append(current)
 
		# Update scores for vertices near the current position
		for neighbour in graph.get_vertex_neighbours(current):
			if neighbour in closedVertices: 
				continue 

			candidateG = G[current] + graph.move_cost(current, neighbour)
 
			if neighbour not in openVertices:
				openVertices.append(neighbour) # New Node

			elif candidateG >= G[neighbour]:
				continue # Larger Cost
 
			# Lower Cost
			cameFrom[neighbour] = current
			G[neighbour] = candidateG

			H = graph.heuristic(neighbour, end)
			F[neighbour] = G[neighbour] + H
 	
 	# Base Case if search exhausted
	raise RuntimeError("Co-ordinate you're looking for is not bounded by Graph")
 
if __name__=="__main__":
	graph = AStarGraph()
	result, cost = AStarSearch((7,0), (1, 1), graph)
	print ("Optimum Path:", result)
	print ("Cost of Optimum Path:", cost)
	