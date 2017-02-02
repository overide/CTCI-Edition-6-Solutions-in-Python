# Route Between Nodes: Given a directed graph, design an algorithm to 
# find out whether there is a route between two nodes.

from queue import Queue
from graph import Graph

def route_exist(graph, s, d):
	'''
	Time Complexity : O(n*m)
	Space Complexity : O(1)
	'''
	visited = {}
	Q = Queue()
	Q.put(s)
	while not Q.empty():
		s = Q.get()
		visited[s] = True
		for v in graph.adjlist[s]:
			if not visited.get(v,False):
				Q.put(v)
				if v == d:
					return True

	return False

def main():
	g = Graph()
	g.insert(0,1)
	g.insert(1,2)
	g.insert(2,0)
	g.insert(2,3)
	g.insert(3,2)
	g.insert(3,4)
	print("Root Exist between 0 to 2 : ",route_exist(g,0,2))
	print("Root Exist between 4 to 0 : ",route_exist(g,4,0))

if __name__ == "__main__":
	main()
