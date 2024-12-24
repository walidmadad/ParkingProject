import unittest
from datetime import datetime

from src.Controller.Livraison import Livraison
from src.Model.Voiture import Voiture


class TestLivraison(unittest.TestCase):
    """
    Classe de test pour la classe Livraison. Utilise la bibliothèque unittest pour tester les méthodes de la classe Livraison.
    """

    def setUp(self):
        """
        Initialisation des objets communs pour les tests.
        """
        self.date_demande = datetime(2024, 12, 15, 14, 30)
        self.date_service = datetime(2024, 12, 16, 10, 0)
        self.rapport = "Rapport initial."
        self.voiture = Voiture(immatriculation="AB-123-CD", hauteur=1.5, longueur=4.0)

    def test_effectuer_livraison(self):
        """
        Teste la méthode `effectuerLivraison` de la classe Livraison.
        """
        livraison = Livraison(self.date_demande, self.date_service, self.rapport)
        result = livraison.effectuerLivraison()

        # Vérifie le retour de la méthode
        self.assertEqual(result, "Livraison effectuée.")


if __name__ == '__main__':
    """
    Exécute les tests unitaires lorsque le script est exécuté directement.
    """
    unittest.main()
