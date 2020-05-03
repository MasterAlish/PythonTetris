from logic.shapes.shape import Shape


class ShapeS(Shape):
    def __init__(self, x, y, c):
        """
        :param c: Color of shape
        """
        super().__init__(x, y)
        self.cells = [[c, 0, 0],
                      [c, c, 0],
                      [0, c, 0]]


class ShapeZ(Shape):
    def __init__(self, x, y, c):
        super().__init__(x, y)
        self.cells = [[0, 0, c],
                      [0, c, c],
                      [0, c, 0]]


class ShapeT(Shape):
    def __init__(self, x, y, c):
        super().__init__(x, y)
        self.cells = [[0, c, 0],
                      [c, c, 0],
                      [0, c, 0]]


class ShapeL(Shape):
    def __init__(self, x, y, c):
        super().__init__(x, y)
        self.cells = [[0, c, 0],
                      [0, c, 0],
                      [0, c, c]]


class ShapeMirroredL(Shape):
    def __init__(self, x, y, c):
        super().__init__(x, y)
        self.cells = [[0, c, 0],
                      [0, c, 0],
                      [c, c, 0]]


class ShapeLine(Shape):
    def __init__(self, x, y, c):
        super().__init__(x, y)
        self.size = 4
        self.cells = [[0, c, 0, 0],
                      [0, c, 0, 0],
                      [0, c, 0, 0],
                      [0, c, 0, 0]]


class ShapeSquare(Shape):
    def __init__(self, x, y, c):
        super().__init__(x, y)
        self.size = 2
        self.rotatable = False
        self.cells = [[c, c],
                      [c, c]]
