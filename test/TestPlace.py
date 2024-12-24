import unittest
from src.Model.Placement import Placement
from src.Model.Place import Place
from src.Model.Voiture import Voiture


class TestPlace(unittest.TestCase):
    """
    Classe de test pour la classe Place. Utilise la bibliothèque unittest pour tester les méthodes de la classe Place.
    """

    def test_creation_place(self):
        """
        Teste la création d'un objet Place avec des attributs spécifiques.
        """
        place = Place(numero=1, niveau='A', longueur=5.0, hauteur=2.0, estLibre=True)

        # Vérifie que les attributs sont initialisés correctement
        self.assertEqual(place.numero, 1)
        self.assertEqual(place.niveau, 'A')
        self.assertEqual(place.longueur, 5.0)
        self.assertEqual(place.hauteur, 2.0)
        self.assertTrue(place.estLibre)
        self.assertEqual(place.id_parking, 'A1')

    def test_add_placement(self):
        """
        Teste la méthode addPlacementP de la classe Place.
        """
        voiture1 = Voiture("ABC123", 1.5, 4.0, False)
        place = Place(numero=1, niveau='B', longueur=5.0, hauteur=2.5, estLibre=True)
        placement = Placement(voiture1, place, 2024-12-16, 2024-12-20, True)

        # Ajoute un placement à une place libre
        place.addPlacementP(placement)

        # Vérifie que le placement a été ajouté et que la place est occupée
        self.assertEqual(len(place.placements), 1)
        self.assertFalse(place.estLibre)
        self.assertEqual(place.placements[0], placement)



    def test_to_string(self):
        """
        Teste la méthode __str__ de la classe Place.
        """
        place = Place(numero=10, niveau='C', longueur=6.0, hauteur=2.5, estLibre=True)
        self.assertEqual(str(place), "Place C10")


if __name__ == '__main__':
    """
    Exécute les tests unitaires lorsque le script est exécuté directement.
    """
    unittest.main()
