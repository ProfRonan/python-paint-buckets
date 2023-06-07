"""Esse arquivo testa o arquivo main.py"""

import importlib  # para importar o módulo main dinamicamente
import io  # para capturar a saída do print
import sys  # para restaurar o stdout padrão e remover o módulo main do cache
import unittest  # para criar o caso de teste
from unittest.mock import patch  # para simular a entrada do usuário


class TestMain(unittest.TestCase):
    """Class for testing the main.py file"""

    def setUp(self):
        """
        Inicializa o ambiente de teste removendo o módulo principal do cache.
        Isso é necessário para ser capaz de importá-lo novamente em cada teste.
        """
        sys.modules.pop("main", None)

    @patch("builtins.input", return_value="0")
    def test_tintas_0(self, _mock_input):
        """
        Testa se o programa imprime "Serão necessárias 0 latas totalizando R$ 0"
        quando o usuário digita 0
        """
        captured_output = io.StringIO()
        sys.stdout = captured_output
        importlib.import_module("main")
        sys.stdout = sys.__stdout__
        self.assertIn(
            "Serão necessárias 0 latas totalizando R$ 0",
            captured_output.getvalue().strip(),
        )

    @patch("builtins.input", return_value="1")
    def test_tintas_1(self, _mock_input):
        """
        Testa se o programa imprime "Serão necessárias 1 latas totalizando R$ 80"
        quando o usuário digita 1
        """
        captured_output = io.StringIO()
        sys.stdout = captured_output
        importlib.import_module("main")
        sys.stdout = sys.__stdout__
        self.assertIn(
            "Serão necessárias 1 latas totalizando R$ 80",
            captured_output.getvalue().strip(),
        )

    @patch("builtins.input", return_value="2")
    def test_tintas_2(self, _mock_input):
        """
        Testa se o programa imprime "Serão necessárias 1 latas totalizando R$ 80"
        quando o usuário digita 2
        """
        captured_output = io.StringIO()
        sys.stdout = captured_output
        importlib.import_module("main")
        sys.stdout = sys.__stdout__
        self.assertIn(
            "Serão necessárias 1 latas totalizando R$ 80",
            captured_output.getvalue().strip(),
        )

    @patch("builtins.input", return_value="54")
    def test_tintas_54(self, _mock_input):
        """
        Testa se o programa imprime "Serão necessárias 1 latas totalizando R$ 80"
        quando o usuário digita 54
        """
        captured_output = io.StringIO()
        sys.stdout = captured_output
        importlib.import_module("main")
        sys.stdout = sys.__stdout__
        self.assertIn(
            "Serão necessárias 1 latas totalizando R$ 80",
            captured_output.getvalue().strip(),
        )

    @patch("builtins.input", return_value="55")
    def test_tintas_55(self, _mock_input):
        """
        Testa se o programa imprime "Serão necessárias 2 latas totalizando R$ 160"
        quando o usuário digita 55
        """
        captured_output = io.StringIO()
        sys.stdout = captured_output
        importlib.import_module("main")
        sys.stdout = sys.__stdout__
        self.assertIn(
            "Serão necessárias 2 latas totalizando R$ 160",
            captured_output.getvalue().strip(),
        )

    @patch("builtins.input", return_value="215")
    def test_tintas_215(self, _mock_input):
        """
        Testa se o programa imprime "Serão necessárias 4 latas totalizando R$ 320"
        quando o usuário digita 215
        """
        captured_output = io.StringIO()
        sys.stdout = captured_output
        importlib.import_module("main")
        sys.stdout = sys.__stdout__
        self.assertIn(
            "Serão necessárias 4 latas totalizando R$ 320",
            captured_output.getvalue().strip(),
        )
