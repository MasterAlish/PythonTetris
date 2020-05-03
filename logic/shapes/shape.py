from logic.field import TetrisField


class Shape(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.size = 3
        self.cells = []
        self.rotatable = True

    def can_move_down(self, field: TetrisField):
        my_future = self.clone()
        my_future.y += 1
        return not field.clashes_with(my_future)

    def move_down(self, field: TetrisField):
        my_future = self.clone()
        my_future.y += 1
        if not field.clashes_with(my_future):
            self.y += 1

    def move_right(self, field: TetrisField):
        my_future = self.clone()
        my_future.x += 1
        if not field.clashes_with(my_future):
            self.x += 1

    def move_left(self, field: TetrisField):
        my_future = self.clone()
        my_future.x -= 1
        if not field.clashes_with(my_future):
            self.x -= 1

    def rotate(self, field: TetrisField):
        pass

    def clone(self):
        clone = Shape(self.x, self.y)
        clone.size = self.size
        clone.rotatable = self.rotatable
        clone.cells = [[self.cells[y][x] for x in range(self.size)] for y in range(self.size)]
        return clone
