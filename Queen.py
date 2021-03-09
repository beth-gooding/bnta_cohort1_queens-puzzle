from Piece import Piece                     #The Queen class inherits from the Piece class, so we need to import that class here

class Queen(Piece):                         #This notation is like class Queen extends Piece in JS
    def __init__(self):                     #Constructor function for the Queen class, 
        Piece.__init__(self)                #which then calls the Piece class constructor to inherit the Piece properties

    def attacks(self, piece):               #The method which defines if a queen object can attack another piece. Returns True
                                            #if the pieces are on the same board and the attack of the queen can be used on the 
                                            #other piece; returns false otherwise
        i = self.rowIndex()
        j = self.colIndex()

        u = piece.rowIndex()
        v = piece.colIndex()

        return (
            self.isMindfulOf(piece)
            and ((i == u)
                or (j == v) 
                or (i-j == u-v)
                or (i+j == u+v)) )