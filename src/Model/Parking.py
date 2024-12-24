from Controller.Camera import Camera
from Model.Abonnement import Abonnement
from Model.Place import Place
from Model.Voiture import Voiture


class Parking:
    _instance = None  # Singleton

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Parking, cls).__new__(cls)
            cls._instance.initialized = False
        return cls._instance

    @classmethod
    def get_instance(cls):
        # Retourne l'instance unique du parking
        return cls._instance
    """
    La classe Parking représente un parking avec plusieurs places de stationnement réparties sur plusieurs niveaux.

    Attributs :
        nbPlacesParNiveau (int) : Le nombre de places disponibles par niveau du parking.
        nbPlacesLibres (int) : Le nombre total de places libres dans le parking.
        prix (int) : Le prix pour stationner dans le parking (par exemple, par heure).
        nbNiveaux (int) : Le nombre total de niveaux du parking.
    """

    def __init__(self, nbPlacesParNiveau: int, nbPlacesLibres: int, prix: int, nbNiveaux: int):
        """
        Initialise un nouveau parking avec les informations spécifiées.

        Args:
            nbPlacesParNiveau (int) : Le nombre de places disponibles par niveau.
            nbPlacesLibres (int) : Le nombre de places libres dans le parking.
            prix (int) : Le prix de stationnement dans le parking.
            nbNiveaux (int) : Le nombre de niveaux du parking.
        """
        if not self.initialized:  # Initialiser uniquement la première fois
            self.nbPlacesParNiveau = nbPlacesParNiveau
            self.nbPlacesLibres = nbPlacesLibres
            self.prix = prix
            self.nbNiveaux = nbNiveaux
            self.mes_places = []
            self.mes_abonnements = []
            self.initialized = True
            self.nbVoituresStatistiques = 0
            self.nbClientAbonnes = 0
            self.nbClientSuperAbonnes = 0
            self.nbNouveauAbonnement = 0
            self.nbClientNonAbonnes = 0

            dimensions_par_niveau = {
                'A': {'longueur': 10.0, 'hauteur': 4.0},  # Niveau A : Pour camions
                'B': {'longueur': 5.0, 'hauteur': 2.5},  # Niveau B : Pour voitures
                'C': {'longueur': 2.5, 'hauteur': 1.5}   # Niveau C : Pour motos
            }

            for niveau in range(nbNiveaux):
                # Convertir l'indice du niveau en lettre (par exemple 0 -> 'A', 1 -> 'B')
                niveau_str = chr(65 + niveau)  # 65 est le code ASCII de 'A'
                dimensions = dimensions_par_niveau.get(niveau_str, {'longueur': 5.0, 'hauteur': 2.5})

                for numero in range(1, nbPlacesParNiveau + 1):  # Numéros commencent à 1
                    self.mes_places.append(
                        Place(numero=numero, niveau=niveau_str,
                              longueur=dimensions['longueur'],
                              hauteur=dimensions['hauteur'],
                              estLibre=True)
                    )

    def rechercherPlace(self, v: Voiture) -> Place:
        """
        Recherche une place disponible pour une voiture donnée.

        Args:
            v (Voiture) : L'objet Voiture pour lequel une place de parking doit être trouvée.

        Returns:
            Place : Un objet Place représentant l'emplacement trouvé pour la voiture dans le parking.
        """
        camera = Camera()

        for place in self.mes_places:
            if place.estLibre and place.longueur >= camera.capturerLongueur(v) and place.hauteur >= camera.capturerHauteur(v):
                return place
        return None


    def nbPlaceLibresParNiveau(self, niveau: str) -> int:
        """
        Retourne le nombre de places libres disponibles sur un niveau donné.

        Args:
            niveau (str) : Le niveau du parking pour lequel on veut connaître le nombre de places libres.

        Returns:
            int : Le nombre de places libres sur le niveau spécifié.
        """
        return sum(1 for place in self.mes_places if place.niveau == niveau and place.estLibre)


    def addAbonnement(self, ab: Abonnement):
        """
        Ajoute un abonnement pour un utilisateur au parking.

        Cette méthode permet d'ajouter un abonnement à un utilisateur afin qu'il puisse bénéficier de certaines réductions ou accès prioritaires.

        Args:
            ab (Abonnement) : L'objet Abonnement représentant l'abonnement à ajouter.

        """
        self.nbNouveauAbonnement += 1
        self.mes_abonnements.append(ab)

    def occuperPlace(self, place: Place):
        """
        Marque une place comme occupée.
        """
        place.estLibre = False
        self.nbPlacesLibres -= 1
        self.nbVoituresStatistiques += 1

    def libererPlace(self, place: Place):
        place.estLibre = True
        self.nbPlacesLibres += 1