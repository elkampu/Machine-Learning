class Tile:
    
    def __init__(self, tileNum, endX, endY , X, Y):
        self.X = X
        self.Y = Y
        self.endX = endX
        self.endY = endY
        self.tileNumber = tileNum
        self.avMove = "none"
        self.movesToEnd = 0
        
    def move(self):
        
        if self.avMove == "up":
            self.Y -= 1
            return
            
        if self.avMove == "down":
            self.Y += 1
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
        return int((abs(self.endX - self.X) + abs(self.endY - self.Y)))
    
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
            self.avMove="up"
            return self.avMove
            
        if (((self.Y - tile.getY()) == -1) & (self.X == tile.getX())):
            self.avMove="down"
            return self.avMove
        
        self.avMove = "none"
        return "none"

    def setPosition (self, pos):
        if (pos == 1):
            self.X = 0
            self.Y = 0
            
        if (pos == 2):
            self.X = 1
            self.Y = 0

        if (pos == 3):
            self.X = 2
            self.Y = 0

        if (pos == 4):
            self.X = 0
            self.Y = 1

        if (pos == 5):
            self.X = 1
            self.Y = 1

        if (pos == 6):
            self.X = 2
            self.Y = 1

        if (pos == 7):
            self.X = 0
            self.Y = 2

        if (pos == 8):
            self.X = 1
            self.Y = 2

        if (pos == 9):
            self.X = 2
            self.Y = 2

        return
        
    def getTempMovesToEnd(self):
        if (self.avMove == "right"):
            return ((abs(self.endX - (self.X + 1)) + abs(self.endY - self.Y)))
        
        if (self.avMove == "left"):
            return ((abs(self.endX - (self.X - 1)) + abs(self.endY - self.Y)))
        
        if (self.avMove == "up"):
            return ((abs(self.endX - self.X) + abs(self.endY - (self.Y - 1))))
        
        if (self.avMove == "down"):
            return ((abs(self.endX - self.X) + abs(self.endY - (self.Y + 1))))

    def getPosition(self):
        if ((self.X == 0) & (self.Y == 0)):
            return 1
        if ((self.X == 1) & (self.Y == 0)):
            return 2
        if ((self.X == 2) & (self.Y == 0)):
            return 3
        if ((self.X == 0) & (self.Y == 1)):
            return 4
        if ((self.X == 1) & (self.Y == 1)):
            return 5
        if ((self.X == 2) & (self.Y == 1)):
            return 6
        if ((self.X == 0) & (self.Y == 2)):
            return 7
        if ((self.X == 1) & (self.Y == 2)):
            return 8
        if ((self.X == 2) & (self.Y == 2)):
            return 9

        return