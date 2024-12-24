import unittest

from src.Model.Place import Place
from src.Model.Placement import Placement
from src.Model.Voiture import Voiture

class TestVoiture(unittest.TestCase):
    """
    Classe de test pour la classe Voiture. Utilise la bibliothèque unittest pour tester les méthodes de la classe Voiture.
    """

    def test_creation_voiture(self):
        """
        Teste la création d'un objet Voiture avec des attributs spécifiques.
        """
        voiture = Voiture(immatriculation="123-ABC", hauteur=1.5, longueur=4.0, estDansParking=False)

        # Vérifie que les attributs sont initialisés correctement
        self.assertEqual(voiture.immatriculation, "123-ABC")
        self.assertEqual(voiture.hauteur, 1.5)
        self.assertEqual(voiture.longueur, 4.0)
        self.assertFalse(voiture.estDansParking)
        self.assertEqual(len(voiture.placements), 0)
        self.assertIsNone(voiture.client)

    def test_creation_voiture_avec_client(self):
        """
        Teste la création d'une voiture associée à un client.
        """
        class MockClient:
            def __init__(self):
                self.voiture = None

        client = MockClient()
        voiture = Voiture(immatriculation="456-DEF", hauteur=1.6, longueur=4.2, client=client)

        # Vérifie que la voiture est associée au client
        self.assertEqual(voiture.client, client)
        self.assertEqual(client.voiture, voiture)

    def test_add_placement(self):
        """
        Teste la méthode addPlacementV de la classe Voiture.
        """
        voiture = Voiture(immatriculation="789-GHI", hauteur=1.8, longueur=4.5)
        place = Place(numero=1, niveau='B', longueur=5.0, hauteur=2.5, estLibre=True)
        placement = Placement(voiture, place, 2024-12-16, 2024-12-20, True)

        # Ajoute un placement
        voiture.addPlacementV(placement)

        # Vérifie que le placement a été ajouté correctement
        self.assertEqual(len(voiture.placements), 1)
        self.assertTrue(voiture.estDansParking)
        self.assertEqual(voiture.placements[0], placement)

if __name__ == '__main__':
    """
    Exécute les tests unitaires lorsque le script est exécuté directement.
    """
    unittest.main()
