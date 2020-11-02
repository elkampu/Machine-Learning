import copy
import random
from Tile import Tile

class TilesBoard:
    
    def __init__ (self):

        self.tile1 = Tile(1, 0, 0, 2, 0)
        self.tile2 = Tile(2, 1, 0, 1, 0)
        self.tile3 = Tile(3, 2, 0, 0, 2)
        self.tile4 = Tile(4, 2, 1, 2, 1)
        self.tile5 = Tile(5, 2, 2, 2, 2)
        self.tile6 = Tile(6, 1, 2, 0, 1)
        self.tile7 = Tile(7, 0, 2, 1, 1)
        self.tile8 = Tile(8, 0, 1, 1, 2)

        self.pastNodes = []
    
        self.emptyTile = Tile(0, 1, 1, 0, 0)
    
        self.tiles = [self.emptyTile, self.tile1, self.tile2, self.tile3, self.tile4, self.tile5, self.tile6, self.tile7, self.tile8]

        self.movements = 0
        self.pastStates = []

    
    def moveTiles(self):
        
        avMoves = []
        movableTiles = []
        i = 0
        k = 0
        x = 0

        tmpState = []
        tmpTiles = []
        possibleStates = []
        
        totalMovesToEnd = 0
        
        for ti in self.tiles: # Checking which tiles are able to me moved (is adyacent to empty space)
            if (ti.getNumber() == 0): # Not checking for the space
                continue
            totalMovesToEnd += ti.getMovesToEnd() # Using the loop to get the current moves left to win
            if (ti.canMove(self.tiles[0]) != "none"): # The tile class will remember if and where it can be moved
                movableTiles.append(ti) # Adding the movable tile to a list

        while x < len(movableTiles): # Checking if a move leads to a past state of the tile board
            for y in range(len(self.pastStates)):
                if ((self.getPossibleState(movableTiles[x].getNumber())) == self.pastStates[y]):
                    movableTiles.pop(x) # Discarding it
                    x -= 1
                    #if (len(movableTiles) == 0):
                    #    resetNum = random.randint (0, len(self.pastStates)-1)
                    #    resetState = self.pastStates[resetNum]
                    #    for i in range(len(self.pastStates)-resetNum):
                    #        self.pastStates.pop()
                    #    for l in range(len(resetState)):
                    #        self.tiles[l].setPosition(resetState[l])

                    #    for tile in self.tiles:
                    #        self.tiles[tile.getNumber()].setAvMove("none")

                    #    return
                    #break
            
            x += 1

        for ti in movableTiles: # A new list with the moves left to win for every possible move
            avMoves.append(totalMovesToEnd - ti.getMovesToEnd() + ti.getTempMovesToEnd())
        
        for k in range(len(avMoves)-1): # Checking which move is best taking the one with the least moves to win
            if (avMoves[k+1] < avMoves[k]):
                i = k+1

        if (movableTiles[i].getAvMove() == "up"):
            self.tiles[0].setAvMove("down")
        
        if (movableTiles[i].getAvMove() == "down"):
            self.tiles[0].setAvMove("up")
                
        if (movableTiles[i].getAvMove() == "right"):
            self.tiles[0].setAvMove("left")

        if (movableTiles[i].getAvMove() == "left"):
            self.tiles[0].setAvMove("right")
        
        self.tiles[0].move()
        self.tiles[movableTiles[i].getNumber()].move()


        for tile in self.tiles:
            tmpState.append(tile.getPosition())
            self.tiles[tile.getNumber()].setAvMove("none")

        self.movements += 1
        self.pastStates.append(tmpState)

        return
       
    def getPossibleState(self, tileNumber):
        state = []
        tmpTiles = copy.deepcopy(self.tiles)
        if (tmpTiles[tileNumber].getAvMove() == "up"):
            tmpTiles[0].setAvMove("down")
        
        if (tmpTiles[tileNumber].getAvMove() == "down"):
            tmpTiles[0].setAvMove("up")
                
        if (tmpTiles[tileNumber].getAvMove() == "right"):
            tmpTiles[0].setAvMove("left")
        
        if (tmpTiles[tileNumber].getAvMove() == "left"):
            tmpTiles[0].setAvMove("right")

        
        tmpTiles[tileNumber].move()
        tmpTiles[0].move()

        for ti in tmpTiles:
            state.append(ti.getPosition())

        tmpTiles.clear()
        return state

    def printBoard(self):
        x = 0
        y = 0
        for tile in (self.tiles):
            x = tile.getX()
            y = tile.getY()
            if ((x == 0) & (y == 0)):
                print("\n|" + str(tile.getNumber()), end = " ")
        for tile in (self.tiles):
            x = tile.getX()
            y = tile.getY()        
            if ((x == 1) & (y == 0)):
                print("|" + str(tile.getNumber()), end = " ")
        for tile in (self.tiles):
            x = tile.getX()
            y = tile.getY()        
            if ((x == 2) & (y == 0)):
                print("|" + str(tile.getNumber()) + "|\n", end = " ")
        for tile in (self.tiles):
            x = tile.getX()
            y = tile.getY()        
            if ((x == 0) & (y == 1)):
                print("|" + str(tile.getNumber()), end = " ")
        for tile in (self.tiles):
            x = tile.getX()
            y = tile.getY()       
            if ((x == 1) & (y == 1)):
                print("|" + str(tile.getNumber()), end = " ")
        for tile in (self.tiles):
            x = tile.getX()
            y = tile.getY()        
            if ((x == 2) & (y == 1)):
                print("|" + str(tile.getNumber()) + "|\n", end = " ")
        for tile in (self.tiles):
            x = tile.getX()
            y = tile.getY()        
            if ((x == 0) & (y == 2)):
                print("|" + str(tile.getNumber()), end = " ")
        for tile in (self.tiles):
            x = tile.getX()
            y = tile.getY()        
            if ((x == 1) & (y == 2)):
                print("|" + str(tile.getNumber()), end = " ")
        for tile in (self.tiles):
            x = tile.getX()
            y = tile.getY()        
            if ((x == 2) & (y == 2)):
                print("|" + str(tile.getNumber()) + "|\n", end = " ")

        return
                
    def movesToSolve(self):
        moves = 0
        for ti in self.tiles:
            if (ti.getNumber() == 0):
                continue

            moves += ti.getMovesToEnd()
            
        return moves

    def getMovements(self):
        return self.movements

tileBrd = TilesBoard()

while (tileBrd.movesToSolve() != 0):
    
    tileBrd.moveTiles()
    tileBrd.printBoard()

print (tileBrd.getMovements())

