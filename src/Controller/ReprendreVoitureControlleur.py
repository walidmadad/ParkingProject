from Controller.Teleporteur import Teleporteur
from Model.Parking import Parking
from Model.Client import Client


class ReprendreVoitureController:
    """
    Le contrôleur `ReprendreVoitureController` gère le processus de reprise d'une voiture
    en interagissant avec les composants du modèle, du contrôleur et de la vue.

    Attributs :
        client (Client) : Le client qui souhaite récupérer sa voiture.
        parking (Parking) : L'instance du parking géré par ce contrôleur.
        teleporteur (Teleporteur) : Le gestionnaire des téléporteurs pour déplacer les voitures.
        vue (ReprendreVoitureVue) : La vue pour interagir avec l'utilisateur.
    """

    def __init__(self, client: Client, parking: Parking):
        """
        Initialise une nouvelle instance de ReprendreVoitureController.

        Args:
            client (Client): Le client qui interagit avec le système pour reprendre sa voiture.
        """
        self.client = client
        self.parking = parking
        self.teleporteur = Teleporteur()  # Instance du teleporteur pour déplacer la voiture

    def reprendre_voiture(self):
        """
        Gère le processus de reprise de voiture pour un client.

        Étapes :
        1. Vérifier si la voiture du client est présente dans le parking.
        2. Si oui, utiliser le téléporteur pour la ramener au client.
        3. Mettre à jour le parking pour libérer la place.
        4. Notifier le client de la réussite de l'opération.
        """
        # Rechercher la voiture du client dans le parking
        voiture = self.client.voiture
        estDansParking = voiture.estDansParking
        if voiture.estDansParking:
            # Utiliser le téléporteur pour déplacer la voiture
            teleporteur = Teleporteur()
            message = teleporteur.recupererVoiture(voiture, self.parking)
            return message
