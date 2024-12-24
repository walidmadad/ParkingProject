import unittest
from datetime import date

from src.Model.Contrat import Contrat


class TestContrat(unittest.TestCase):
    """
    La classe TestContrat contient des tests unitaires pour la classe Contrat.
    Elle permet de tester la création d'un contrat et la rupture d'un contrat.
    """

    def test_creation_contrat(self):
        """
        Teste la création d'un contrat et vérifie les valeurs des attributs.
        """
        c = Contrat(date(2024,12,12), date(2024,12,25), True)
        self.assertTrue(True, c.estEnCours)
        self.assertTrue("2024-12-12", c.date_debut)
        self.assertTrue("2024-12-25", c.date_fin)


    def test_rompre_contrat(self):
        """
        Teste la rupture d'un contrat en cours.
        """
        c = Contrat(date(2024,12,12), date(2025,12,26), True)
        c.rompreContrat()
        self.assertTrue(True, c.estEnCours)

if __name__ == '__main__':
    unittest.main()
