from datetime import date

class Contrat:
    """
    La classe Contrat représente un contrat avec une période de début et de fin, ainsi qu'un statut indiquant s'il est en cours ou non.

    Elle permet de gérer les informations relatives à un contrat et de rompre un contrat si nécessaire.
    """

    def __init__(self, date_debut: date, date_fin: date, estEnCours: bool):
        """
        Initialise un nouveau contrat.

        Args:
            date_debut (date) : La date de début du contrat.
            date_fin (date) : La date de fin du contrat.
            estEnCours (bool) : Un indicateur indiquant si le contrat est actuellement en cours.
        """
        self.date_debut = date_debut
        self.date_fin = date_fin
        self.estEnCours = estEnCours

    def rompreContrat(self):
        """
        Rompt le contrat en cours.

        Cette méthode permet de mettre fin au contrat avant sa date de fin. La logique exacte de la rupture du contrat n'est pas encore définie (méthode vide).

        Returns:
            None
        """
        if date.today() >= self.date_fin:
            self.estEnCours = False
        else:
            self.estEnCours = False