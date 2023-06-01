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
            self.grid.append([0 for y in range(self.size)])
        print("Grid Built\n")
        
    def createTile(self) -> Tile:
        """Returns a 4 tile 10% of the time and a 2 tile the other 90%"""
        if not random.randint(0, 9):
            return Tile(4)
        else:
            return Tile(2)
        # TODO Fix this
    
    def addRandomTile(self):
        """Adds tile to random empty spot on the board"""
        tile = self.createTile()
        print(tile)
        empty = [] # TODO fix this ugly ass code
        for i, row in enumerate(self.grid):
            for j, tile in enumerate(row):
                if tile == 0:
                    empty.append([i, j])
        pos = random.choice(empty)
        x = pos[0]
        y = pos[1]
        self.grid[x][y] = tile # Why does it just ignore this line
        print(self.grid[x][y])
        # DONE Create a tile
        # DONE Find a random !empty! position for the it
        # TODO Put it at that position
    
    def start(self):
        """Add two tiles to random spots at the start of the game"""
        self.addRandomTile()
        self.addRandomTile()
        
    def show(self):
        out = ""
        for row in self.grid:
            out += str(row) + "\n"
        return out
        
# Ok so what does this board need to do (backend)
"""
1. Manage a list of the current tiles and their values DONE
2. Update each time a move is made
2a. Move tiles to the correct new position
2b. Combine like tiles
2b. Collide unlike tiles
3. Add a tile to a random spot
3a. Add two tiles to random spots at the beginning of the game
4. Make sure the move is valid? (non-valid moves just wouldn't do anything so maybe not)
"""

test = Board(4)
print(test.show())