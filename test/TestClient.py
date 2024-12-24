import unittest

from src.Model.Abonnement import Abonnement
from src.Model.Client import Client
from src.Model.Voiture import Voiture


class TestClient(unittest.TestCase):
    voiture1 = Voiture("ABC123", 1.5, 4.0, False)
    client1 = Client("Alice", "Rue des Lilas", True, True, 5, voiture1)
    ab = Abonnement("Super Abonnement", 150.00, True)

    def test_sAbonner(self):
        """
        Tester la méthode sAbonner sans implémenter la méthode.
        """

        self.client1.sAbonner(self.ab)
        self.assertTrue(self.ab, self.client1.mon_abonnement)

    def test_nouvelleVoiture(self):
        """
        Tester la méthode nouvelleVoiture sans implémenter la méthode.
        """
        voiture2 = Voiture("FR15483", 2, 4.0, False)
        self.client1.nouvelleVoiture(voiture2.immatriculation, voiture2.hauteur, voiture2.longueur)
        self.assertTrue(voiture2, self.client1.voiture)


    def test_seDesabonner(self):
        """
        Tester la méthode seDesabonner sans implémenter la méthode.
        """
        self.client1.seDesabonner()
        print(self.client1.mon_abonnement)
        self.assertTrue( self.client1.mon_abonnement, "")


    def test_demanderMaintenance(self):
        """
        Tester la méthode demanderMaintenance sans implémenter la méthode.
        """

        self.assertTrue(self.client1.demanderMaintenance(),"Effectuer maintenance sur la voiture : ABC123")
        client2 = Client("Bob", "Rue de Bob", True, True, 4)
        self.assertTrue(client2.demanderMaintenance(), "Aucune voiture associée pour effectuer la maintenance.")

    def test_demanderLivraison(self):
        """
        Tester la méthode demanderLivraison sans implémenter la méthode.
        """


    def test_demanderEntretien(self):
        """
        Tester la méthode demanderEntretien sans implémenter la méthode.
        """


    def test_entrerParking(self):
        """
        Tester la méthode entrerParking sans implémenter la méthode.
        """


if __name__ == '__main__':
    unittest.main()
