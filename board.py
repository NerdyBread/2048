import random

from tile import Tile

class Board:
    def __init__(self, size):
        self.size = size
        self.grid = []
        self._buildGrid()
        self.empty = (size**2) - 2 # Because two spaces are filled by self.start()
        self.start()
        
    def _buildGrid(self):
        """Creates grid of x size when the board is initialized"""
        for x in range(self.size):
            self.grid[x] = list()
            for y in range(self.size):
                self.grid[x][y] = None
        
    def createTile(self):
        """Returns a 4 tile 10% of the time and a 2 tile the other 90%"""
        return Tile(4) if not random.randint(0, 9) else Tile(2)
    
    def addTile(self):
        """Adds tile to random empty spot on the board"""
        empty = [] # TODO fix this ugly ass code
        for row in self.grid:
            for column in self.grid:
                if not self.grid[row][column]:
                    empty.append(self.grid[row][column])
        tile = self.createTile()
        # DONE Create a tile
        # TODO Find a random !empty! position for the it
        # Put it at that position
    
    def start(self):
        """Add two tiles to random spots at the start of the game"""
        pass
        

        
# Ok so what does this board need to do (backend)
"""
1. Manage a list of the current tiles and their values
2. Update each time a move is made
2a. Move tiles to the correct new position
2b. Combine like tiles
2b. Collide unlike tiles
3. Add a tile to a random spot
3a. Add two tiles to random spots at the beginning of the game
4. Make sure the move is valid? (non-valid moves just wouldn't do anything so maybe not)
"""