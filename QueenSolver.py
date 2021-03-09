import argparse

from Board import Board
from Queen import Queen

#Working out how the attacks function works
#myBoard = Board(3)

#myQueen = Queen()

#myQueen.placeOn(myBoard, 1, 1)

#myQueen2 = Queen()
#myQueen2.placeOn(myBoard, 3, 2)

#s = myQueen.attacks(myQueen2)
#print(s)


# https://en.wikipedia.org/wiki/Eight_queens_puzzle
def numberOfSolutions(i, board):
    if (i < board.size()):
        queen = Queen()
        count = 0

        for j in range(board.size()):
            queen.placeOn(board, i, j)
            if (board.adminissiblePlacementFor(queen)):
                count = count + numberOfSolutions(i + 1, board)
            queen.removeFromBoard()

        return count
    else:
        return 1

parser = argparse.ArgumentParser(description="Solve the Queen\'s puzzle of the specified size")
parser.add_argument('size', metavar='N', type=int,
                    help='an integer for the size of the board and number of queens')
args = parser.parse_args()

size = args.size
board = Board(size)

print(numberOfSolutions(0, board))