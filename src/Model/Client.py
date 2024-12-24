from datetime import datetime
from Model.Abonnement import Abonnement
from Controller.Entretien import Entretien
from Controller.Livraison import Livraison
from Controller.Maintenance import Maintenance
from Model.Voiture import Voiture


class Client:
    """
    La classe Client représente un client qui peut s'abonner à des services et effectuer diverses actions liées à son abonnement,
    à ses voitures et à ses demandes de services.

    Un client possède des informations personnelles comme son nom, son adresse, son statut d'abonnement, et son nombre de fréquentations.
    Il peut également accéder à des services spécifiques comme la maintenance, la livraison, l'entretien, et entrer dans un parking.
    """

    def __init__(self, nom: str, adresse: str, estAbonne: bool, estSuperAbonne: bool, nbrFrequentations: int, voiture=None):
        """
        Initialise un client avec des informations personnelles.

        Args:
            nom (str) : Le nom du client.
            adresse (str) : L'adresse du client.
            estAbonne (bool) : Indicateur si le client est abonné ou non.
            estSuperAbonne (bool) : Indicateur si le client est un super-abonné ou non.
            nbrFrequentations (int) : Le nombre de fois que le client a fréquenté le service.
        """
        self.nom = nom
        self.adresse = adresse
        self.estAbonne = estAbonne
        self.estSuperAbonne = estSuperAbonne
        self.nbrFrequentations = nbrFrequentations
        self.mon_abonnement = ""
        self.voiture = voiture
        if voiture:
            voiture.client = self

    def sAbonner(self, ab: Abonnement):
        """
        Permet au client de s'abonner à un service.

        Cette méthode permet d'abonner un client à un service en associant l'objet `Abonnement` au client.

        Args:
            ab (Abonnement) : L'abonnement à ajouter pour le client.

        Returns:
            None
        """
        self.mon_abonnement = ab


    def nouvelleVoiture(self, imma: str, hautV: float, longV: float):
        """
        Permet au client d'ajouter une nouvelle voiture à son profil.

        Cette méthode permet au client d'ajouter une voiture avec un numéro d'immatriculation, une hauteur et une longueur.

        Args:
            imma (str) : Le numéro d'immatriculation de la voiture.
            hautV (float) : La hauteur de la voiture.
            longV (float) : La longueur de la voiture.

        Returns:
            None
        """
        self.voiture = Voiture(imma, hautV, longV)

    def seDesabonner(self):
        """
        Permet au client de se désabonner du service.

        Cette méthode permet au client de résilier son abonnement.

        Returns:
            None
        """
        self.mon_abonnement = ""

    def demanderMaintenance(self, date_service):
        """
        Permet au client de demander une maintenance pour sa voiture.

        Cette méthode crée un objet Maintenance et effectue la maintenance sur la voiture du client.

        Returns:
            str : Un message indiquant si la maintenance a été demandée.
        """
        if self.voiture is not None:
            try:
                date_demande = datetime.now()
                rapport = f"Maintenance demandée pour la voiture {self.voiture.immatriculation}."
                maintenance = Maintenance(date_demande, date_service, rapport)
                return maintenance.effectuerMaintenance(self.voiture)
            except ValueError:
                return "Format de date invalide. Utilisez le format 'AAAA-MM-JJ'."
        else:
            return "Aucune voiture associée pour effectuer la maintenance."

    def demanderLivraison(self, dateLiv: datetime, heure, adresseLiv: str):
        """
        Permet au client de demander une livraison de sa voiture.

        Cette méthode crée un objet Livraison et effectue la livraison à l'adresse spécifiée.

        Args:
            dateLiv (datetime) : La date de livraison de la voiture.
            heur (int) : L'heure de la livraison.
            adresseLiv (str) : L'adresse de livraison.

        Returns:
            str : Un message indiquant si la livraison a été demandée.
        """
        if self.voiture is not None:
            try:

                rapport = f"Livraison demandée pour la voiture {self.voiture.immatriculation} à {adresseLiv}."
                livraison = Livraison(dateLiv, heure, rapport)
                return livraison.effectuerLivraison()
            except ValueError:
                return "Format de date invalide. Utilisez le format 'AAAA-MM-JJ'."
        else:
            return "Aucune voiture associée pour effectuer la livraison."

    def demanderEntretien(self, date_service):
        """
        Permet au client de demander un entretien pour sa voiture.

        Cette méthode crée un objet Entretien et effectue l'entretien de la voiture du client.

        Returns:
            str : Un message indiquant si l'entretien a été demandé.
        """
        if self.voiture is not None:
            try:
                date_demande = datetime.now()
                rapport = f"Entretien demandé pour la voiture {self.voiture.immatriculation}."
                entretien = Entretien(date_demande, date_service, rapport)
                return entretien.effectuerEntretien()
            except ValueError:
                return "Format de date invalide. Utilisez le format 'AAAA-MM-JJ'."
        else:
            return "Aucune voiture associée pour effectuer l'entretien."

    def entrerParking(self, a) -> str:
        """
        Permet au client d'entrer dans un parking.

        Cette méthode permet au client d'entrer dans un parking, en fonction de certaines conditions d'accès.

        Args:
            a : Paramètre lié à l'accès au parking, probablement un objet ou un attribut.

        Returns:
            str : Un message indiquant si l'entrée dans le parking est autorisée ou non.
        """
        return a.lancerProcedureEntree(self)
