class Piece:                                                    #Piece does not inherit from board, hence we don't need to import the board class here.
    def __init__(self):                                         #Constructs the piece class with the given properties
        self.board = None
        self.i = None
        self.j = None

    def isOnBoard(self):                                        #Returns true if self.board does not equal none, i.e the piece is on the board
        return self.board != None

    def placeOn(self, board, i, j):                             #Defines a method which sets the position properties of the piece, and then places it on the board
                                                                #using the board.add method from the board class.
        if (not self.isOnBoard()
            and (0 <= i)
            and (i < board.size())
            and (0 <= j)
            and (j < board.size()) ):
                self.board = board;
                self.i = i;
                self.j = j;
                board.add( self );

    def removeFromBoard(self):                                  #Defines a method which checks if the piece is on the board and removes it from both the board.pieces set
                                                                #and changes the self.board property back to none, so that the isOnBoard method will work
        if (self.isOnBoard()):
            self.board.remove(self)
            self.board = None

    def attacks(self, piece):                                  #This is an abstract method, the attacks method belongs to all classes of pieces, but not the pieces class itself
                                                               #as the attack is different for each class which inherits from pieces class.
        raise Exception("An abstract method has been invoked")

    def isMindfulOf(self, piece):
        return ((piece!=None)
                and self.isOnBoard()
                and piece.isOnBoard()
                and self.board == piece.board
                and self != piece)
    
    def rowIndex(self):                                         #If we remove the piece from the board, we do not reset the i and j coordinates inside the removeFromBoard function
                                                                #so if we checked the coordinates we may come to the wrong conclusion. This makes sure it is returned as something
                                                                #which will flag up an error.
        if (self.isOnBoard()):
            return self.i
        else:
            return self.UNKNOWN
    
    def colIndex(self):                                         #This method does follows the same principal as rowIndex()
        if (self.isOnBoard()):
            return self.j;
        else:
            return self.UNKNOWN

    UNKNOWN = -1