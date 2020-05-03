from unittest import TestCase

from logic.shapes.type import ShapeS, ShapeT


class ShapeTestCase(TestCase):
    def test_shape_S_clones_correctly(self):
        shape = ShapeS(2, 3, 2)
        clone = shape.clone()
        self.assertEqual(shape.x, clone.x)
        self.assertEqual(shape.y, clone.y)
        self.assertEqual(shape.size, clone.size)
        self.assertEqual(shape.rotatable, clone.rotatable)
        self.assertListEqual(shape.cells, clone.cells)

    def test_shape_T_clones_correctly(self):
        shape = ShapeT(2, 3, 2)
        clone = shape.clone()
        self.assertEqual(shape.x, clone.x)
        self.assertEqual(shape.y, clone.y)
        self.assertEqual(shape.size, clone.size)
        self.assertEqual(shape.rotatable, clone.rotatable)
        self.assertListEqual(shape.cells, clone.cells)
