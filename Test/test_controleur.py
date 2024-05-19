import unittest
from unittest.mock import MagicMock
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from controleur import Controleur
from modele import Modele

class TestControleur(unittest.TestCase):

    def setUp(self):
        self.modele = Modele("Test", "ValeurTest")
        self.vue = MagicMock()
        self.controleur = Controleur(self.modele, self.vue)

        self.controleur.led_rouge = MagicMock()
        self.controleur.led_vert = MagicMock()
        self.controleur.buzzer = MagicMock()

    def test_validate_code_correct(self):
        self.controleur.set_input_code("5629")
        result = self.controleur.validate_code()
        self.assertTrue(result)
        self.vue.journal_listbox.insert.assert_called_with('end', unittest.mock.ANY)
    
    def test_validate_code_incorrect(self):
        self.controleur.set_input_code("1234")
        result = self.controleur.validate_code()
        self.assertFalse(result)
        self.controleur.set_input_code("5678")
        result = self.controleur.validate_code()
        self.assertFalse(result)
        self.controleur.set_input_code("9101")
        result = self.controleur.validate_code()
        self.assertFalse(result)
        self.vue.journal_listbox.insert.assert_called_with('end', unittest.mock.ANY)

if __name__ == '__main__':
    unittest.main()
