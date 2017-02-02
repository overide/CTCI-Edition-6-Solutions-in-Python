# Build Order: You are given a list of projects and a list of dependencies (which is a list of pairs of
# projects, where the second project is dependent on the first project). All of a project's dependencies
# must be built before the project is. Find a build order that will allow the projects to be built. If there
# is no valid build order, return an error.
# EXAMPLE
# Input:
# projects: a, b, c, d, e, f
# dependencies: (a, d), (f, b), (b, d), (f, a), (d, c)
# Output: f, e, a, b, d, c

from collections import defaultdict
from graph import Graph

def topological_sort(graph,nodes):
	'''
	Time complexity : O(V + E)
	'''
	visited = defaultdict()
	stack = []
	for n in nodes:
		if not visited.get(n,False):
			visit(n,visited,stack,graph)
	
	for _ in range(len(stack)):
		print(stack.pop(),end = " ")

def visit(n,visited,stack,graph):
	visited[n] = True
	for v in graph.adjlist.get(n,[]):
		if not visited.get(v,False):
			visit(v,visited,stack,graph)
	stack.append(n)

def main():

	projects = ['a','b','c','d','e','f']
	g = Graph()
	g.insert('a','d')
	g.insert('f','b')
	g.insert('b','d')
	g.insert('f','a')
	g.insert('d','c')
	topological_sort(g,projects)
	print("\n")

if __name__ == "__main__":
	main()

