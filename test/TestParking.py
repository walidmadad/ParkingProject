import unittest

from src.Model.Parking import Parking
from src.Model.Place import Place
from src.Model.Voiture import Voiture
from src.Controller.Camera import Camera


class MockCamera(Camera):
    def capturerLongueur(self, v: Voiture):
        return v.longueur

    def capturerHauteur(self, v: Voiture):
        return v.hauteur

class MockVoiture(Voiture):
    def __init__(self, longueur, hauteur):
        self.longueur = longueur
        self.hauteur = hauteur

class TestParking(unittest.TestCase):
    def setUp(self):
        # Création d'un parking pour chaque test
        self.parking = Parking(nbPlacesParNiveau=10, nbPlacesLibres=30, prix=5, nbNiveaux=3)
        self.parking.Camera = MockCamera  # Mock pour éviter des dépendances inutiles

    def test_creation_parking(self):
        """
        Teste la création d'un parking et vérifie les valeurs des attributs.
        """
        self.assertEqual(self.parking.nbPlacesParNiveau, 10)
        self.assertEqual(self.parking.nbPlacesLibres, 30)
        self.assertEqual(self.parking.prix, 5)
        self.assertEqual(self.parking.nbNiveaux, 3)
        self.assertEqual(len(self.parking.mes_places), 30)  # 3 niveaux x 10 places

        # Vérifier la configuration des places
        place_niveau_a = [place for place in self.parking.mes_places if place.niveau == 'A']
        self.assertEqual(len(place_niveau_a), 10)
        self.assertEqual(place_niveau_a[0].longueur, 10.0)
        self.assertEqual(place_niveau_a[0].hauteur, 4.0)

    def test_rechercher_place(self):
        """
        Teste la recherche d'une place pour une voiture dans le parking.
        """
        voiture = MockVoiture(longueur=4.0, hauteur=2.0)
        place_trouvee = self.parking.rechercherPlace(voiture)
        self.assertIsNotNone(place_trouvee)
        self.assertTrue(place_trouvee.estLibre)
        self.assertGreaterEqual(place_trouvee.longueur, voiture.longueur)
        self.assertGreaterEqual(place_trouvee.hauteur, voiture.hauteur)

        # Occuper la place et vérifier qu'elle est marquée comme occupée
        self.parking.occuperPlace(place_trouvee)
        self.assertFalse(place_trouvee.estLibre)
        self.assertEqual(self.parking.nbPlacesLibres, 28)

    def test_nb_places_libres_par_niveau(self):
        """
        Teste le nombre de places libres pour un niveau donné.
        """
        self.assertEqual(self.parking.nbPlaceLibresParNiveau('A'), 10)
        self.assertEqual(self.parking.nbPlaceLibresParNiveau('B'), 10)
        self.assertEqual(self.parking.nbPlaceLibresParNiveau('C'), 10)

        # Occuper une place sur le niveau A et révérifier
        place = [place for place in self.parking.mes_places if place.niveau == 'A'][0]
        self.parking.occuperPlace(place)
        self.assertEqual(self.parking.nbPlaceLibresParNiveau('A'), 9)

if __name__ == '__main__':
    unittest.main()
