class Board:
    def __init__(self, size):                #Constructor in Python basically, defining the properties of a class
        self.n = size
        self.pieces = set()

    def size(self):
        return self.n                        #A method which returns the size of a given board

    def admissiblePlacementFor(self, piece): #A method which checks whether the placement of piece violates the conditions of the problem
        for other in self.pieces:            #For the pieces in the board.pieces set
            if ((other != piece)             #If the other piece is not our specific piece...
                and other.attacks(piece)     #...and the other piece can attack or piece...
                or piece.attacks(other)):    #...or our specific piece could attack the other piece
                    return False             # the placement of the piece is not admissible
        return True                          #if we haven't returned False, then the placement is admissible

    def add(self, piece): 
        self.pieces.add(piece)              #A method which adds a piece to the board, the piece is stored in the board.pieces set

    def remove(self, piece):
        self.pieces.remove(piece)           #A method which removes a piece from the board, the piece is removed from the board.pieces set