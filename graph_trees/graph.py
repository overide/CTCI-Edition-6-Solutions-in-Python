from collections import defaultdict

class Graph:

	def __init__(self):
		self.adjlist = defaultdict(list)

	def insert(self, s, d):
		self.adjlist[s].append(d)

	def del_edge(self, s, d):
		for i,v in enumerate(self.adjlist[s]):
			if v == d:
				self.adjlist[s].pop(i)	