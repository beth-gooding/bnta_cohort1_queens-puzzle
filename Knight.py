from Piece import Piece

class Knight(Piece):
    def __init__(self):
        Piece.__init__(self)

    def attacks(self, piece):

        i = self.rowIndex();
        j = self.colIndex();

        u = piece.rowIndex();
        v = piece.colIndex();

        return (
            self.isMindfulOf(piece)
            and (((u == i-2) and (v == j-1))
                or ((u == i-2) and (v == j+1))
                or ((u == i+2) and (v == j-1))
                or ((u == i+2) and (v == j+1))
                or ((u == i-1) and (v == j-2))
                or ((u == i-1) and (v == j-2))
                or ((u == i+1) and (v == j-2))
                or ((u == i+1) and (v == j+2))) )
