import random

from tile import Tile

class Board:
	def __init__(self, size):
		self.size = size
		self.grid = []
		self.filled = []
		self._buildGrid()
		self.start()
		
	def _buildGrid(self):
		"""Creates grid of x size when the board is initialized"""
		for x in range(self.size):
			self.grid.append([Tile(None, x, y) for y in range(self.size)])
		
	def createTile(self) -> Tile:
		"""Returns a 4 tile 10% of the time and a 2 tile the other 90%"""
		if not random.randint(0, 9):
			return Tile(4)
		else:
			return Tile(2)
	
	def addRandomTile(self):
		"""Adds tile to random empty spot on the board"""
		newTile = self.createTile()
		empty = []
		for row in self.grid:
			for tile in row:
				if tile not in self.filled:
					empty.append(tile)
		newPos = random.choice(empty).position
		self.grid[newPos["x"]][newPos["y"]] = newTile
		self.filled.append(newTile)
		newTile.position = newPos
		# DONE Create a tile
		# DONE Find a random !empty! position for the it
		# DONE Put it at that position
	
	def start(self):
		"""Add two tiles to random spots at the start of the game"""
		self.addRandomTile()
		self.addRandomTile()
		
	def show(self):
		out = ""
		for row in self.grid:
			for tile in row:
				if not tile.val:
					out += "[ ]"
				else:
					out += f"[{str(tile)}]"
			out += "\n"
		return out
		
	def directionMap(self, direction):
		directions = {"r": {"x": 1, "y": 0},
                "l": {"x": -1, "y": 0},
                "u": {"x": 0, "y": -1},
                "d": {"x": 0, "y": 1}}
		return directions[direction]
	
		
# Ok so what does this board need to do (backend)
"""
1. Manage a list of the current tiles and their values DONE
2. Update each time a move is made
2a. Move tiles to the correct new position
2b. Combine like tiles
2b. Collide unlike tiles
3. Add a tile to a random spot DONE
3a. Add two tiles to random spots at the beginning of the game DONE
4. Make sure the move is valid? (non-valid moves just wouldn't do anything so maybe not)
"""

test = Board(4)
print(test.show())