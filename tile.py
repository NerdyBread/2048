class Tile:
	def __init__(self, val, x=None, y=None):
		self.val = val
		self.moved = bool() # Check if tile has moved this turn
		self.position = {"x": x, "y": y}
		
	def __str__(self):
		return str(self.val)