from chess.figure import AbstractChessFigure
from chess.colors import Color
import logging


class King(AbstractChessFigure):

    def char(self):
        if self.color == Color.WHITE:
            return '♔'
        else:
            return '♚'
        
    def can_move(self, row, col):
        logging.debug(f'Проверка короля на ход')
        dx = abs(self.col - col)
        dy = abs(self.row - row)
        if 0 <= dx <= 1 and 0 <= dy <= 1:
            return True
        else:
            return False
