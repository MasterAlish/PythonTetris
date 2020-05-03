from logic.field import TetrisField
from logic.shapes.generator import ShapeGenerator


class Tetris(object):
    def __init__(self, cols, rows):
        self.field = TetrisField(cols, rows)
        self.next_shape = self.random_shape()
        self.current_shape = self.random_shape()

    def generate_cells(self):
        pass

    def touchdown(self):
        pass

    def rotate(self):
        pass

    def move_right(self):
        pass

    def move_left(self):
        pass

    def random_shape(self):
        start_x = int(self.field.cols/2-2)
        return ShapeGenerator.random_shape(start_x)
