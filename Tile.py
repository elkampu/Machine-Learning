class Tile:
    
    endX = 0
    endY = 0
    X = 0
    Y = 0
    
    tileNumber = 0
    
    avMove = "none"
    movesToEnd = 0
    
    
    def __init__(self, tileNum, endX, endY , X, Y):
        self.X = X
        self.Y = Y
        self.endX = endX
        self.endY = endY
        self.tileNumber = tileNum
        
    def move(self):
        
        if self.avMove == "up":
            self.Y += 1
            return
            
        if self.avMove == "down":
            self.Y -= 1
            return
            
        if self.avMove == "right":
            self.X += 1
            return
            
        if self.avMove == "left":
            self.X -= 1
            return
            
        return
        
    def getX(self):
        return self.X
    
    def getY(self):
        return self.Y
    
    def getMovesToEnd(self):
        return (abs(self.endX - self.X) + abs(self.endY - self.Y))
    
    def setAvMove(self, move):
        self.avMove = move
        return
    
    def getAvMove(self):
        return self.avMove
    
    def getNumber(self):
        return self.tileNumber
    
    def canMove(self, tile):
        if (((self.X - tile.getX()) == 1) & (self.Y == tile.getY())):
            self.avMove="left"
            return self.avMove
        
        if (((self.X - tile.getX()) == -1) & (self.Y == tile.getY())):
            self.avMove="right"
            return self.avMove
            
        if (((self.Y - tile.getY()) == 1) & (self.X == tile.getX())):
            self.avMove="down"
            return self.avMove
            
        if (((self.Y - tile.getY()) == -1) & (self.X == tile.getX())):
            self.avMove="up"
            return self.avMove
        
        self.avMove = "none"
        return "none"
        
    def getTempMovesToEnd(self):
        if (self.avMove == "right"):
            return ((abs(self.endX - self.X + 1)) + abs(self.endY - self.Y))
        
        if (self.avMove == "left"):
            return ((abs(self.endX - self.X - 1)) + abs(self.endY - self.Y))
        
        if (self.avMove == "up"):
            return ((abs(self.endX - self.X)) + abs(self.endY - self.Y - 1))
        
        if (self.avMove == "down"):
            return ((abs(self.endX - self.X + 1)) + abs(self.endY - self.Y + 1))

    def getPosition(self):
        if ((x == 0) & (y == 0)):
            return 1
        if ((x == 0) & (y == 0)):
            return 2
        if ((x == 0) & (y == 0)):
            return 3
        if ((x == 0) & (y == 0)):
            return 4
        if ((x == 0) & (y == 0)):
            return 5
        if ((x == 0) & (y == 0)):
            return 6
        if ((x == 0) & (y == 0)):
            return 7
        if ((x == 0) & (y == 0)):
            return 8
        if ((x == 0) & (y == 0)):
            return 9

        return