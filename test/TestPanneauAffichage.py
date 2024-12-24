import unittest

from src.Controller.PanneauAffichage import PanneauAffichage
from src.Model.Parking import Parking


class TestPanneauAffichage(unittest.TestCase):

    def setUp(self):
        # Création d'un parking pour chaque test
        self.parking = Parking(nbPlacesParNiveau=10, nbPlacesLibres=30, prix=5, nbNiveaux=3)
        self.paneau = PanneauAffichage()

    def test_afficherNbPlacesDisponibles(self):
        """
        Tester la méthode afficherNbPlacesDisponibles pour vérifier que le nombre de places est bien affiché.
        """
        self.assertEqual(self.paneau.afficherNbPlacesDisponibles(self.parking), "Il y a 30 places disponibles dans ce parking.")



if __name__ == '__main__':
    unittest.main()
