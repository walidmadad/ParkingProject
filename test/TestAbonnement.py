import unittest
from datetime import datetime, date

from src.Model.Abonnement import Abonnement
from src.Model.Contrat import Contrat


class TestAbonnement(unittest.TestCase):



    def test_creation_abonnement(self):
        """
        Teste la création d'un objet `Abonnement`.
        """
        ab = Abonnement("Super Abonnement", 150.00,True)
        self.assertTrue("Super Abonnement", ab.libelle)
        self.assertTrue(150.00, ab.prix)
        self.assertTrue(True, ab.estPackGar)

    def test_add_contrat(self):
        """
        Teste l'ajout d'un contrat à un abonnement.
        """
        contrat = Contrat(datetime.today(), "12-12-2024", True)
        ab = Abonnement("Super Abonnement", 150.00, True)

        ab.addContrat(contrat)
        self.assertTrue(contrat, ab.mes_contrats[0])


if __name__ == '__main__':
    unittest.main()
