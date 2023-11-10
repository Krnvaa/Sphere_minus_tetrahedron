import unittest
from unittest.mock import patch
from src.pygame_window import create_pygame_window

class TestPygameWindow(unittest.TestCase):
    @patch('src.pygame_window.pygame.init')
    @patch('src.pygame_window.pygame.display.set_mode')
    @patch('src.pygame_window.OPENGL')
    @patch('src.pygame_window.DOUBLEBUF')
    @patch('src.pygame_window.gluPerspective')
    def test_create_pygame_window(self, mock_gluPerspective, mock_DOUBLEBUF, mock_OPENGL, mock_set_mode, mock_init):
        display = (800, 600)
        create_pygame_window()
        mock_init.assert_called_once()
        mock_set_mode.assert_called_once_with(display, mock_DOUBLEBUF | mock_OPENGL)
        mock_gluPerspective.assert_called_once_with(45, (display[0] / display[1]), 0.1, 50.0)