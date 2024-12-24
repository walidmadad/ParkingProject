import unittest

from src.Controller.Camera import Camera
from src.Model.Voiture import Voiture


class TestCamera(unittest.TestCase):

    def test_capturer_hauteur(self):
        """
        Tester la méthode capturerHauteur sans implémenter la méthode.
        """
        voiture2 = Voiture("FR15483", 2, 4.0, False)
        camera = Camera()
        self.assertTrue(2, camera.capturerHauteur(voiture2))

    def test_capturer_longueur(self):
        """
        Tester la méthode capturerLongueur sans implémenter la méthode.
        """
        voiture2 = Voiture("FR15483", 2, 4.0, False)
        camera = Camera()
        self.assertTrue(4.0, camera.capturerHauteur(voiture2))
    def test_capturer_immat(self):
        """
        Tester la méthode capturerImmat sans implémenter la méthode.
        """
        voiture2 = Voiture("FR15483", 2, 4.0, False)
        camera = Camera()
        self.assertTrue("FR15483", camera.capturerImmat(voiture2))

if __name__ == '__main__':
    unittest.main()
