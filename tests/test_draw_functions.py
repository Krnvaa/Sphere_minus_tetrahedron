import unittest
from unittest.mock import patch, call

from src.draw_functions import draw_sphere, draw_tetrahedron


class TestDrawFunctions(unittest.TestCase):
    @patch('src.draw_functions.glColor3f')
    @patch('src.draw_functions.gluSphere')
    @patch('src.draw_functions.gluNewQuadric')
    def test_draw_sphere(self, mock_gluNewQuadric, mock_gluSphere, mock_glColor3f):
        radius = 1.0
        draw_sphere(radius)
        mock_glColor3f.assert_called_once_with(0.8, 0.4, 0.8)
        mock_gluNewQuadric.assert_called_once()
        mock_gluSphere.assert_called_once_with(mock_gluNewQuadric.return_value, radius, 100, 100)

    @patch('src.draw_functions.glBegin')
    @patch('src.draw_functions.glEnd')
    @patch('src.draw_functions.glVertex3f')
    @patch('src.draw_functions.glColor3f')
    def test_draw_tetrahedron(self, mock_glColor3f, mock_glVertex3f, mock_glEnd, mock_glBegin):
        draw_tetrahedron()
        expected_calls = [
            unittest.mock.call(0.0, 1.5, 0.0),
            unittest.mock.call(1.0, -1.0, -1.0),
            unittest.mock.call(-1.0, -1.0, -1.0),
            unittest.mock.call(0.0, 1.5, 0.0),
            unittest.mock.call(-1.0, -1.0, -1.0),
            unittest.mock.call(-1.0, -1.0, 1.0),
            unittest.mock.call(-1.0, -1.0, 1.0),
            unittest.mock.call(1.0, -1.0, 1.0),
            unittest.mock.call(1.0, -1.0, -1.0),
            unittest.mock.call(-1.0, -1.0, 1.0),
            unittest.mock.call(1.0, -1.0, -1.0),
            unittest.mock.call(-1.0, -1.0, -1.0)
        ]
        mock_glColor3f.assert_called_once_with(0.0, 0.0, 0.0)
        mock_glVertex3f.assert_has_calls(expected_calls)
        mock_glBegin.assert_called_once_with(4)
        mock_glEnd.assert_called_once()
