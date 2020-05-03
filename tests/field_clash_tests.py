from unittest import TestCase

from logic.field import TetrisField
from logic.shapes.type import ShapeZ, ShapeT, ShapeS


class FieldClashTestCase(TestCase):
    def setUp(self):
        self.field = TetrisField(5, 5)

    def test_shape_clashes_when_shape_cell_is_left_of_field(self):
        shape = ShapeT(-1, 0, 2)
        self.assertTrue(self.field.clashes_with(shape))

    def test_shape_clashes_1(self):
        shape = ShapeT(4, 0, 2)
        self.assertTrue(self.field.clashes_with(shape))

    def test_shape_not_clashes_0(self):
        shape = ShapeT(2, 0, 2)
        self.assertFalse(self.field.clashes_with(shape))

    def test_shape_not_clashes_1(self):
        shape = ShapeT(3, 0, 2)
        self.assertFalse(self.field.clashes_with(shape))

    def test_shape_not_clashes(self):
        shape = ShapeT(0, 0, 2)
        self.assertFalse(self.field.clashes_with(shape))

    def test_shape_not_clashes_2(self):
        shape = ShapeS(0, 0, 2)
        self.assertFalse(self.field.clashes_with(shape))

    def test_shape_not_clashes_3(self):
        shape = ShapeS(3, 0, 2)
        self.assertFalse(self.field.clashes_with(shape))
