import unittest
from datetime import datetime

from src.Controller.Entretien import Entretien
from src.Model.Voiture import Voiture


class TestEntretien(unittest.TestCase):
    """
    Classe de test pour la classe Entretien. Utilise la bibliothèque unittest pour tester les méthodes de la classe Entretien.
    """

    def setUp(self):
        """
        Initialisation des objets communs pour les tests.
        """
        self.date_demande = datetime(2024, 12, 15, 14, 30)
        self.date_service = datetime(2024, 12, 16, 10, 0)
        self.rapport = "Rapport initial."
        self.voiture = Voiture(immatriculation="AB-123-CD", hauteur=1.5, longueur=4.0)

    def test_effectuer_entretien(self):
        """
        Teste la méthode `effectuerEntretien` de la classe Entretien.
        """
        entretien = Entretien(self.date_demande, self.date_service, self.rapport)
        result = entretien.effectuerEntretien()

        # Vérifie le retour de la méthode
        self.assertEqual(result, "Entretien effectué.")




if __name__ == '__main__':
    """
    Exécute les tests unitaires lorsque le script est exécuté directement.
    """
    unittest.main()
