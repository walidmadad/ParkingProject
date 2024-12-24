import unittest
from datetime import datetime

from src.Controller.Maintenance import Maintenance
from src.Model.Voiture import Voiture


class TestMaintenance(unittest.TestCase):
    """
    Classe de test pour la classe Maintenance. Utilise la bibliothèque unittest pour tester les méthodes de la classe Maintenance.
    """

    def setUp(self):
        """
        Initialisation des objets communs pour les tests.
        """
        self.date_demande = datetime(2024, 12, 15, 14, 30)
        self.date_service = datetime(2024, 12, 16, 10, 0)
        self.rapport = "Rapport initial."
        self.voiture = Voiture(immatriculation="AB-123-CD", hauteur=1.5, longueur=4.0)


    def test_effectuer_maintenance(self):
        """
        Teste la méthode `effectuerMaintenance` de la classe Maintenance.
        """
        maintenance = Maintenance(self.date_demande, self.date_service, self.rapport)
        result = maintenance.effectuerMaintenance(self.voiture)

        # Vérifie le retour de la méthode
        self.assertEqual(result, f"Effectuer maintenance sur la voiture : {self.voiture.immatriculation}")



if __name__ == '__main__':
    """
    Exécute les tests unitaires lorsque le script est exécuté directement.
    """
    unittest.main()
