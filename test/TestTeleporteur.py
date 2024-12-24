import unittest
from datetime import date, timedelta
from src.Model.Voiture import Voiture
from src.Model.Place import Place
from src.Model.Parking import Parking
from src.Controller.Teleporteur import Teleporteur

class TestTeleporteur(unittest.TestCase):
    """
    Classe de test pour la classe Teleporteur.
    Cette classe contient les tests pour vérifier les fonctionnalités de téléportation
    des voitures dans les parkings.
    """

    def setUp(self):
        """
        Méthode exécutée avant chaque test pour initialiser les objets nécessaires.
        """
        self.teleporteur = Teleporteur()
        self.voiture = Voiture("AB-123-CD", 1.5, 4.0)
        self.parking = Parking(nbPlacesParNiveau=10, nbPlacesLibres=30, prix=5, nbNiveaux=3)
        self.place_libre = Place(numero=1, niveau='B', longueur=5.0, hauteur=2.5, estLibre=True)
        self.place_occupee = Place(numero=2, niveau='B', longueur=5.0, hauteur=2.5, estLibre=False)


    def test_teleporter_voiture(self):
        """
        Teste la méthode `teleporterVoiture` de la classe Teleporteur.
        """
        placement = self.teleporteur.teleporterVoiture(self.voiture, self.place_libre)

        # Vérifie que le placement a été correctement créé
        self.assertEqual(placement.voiture, self.voiture)
        self.assertEqual(placement.place, self.place_libre)
        self.assertTrue(placement.estEnCours)
        self.assertEqual(placement.dateDebut, date.today())
        self.assertEqual(placement.dateFin, date.today() + timedelta(days=1))

        # Vérifie que la place est maintenant occupée
        self.assertFalse(self.place_libre.estLibre)

    def test_teleporter_voiture_place_occupee(self):
        """
        Teste que la méthode `teleporterVoiture` lève une erreur si la place est déjà occupée.
        """
        with self.assertRaises(ValueError) as context:
            self.teleporteur.teleporterVoiture(self.voiture, self.place_occupee)
        self.assertEqual(str(context.exception), "La place B2 est déjà occupée.")
if __name__ == '__main__':
    unittest.main()
