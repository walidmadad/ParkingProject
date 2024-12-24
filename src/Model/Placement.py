from datetime import date

class Placement:
    """
    La classe Placement représente un emplacement de véhicule, avec une période de début et de fin, et un statut indiquant si l'emplacement est encore en cours.

    Attributs :
        dateDebut (date) : La date de début de l'occupation de l'emplacement.
        dateFin (date) : La date de fin de l'occupation de l'emplacement.
        estEnCours (bool) : Indique si l'emplacement est actuellement occupé (True) ou non (False).
        voiture (Voiture) : La voiture qui occupe l'emplacement.
        place (Place) : La place de parking où la voiture est stationnée.
    """

    def __init__(self, voiture, place, dateDebut: date, dateFin: date, estEnCours: bool):
        """
        Initialise un nouvel emplacement avec les informations spécifiées.

        Args:
            voiture (Voiture) : La voiture qui occupe l'emplacement.
            place (Place) : La place de parking où la voiture est stationnée.
            dateDebut (date) : La date à laquelle l'occupation de l'emplacement commence.
            dateFin (date) : La date à laquelle l'occupation de l'emplacement se termine.
            estEnCours (bool) : Indique si l'occupation est toujours en cours.
        """
        self.voiture = voiture
        self.place = place
        self.dateDebut = dateDebut
        self.dateFin = dateFin
        self.estEnCours = estEnCours

    def partirPlace(self):
        """
        Marque la fin de l'occupation de l'emplacement et le rend disponible à nouveau.

        Cette méthode met à jour l'attribut estEnCours à False.

        Returns:
            None
        """
        self.place.estLibre = True
        self.estEnCours = False
        self.voiture = None
        self.place = None
