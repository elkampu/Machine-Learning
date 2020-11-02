from Tile import tile

class Node:
    
    def __init__(self, st, nFS):

        self.state = st
        self.nodesFromStart = nFS
        self.childNodes = []
        self.movesToWin = 0
    def getChildNodes(self, moves):

        i = self.state.index(0)

        if i in [0, 1, 2, 3, 4, 5]:
            nextState = self.state [:]
            nextState[i], nextState[i+3] = nextState[i+3], nextState[i]
            yield Node(nextState, moves + 1)

        if i in [3, 4, 5, 6, 7, 8]:
            nextState = self.state [:]
            nextState[i], nextState[i-3] = nextState[i-3], nextState[i]
            yield Node(nextState, moves + 1)

        if i in [0, 1, 3, 4, 6, 7]:
            nextState = self.state [:]
            nextState[i], nextState[i+1] = nextState[i+1], nextState[i]
            yield Node(nextState, moves + 1)

        if i in [1, 2, 4, 5, 7, 8]:
            nextState = self.state [:]
            nextState[i], nextState[i-1] = nextState[i-1], nextState[i]
            yield Node(nextState, moves + 1)
        