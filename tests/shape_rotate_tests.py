from unittest import TestCase

from logic.shapes.type import ShapeS, ShapeT, ShapeLine


class ShapeRotateTestCase(TestCase):
    def test_shape_s_rotation(self):
        shape = ShapeS(0, 0, 1)
        shape._rotate_cells()
        expected_cells = [[0, 1, 1],
                          [1, 1, 0],
                          [0, 0, 0]]
        self.assertListEqual(expected_cells, shape.cells)

    def test_shape_t_rotation(self):
        shape = ShapeT(0, 0, 1)
        shape._rotate_cells()
        expected_cells = [[0, 1, 0],
                          [1, 1, 1],
                          [0, 0, 0]]
        self.assertListEqual(expected_cells, shape.cells)

    def test_shape_line_rotation(self):
        shape = ShapeLine(0, 0, 1)
        shape._rotate_cells()
        expected_cells = [[0, 0, 0, 0],
                          [1, 1, 1, 1],
                          [0, 0, 0, 0],
                          [0, 0, 0, 0]]
        self.assertListEqual(expected_cells, shape.cells)
