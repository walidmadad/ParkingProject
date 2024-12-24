from Model.Placement import Placement

class Place:
    """
    La classe Place représente une place de parking, avec un numéro, un niveau, des dimensions, et un statut d'occupation.

    Attributs :
        numero (int) : Le numéro de la place de parking.
        niveau (int) : Le niveau de la place (par exemple, étage ou niveau du parking).
        longueur (float) : La longueur de la place de parking.
        hauteur (float) : La hauteur de la place de parking.
        estLibre (bool) : Indique si la place est libre (True) ou occupée (False).
    """

    def __init__(self, numero: int, niveau: chr, longueur: float, hauteur: float, estLibre: bool):
        """
        Initialise une nouvelle place de parking avec les informations spécifiées.

        Args:
            numero (int) : Le numéro de la place de parking.
            niveau (int) : Le niveau de la place (par exemple, 1 pour le rez-de-chaussée, 2 pour le premier étage, etc.).
            longueur (float) : La longueur de la place de parking.
            hauteur (float) : La hauteur de la place de parking.
            estLibre (bool) : Indique si la place est libre ou occupée.
        """
        self.numero = numero
        self.niveau = niveau
        self.longueur = longueur
        self.estLibre = estLibre
        self.hauteur = hauteur
        self.placements = []
        self.id_parking = f"{self.niveau}{self.numero}"

    def addPlacementP(self, p: Placement):
        """
        Associe un placement à la place de parking.

        Args:
            p (Placement) : L'objet Placement représentant l'occupation de la place de parking.

        Returns:
            None
        """
        if self.estLibre:
            self.placements.append(p)
            self.estLibre = False  # Marque la place comme occupée
        else:
            print(f"Place {self.id_parking} déjà occupée. Impossible d'ajouter un placement.")

    def __str__(self):
        return f"Place {self.id_parking}"

