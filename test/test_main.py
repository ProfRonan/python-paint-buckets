"""Esse arquivo testa o arquivo main.py"""

import importlib  # for importing the main.py file
import io  # for capturing the output
import sys  # for restoring the stdout and removing the main module from the cache
import unittest  # for creating the test case
from unittest.mock import patch  # for mocking the input


class TestMain(unittest.TestCase):
    """Class for testing the main.py file"""

    def setUp(self):
        """Sets up the test environment by removing the main module from the cache"""
        super().setUp()
        sys.modules.pop("main", None)

    @patch("builtins.input", return_value="0")
    def test_tintas_0(self, _mock_input):
        """Testa se o programa imprime "Serão necessárias 0 latas totalizando R$ 0"
        quando o usuário digita 0"""
        captured_output = io.StringIO()
        sys.stdout = captured_output
        importlib.import_module("main")
        sys.stdout = sys.__stdout__
        self.assertIn("Serão necessárias 0 latas totalizando R$ 0",
                      captured_output.getvalue().strip())

    @patch("builtins.input", return_value="1")
    def test_tintas_1(self, _mock_input):
        """Testa se o programa imprime "Serão necessárias 1 latas totalizando R$ 80"
        quando o usuário digita 1"""
        captured_output = io.StringIO()
        sys.stdout = captured_output
        importlib.import_module("main")
        sys.stdout = sys.__stdout__
        self.assertIn("Serão necessárias 1 latas totalizando R$ 80",
                      captured_output.getvalue().strip())

    @patch("builtins.input", return_value="2")
    def test_tintas_2(self, _mock_input):
        """Testa se o programa imprime "Serão necessárias 1 latas totalizando R$ 80"
        quando o usuário digita 2"""
        captured_output = io.StringIO()
        sys.stdout = captured_output
        importlib.import_module("main")
        sys.stdout = sys.__stdout__
        self.assertIn("Serão necessárias 1 latas totalizando R$ 80",
                      captured_output.getvalue().strip())

    @patch("builtins.input", return_value="54")
    def test_tintas_54(self, _mock_input):
        """Testa se o programa imprime "Serão necessárias 1 latas totalizando R$ 80"
        quando o usuário digita 54"""
        captured_output = io.StringIO()
        sys.stdout = captured_output
        importlib.import_module("main")
        sys.stdout = sys.__stdout__
        self.assertIn("Serão necessárias 1 latas totalizando R$ 80",
                      captured_output.getvalue().strip())

    @patch("builtins.input", return_value="55")
    def test_tintas_55(self, _mock_input):
        """Testa se o programa imprime "Serão necessárias 2 latas totalizando R$ 160"
        quando o usuário digita 55"""
        captured_output = io.StringIO()
        sys.stdout = captured_output
        importlib.import_module("main")
        sys.stdout = sys.__stdout__
        self.assertIn("Serão necessárias 2 latas totalizando R$ 160",
                      captured_output.getvalue().strip())

    @patch("builtins.input", return_value="215")
    def test_tintas_215(self, _mock_input):
        """Testa se o programa imprime "Serão necessárias 4 latas totalizando R$ 320"
        quando o usuário digita 215"""
        captured_output = io.StringIO()
        sys.stdout = captured_output
        importlib.import_module("main")
        sys.stdout = sys.__stdout__
        self.assertIn("Serão necessárias 4 latas totalizando R$ 320",
                      captured_output.getvalue().strip())
