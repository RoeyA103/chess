class Piece:
    def __init__(self, color: str, symbol_white: str, symbol_black: str):
        if color not in ("white", "black"):
            raise ValueError("Color must be 'white' or 'black'")
        self.color = color
        self.symbol_white = symbol_white
        self.symbol_black = symbol_black

    def __str__(self):
        return self.symbol_white if self.color == "white" else self.symbol_black
p = Piece("white", "♔", "♚")
print(p.__str__())  # Returns "♔"