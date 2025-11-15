import os
import random
from time import sleep

ScreenResX, ScreenResY = 10, 20
pieceTypes = ['O', 'I', 'S', 'Z', 'L', 'J', 'T']

red = '\033[41m'
blue = '\033[44m'
yellow = '\033[43m'
green = '\033[42m'
orange = '\033[45;5;208m'
pink = '\033[48;5;213m'
purple = '\033[45m'
white = '\033[0m'

class Piece:
    def __init__(self):
        self.type = random.choice(pieceTypes)
        self.isMoving = True
        self.locx = (ScreenResX - 1) // 2
        self.locy = ScreenResY - 1
    def add_to_board(self, board):
        if self.type == 'O':
            board[board_index(self.locx, self.locy)] = yellow + '  ' + white
            board[board_index(self.locx + 1, self.locy)] = yellow + '  ' + white
            board[board_index(self.locx, self.locy + 1)] = yellow + '  ' + white
            board[board_index(self.locx + 1, self.locy + 1)] = yellow + '  ' + white
        elif self.type == 'I':
            board[board_index(self.locx, self.locy)] = blue + '  ' + white
            board[board_index(self.locx, self.locy + 1)] = blue + '  ' + white
            board[board_index(self.locx, self.locy + 2)] = blue + '  ' + white
            board[board_index(self.locx, self.locy + 3)] = blue + '  ' + white
        elif self.type == 'S':
            board[board_index(self.locx, self.locy)] = red + '  ' + white
            board[board_index(self.locx + 1, self.locy)] = red + '  ' + white
            board[board_index(self.locx + 1, self.locy + 1)] = red + '  ' + white
            board[board_index(self.locx + 2, self.locy + 1)] = red + '  ' + white
        elif self.type == 'Z':
            board[board_index(self.locx, self.locy)] = green + '  ' + white
            board[board_index(self.locx + 1, self.locy)] = green + '  ' + white
            board[board_index(self.locx, self.locy + 1)] = green + '  ' + white
            board[board_index(self.locx - 1, self.locy + 1)] = green + '  ' + white
        elif self.type == 'L':
            board[board_index(self.locx, self.locy)] = orange + '  ' + white
            board[board_index(self.locx + 1, self.locy)] = orange + '  ' + white
            board[board_index(self.locx, self.locy + 1)] = orange + '  ' + white
            board[board_index(self.locx, self.locy + 2)] = orange + '  ' + white
        elif self.type == 'J':
            board[board_index(self.locx, self.locy)] = pink + '  ' + white
            board[board_index(self.locx + 1, self.locy)] = pink + '  ' + white
            board[board_index(self.locx + 1, self.locy + 1)] = pink + '  ' + white
            board[board_index(self.locx + 1, self.locy + 2)] = pink + '  ' + white
        elif self.type == 'T':
            board[board_index(self.locx, self.locy)] = purple + '  ' + white
            board[board_index(self.locx, self.locy + 1)] = purple + '  ' + white
            board[board_index(self.locx + 1, self.locy + 1)] = purple + '  ' + white
            board[board_index(self.locx - 1, self.locy + 1)] = purple + '  ' + white
            
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
        board = { idx : '..' for idx in range(ScreenResX * ScreenResY)}
        if selectedPiece is None:
            selectedPiece = Piece()
            pieces.append(selectedPiece)
        else:
            selectedPiece.locy -= 1
        draw_board(pieces, board)
        sleep(1)