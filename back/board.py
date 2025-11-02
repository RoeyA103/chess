
board = [[None for _ in range(8)] for _ in range(8)]


tools = [Rook, Knight, Bishop, Queen, King, Bishop, Knight, Rook]  

for i, piece_class in enumerate(tools):
    board[0][i] = piece_class("white")  
    board[1][i] = Pawn("white")          


for i, piece_class in enumerate(tools[::-1]):
    board[7][i] = piece_class("black") 
    board[6][i] = Pawn("black")          


for row in board:
    print([type(piece).__name__ if piece else None for piece in row])
