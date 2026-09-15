import os
import random
from time import sleep

ScreenResX, ScreenResY = 10, 20
pieceTypes = ['O', 'I', 'S', 'Z', 'L', 'J', 'T']

RED = '\033[41m'
BLUE = '\033[44m'
YELLOW = '\033[43m'
GREEN = '\033[42m'
ORANGE = '\033[45;5;208m'
PINK = '\033[48;5;213m'
PURPLE = '\033[45m'
WHITE = '\033[0m'

class Square:
    def __init__(self, locx, locy, color):
        self.colorText = color + '  ' + WHITE
        self.locx = locx
        self.locy = locy
    def __eq__(self, s):
        return s.locx == self.locx and s.locy == self.locy
    def fall(self):
        self.locy -= 1
    def restore(self):
        self.locy += 1

class Piece:
    def __init__(self):
        self.type = random.choice(pieceTypes)
        self.isMoving = True
        self.squares = []
        self.locx = (ScreenResX - 1) // 2
        self.locy = ScreenResY - 1
    def add_to_board(self):
        if self.type == 'O':
            self.squares.append(Square(self.locx, self.locy, YELLOW))
            self.squares.append(Square(self.locx + 1, self.locy, YELLOW))
            self.squares.append(Square(self.locx, self.locy + 1, YELLOW))
            self.squares.append(Square(self.locx + 1, self.locy + 1, YELLOW))
        elif self.type == 'I':
            self.squares.append(Square(self.locx, self.locy, BLUE))
            self.squares.append(Square(self.locx, self.locy + 1, BLUE))
            self.squares.append(Square(self.locx, self.locy + 2, BLUE))
            self.squares.append(Square(self.locx, self.locy + 3, BLUE))
        elif self.type == 'S':
            self.squares.append(Square(self.locx, self.locy, RED))
            self.squares.append(Square(self.locx + 1, self.locy, RED))
            self.squares.append(Square(self.locx + 1, self.locy + 1, RED))
            self.squares.append(Square(self.locx + 2, self.locy + 1, RED))
        elif self.type == 'Z':
            self.squares.append(Square(self.locx, self.locy, GREEN))
            self.squares.append(Square(self.locx + 1, self.locy, GREEN))
            self.squares.append(Square(self.locx, self.locy + 1, GREEN))
            self.squares.append(Square(self.locx - 1, self.locy + 1, GREEN))
        elif self.type == 'L':
            self.squares.append(Square(self.locx, self.locy, ORANGE))
            self.squares.append(Square(self.locx + 1, self.locy, ORANGE))
            self.squares.append(Square(self.locx, self.locy + 1, ORANGE))
            self.squares.append(Square(self.locx, self.locy + 2, ORANGE))
        elif self.type == 'J':
            self.squares.append(Square(self.locx, self.locy, PINK))
            self.squares.append(Square(self.locx + 1, self.locy, PINK))
            self.squares.append(Square(self.locx + 1, self.locy + 1, PINK))
            self.squares.append(Square(self.locx + 1, self.locy + 2, PINK))
        elif self.type == 'T':
            self.squares.append(Square(self.locx, self.locy, PURPLE))
            self.squares.append(Square(self.locx, self.locy + 1, PURPLE))
            self.squares.append(Square(self.locx + 1, self.locy + 1, PURPLE))
            self.squares.append(Square(self.locx - 1, self.locy + 1, PURPLE))
    def fall(self):
        for square in self.squares:
            square.fall()
    def restore(self):
        for square in self.squares:
            square.restore()

class Board:
    def __init__(self):
        
def draw_board(pieces, board): 
    clear_screen()
    for piece in pieces:
        piece.add_to_board(board)
    printStr = ''
    for j in range(ScreenResY):
        for i in range(ScreenResX):
            printStr += board[(ScreenResX * ScreenResY - 1) - board_index(i, j)]
        printStr += '\n'
    print(printStr)
    
def board_index(x, y):
    return ScreenResX * y + x

def clear_screen():
    """ Only works for Mac """
    _ = os.system('clear')
        
if __name__ == "__main__":
    isRunning = True
    pieces = []
    selectedPiece = None
    while isRunning:
        if selectedPiece is None:
            selectedPiece = Piece()
            pieces.append(selectedPiece)
        else:
            selectedPiece.fall()
            if (selectedPiece.locy == -1):
                if selectedPiece.locy == ScreenResY - 1:
                    isRunning = False
                selectedPiece = None
        board = { idx : '..' for idx in range(ScreenResX * ScreenResY)}
        draw_board(pieces, board)
        sleep(0.2)