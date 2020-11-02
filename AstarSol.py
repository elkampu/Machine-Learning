from TilesBoard import TilesBoard
from Tile import Tile
from Node import Node

class AstarSol:

    def __init__ (self):

        self.initialState = [0, 2, 1, 6, 7, 4, 3, 8, 5]
        self.goalState = [1, 2, 3, 8, 0, 4, 7, 6, 5]

    def solve(self):

        moves = 0
        openList = []
        closedList = []

        openList.append(Node(self.initialState[:], 0))

        while (1):

            for node in openList:
                if (node.getState == self.goalState):
                    return

                for nextNode in node.getChildNodes():
                    if nextNode not in closedList:
                        openList.append(nextNode)

                

                closedList.append(node)
            

