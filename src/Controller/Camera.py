from Model.Voiture import Voiture

class Camera:
    """
    La classe Camera représente une caméra utilisée pour capturer les informations d'une voiture.
    Elle permet de capturer la hauteur, la longueur et l'immatriculation d'une voiture donnée.
    """

    @staticmethod
    def capturerHauteur(v: Voiture) -> float:
        """
        Capture la hauteur de la voiture à l'aide de la caméra.

        Args:
            v (Voiture) : La voiture dont la hauteur doit être capturée.

        Returns:
            float : La hauteur de la voiture capturée par la caméra.
        """
        return v.hauteur

    @staticmethod
    def capturerLongueur(v: Voiture) -> float:
        """
        Capture la longueur de la voiture à l'aide de la caméra.

        Args:
            v (Voiture) : La voiture dont la longueur doit être capturée.

        Returns:
            float : La longueur de la voiture capturée par la caméra.
        """
        return v.longueur

    @staticmethod
    def capturerImmat(v: Voiture) -> str:
        """
        Capture l'immatriculation de la voiture à l'aide de la caméra.

        Args:
            v (Voiture) : La voiture dont l'immatriculation doit être capturée.

        Returns:
            str : L'immatriculation de la voiture capturée par la caméra.
        """
        return v.immatriculation
