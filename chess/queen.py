from chess.figure import AbstractChessFigure
from chess.colors import Color
import logging

class Queen(AbstractChessFigure):
    
    def char(self):
        if self.color == Color.WHITE:
            return '♕'
        else:
            return '♛'

    def can_move(self, row, col):
        logging.debug(f'Проверка королевы на ход')
        if abs(self.row - row) == abs(self.col - col):
            return True
        else:
            if self.row == row or self.col == col:
                return True
            else:
                return False