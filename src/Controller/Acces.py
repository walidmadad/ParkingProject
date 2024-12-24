from Model.Client import Client
from Model.Voiture import Voiture
from Model.Parking import Parking
from Controller.PanneauAffichage import PanneauAffichage
from Controller.BorneTicket import BorneTicket
from Controller.Teleporteur import Teleporteur

class Acces:
    """
    La classe Acces gère les interactions d'entrée pour un client dans un parking,
    telles que l'actionnement de la caméra, du panneau d'affichage, et le lancement
    de la procédure d'entrée du client.
    """

    def __init__(self, parking: Parking):
        self.parking = parking
        self.panneau = PanneauAffichage()
        self.borne_ticket = BorneTicket()
        self.teleporteur = Teleporteur()

    def actionnerCamera(self, c: Client) -> Voiture:
        """
        Actionne la caméra pour capturer des informations liées à la voiture du client.

        Args:
            c (Client) : Le client dont la voiture doit être capturée par la caméra.

        Returns:
            Voiture : L'objet Voiture associé au client, obtenu après l'actionnement de la caméra.
        """

        return c.voiture

    def actionnerPanneau(self) -> str:
        """
        Actionne le panneau d'affichage pour afficher des informations liées à l'entrée du client.

        Returns:
            str : Une chaîne de caractères représentant l'information affichée sur le panneau.
        """
        return self.panneau.afficherNbPlacesDisponibles(self.parking)

    def lancerProcedureEntree(self, client: Client) -> str:
        """
        Lance la procédure d'entrée du client dans le parking.

        Args:
            client : Le client qui entre dans le parking.

        Returns:
            str : Une chaîne de caractères indiquant le statut ou le résultat de la procédure d'entrée.
        """
        if client.voiture:
            txt = self.teleporteur.teleporterVoitureSuperAbonne(client.voiture, self.parking)
            return txt


        else:
            return f"Le client {client.nom} n'a pas de voiture associée pour l'entrée."
