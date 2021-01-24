from chess.colors import Color
from chess.figure import AbstractChessFigure
import logging


class Bishop(AbstractChessFigure):
    
    def char(self):
        if self.color == Color.WHITE:
            return '♗'
        else:
            return '♝'

    def can_move(self, row, col):
        logging.debug(f'Проверка слона на ход')
        if abs(self.row - row) == abs(self.col - col):
            return True
        else:
            return False
