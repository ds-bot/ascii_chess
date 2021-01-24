from chess.figure import AbstractChessFigure
from chess.colors import Color
import logging

class Knight(AbstractChessFigure):

    def char(self):
        if self.color == Color.WHITE:
            return '♘'
        else:
            return '♞'
        
    def can_move(self, row, col):
        logging.debug(f'Проверка коня на ход')
        dx = abs(self.col - col)
        dy = abs(self.row - row)
        if abs(dx*dy) == 2:
            return True
        else:
            return False
