
from Tile import Tile

class TilesBoard:
    
    tile1 = Tile(1, 0, 0, 2, 0)
    tile2 = Tile(2, 1, 0, 1, 0)
    tile3 = Tile(3, 2, 0, 0, 2)
    tile4 = Tile(4, 2, 1, 2, 1)
    tile5 = Tile(5, 2, 2, 2, 2)
    tile6 = Tile(6, 1, 2, 0, 1)
    tile7 = Tile(7, 0, 2, 1, 1)
    tile8 = Tile(8, 0, 1, 1, 2)
    
    emptyTile = Tile(0, 1, 1, 0, 0)
    
    tiles = [emptyTile, tile1, tile2, tile3, tile4, tile5, tile6, tile7, tile8]

    movements = 0
    pastStates = []
    
    def moveTiles(self):
        
        avMoves = []
        movableTiles = []
        i = 0

        tmpState = []
        
        totalMovesToEnd = 0
        
        for ti in self.tiles:
            if (ti.getNumber() == 0):
                continue
            totalMovesToEnd += ti.getMovesToEnd()
            if (ti.canMove(self.emptyTile) != "none"):
                movableTiles.append(ti)
            
        for ti in movableTiles:
            avMoves.append(totalMovesToEnd - ti.getMovesToEnd() + ti.getTempMovesToEnd())
        
        for k in range((len(movableTiles))-1):
            if (movableTiles[k+1].getMovesToEnd() < movableTiles[k].getMovesToEnd()):
                i = k+1


             
        if (movableTiles[i].getAvMove() == "up"):
            self.emptyTile.setAvMove("down")
        else:
            self.emptyTile.setAvMove("up")
                
        if (movableTiles[i].getAvMove() == "right"):
            self.emptyTile.setAvMove("left")
        else:
            self.emptyTile.setAvMove("right")
        
        self.emptyTile.move()
        self.tiles[movableTiles[i].getNumber()].move()


        for tile in self.tiles:
            tmpState.append(tile.getPosition)

        #if (tmpState == self.pastStates[movements]):
        #    movableTiles.pop(i)

        self.movements += 1
        self.pastStates.append(tmpState)

        return
        
    def printBoard(self):
        x = 0
        y = 0
        for tile in (self.tiles):
            x = tile.getX()
            y = tile.getY()
            if ((x == 0) & (y == 0)):
                print("\n|" + str(tile.getNumber()), end = " ")
                break
        for tile in (self.tiles):
            x = tile.getX()
            y = tile.getY()        
            if ((x == 1) & (y == 0)):
                print("|" + str(tile.getNumber()), end = " ")
        for tile in (self.tiles):
            x = tile.getX()
            y = tile.getY()        
            if ((x == 2) & (y == 0)):
                print("|" + str(tile.getNumber()), end = " ")
        for tile in (self.tiles):
            x = tile.getX()
            y = tile.getY()        
            if ((x == 0) & (y == 1)):
                print("|\n|" + str(tile.getNumber()), end = " ")
        for tile in (self.tiles):
            x = tile.getX()
            y = tile.getY()       
            if ((x == 1) & (y == 1)):
                print("|" + str(tile.getNumber()), end = " ")
        for tile in (self.tiles):
            x = tile.getX()
            y = tile.getY()        
            if ((x == 2) & (y == 1)):
                print("|" + str(tile.getNumber()), end = " ")
        for tile in (self.tiles):
            x = tile.getX()
            y = tile.getY()        
            if ((x == 0) & (y == 2)):
                print("|\n|" + str(tile.getNumber()), end = " ")
        for tile in (self.tiles):
            x = tile.getX()
            y = tile.getY()        
            if ((x == 1) & (y == 2)):
                print("|" + str(tile.getNumber()), end = " ")
        for tile in (self.tiles):
            x = tile.getX()
            y = tile.getY()        
            if ((x == 2) & (y == 2)):
                print("|" + str(tile.getNumber()) + "|", end = " ")

        return
                
    def movesToSolve(self):
        moves = 0
        for ti in self.tiles:
            moves += ti.getMovesToEnd()
            
        return moves
    
tileBrd = TilesBoard
tileBrd.printBoard(tileBrd)
tileBrd.moveTiles(tileBrd)
tileBrd.printBoard(tileBrd)

tileBrd.moveTiles(tileBrd)
tileBrd.printBoard(tileBrd)

tileBrd.moveTiles(tileBrd)
tileBrd.printBoard(tileBrd)