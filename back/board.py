from tools import *

class Board:
    def __init__(self):
        self.board = None

    def creat_board(self):
        board = [[" " for _ in range(8)] for _ in range(8)]

        tools = [Rook, Knight, Bishop, Queen, King, Bishop, Knight, Rook]  

        for i, piece_class in enumerate(tools):
            board[0][i] = piece_class("white") 
            board[1][i] = Pawn("white")          

        for i, piece_class in enumerate(tools[::-1]):
            board[7][i] = piece_class("black") 
            board[6][i] = Pawn("black")    

        self.board = board

    def __str__(self):
        res = " "
        res += " | "
        for num in range(1,9):
            res += f"{num} | "
        res += "\n"
        for num , char in zip(range(1,9) , [chr(i) for i in range(ord('a'), ord('h') + 1)]):
            res += f"{num} | "
            for pice in self.board[num-1]:
                res += f"{pice} | "
            res += f"{char}\n" 
        res += "  | "
        for char in [chr(i) for i in range(ord('a'), ord('h') + 1)]:
            res += f"{char} | " 
        return res
b1 = Board()
b1.creat_board()
print(b1)                



