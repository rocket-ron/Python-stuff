class GraphNode(object):

	def __init__(self, value = None):
		self.value = value
		self.connections = []

	def add_connections(self, other):
		if other not in self.connections:
			self.connections.append(other)
		if self not in other.connections:
			other.connections.append(self)

	def get_connections(self):
		return self.connections