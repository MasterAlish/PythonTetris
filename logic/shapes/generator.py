from random import randint
from logic.shapes.type import *


class ShapeGenerator:
    @staticmethod
    def random_shape(start_x):
        color = randint(1, 10)
        shape_classes = [ShapeS, ShapeL, ShapeT, ShapeZ, ShapeLine, ShapeMirroredL, ShapeSquare]
        random_shape = randint(0, len(shape_classes) - 1)
        shape_class = shape_classes[random_shape]
        return shape_class(start_x, 0, color)