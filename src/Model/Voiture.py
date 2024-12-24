from Model.Placement import Placement

class Voiture:
    """
    La classe Voiture représente une voiture avec des caractéristiques spécifiques telles que l'immatriculation, la hauteur,
    la longueur et son statut dans le parking.

    Attributs :
        immatriculation (str) : L'immatriculation de la voiture.
        hauteur (float) : La hauteur de la voiture.
        longueur (float) : La longueur de la voiture.
        estDansParking (bool) : Indique si la voiture est actuellement dans un parking.
    """

    def __init__(self, immatriculation: str, hauteur: float, longueur: float, estDansParking: bool = False, client=None):
        """
        Initialise une nouvelle voiture avec les attributs spécifiés.

        Args:
            immatriculation (str) : L'immatriculation de la voiture.
            hauteur (float) : La hauteur de la voiture.
            longueur (float) : La longueur de la voiture.
            estDansParking (bool) : Indique si la voiture est dans le parking.
        """
        self.immatriculation = immatriculation
        self.hauteur = hauteur
        self.longueur = longueur
        self.estDansParking = estDansParking
        self.placement = None
        self.client = client
        if client:
            client.voiture = self

    def addPlacementV(self, p: Placement):
        """
        Associe un placement à la voiture. Cette méthode permet d'ajouter un placement pour la voiture,
        mais son comportement n'est pas défini dans cette implémentation (méthode vide).

        Args:
            p (Placement) : L'objet Placement représentant un emplacement dans un parking.

        Returns:
            None
        """
        self.placement = p
        self.estDansParking = True
