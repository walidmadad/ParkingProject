from Controller.Acces import Acces
from Controller.BorneTicket import BorneTicket
from Controller.PanneauAffichage import PanneauAffichage
from Model.Client import Client
from Model.Parking import Parking


class SeGarerController:
    """
    Le contrôleur `SeGarerController` gère le processus de stationnement en interagissant avec
    les composants du modèle, du contrôleur et de la vue.

    Attributs :
        client (Client) : Le client qui souhaite se garer.
        parking (Parking) : L'instance du parking géré par ce contrôleur.
        acces (Acces) : Le gestionnaire des accès au parking.
        panneauAffichage (PanneauAffichage) : Le panneau d'affichage des places disponibles.
        borne_ticket (BorneTicket) : La borne qui gère les tickets et services associés.
        vue (SeGarerVue) : La vue pour interagir avec l'utilisateur.
    """

    def __init__(self, client: Client, parking: Parking):
        """
        Initialise une nouvelle instance de SeGarerController.

        Args:
            client (Client): Le client qui interagit avec le système de stationnement.
        """
        self.client = client
        self.parking = parking
        self.acces = Acces(self.parking)
        self.panneauAffichage = PanneauAffichage()
        self.borne_ticket = BorneTicket()

    def se_garer(self):
        """
        Simule le processus de stationnement pour un client.

        Étapes :
        1. Affiche un message de bienvenue au client.
        2. Affiche les places disponibles dans le parking.
        3. Traite le stationnement selon le statut du client :
           - Super Abonné : Procède à l'entrée immédiate.
           - Abonné : Propose des services et délivre un ticket.
           - Non Abonné : Propose des options de paiement et d'abonnement, puis délivre un ticket.

        Affiche les résultats des actions à chaque étape à travers la vue.
        """

        # Vérification du statut du client et traitement en fonction
        if self.client.estSuperAbonne:
            self.parking.nbClientSuperAbonnes += 1
            return self.client.entrerParking(Acces(self.parking))
        elif self.client.estAbonne:
            self.parking.nbClientAbonnes += 1
            return self.client.entrerParking(Acces(self.parking))
        else:
            return self.client.entrerParking(Acces(self.parking))

    def recupererTicket(self):
        return self.borne_ticket.deliverTicket(self.client)
    def afficherPlaceParking(self):
        places_disponibles = self.panneauAffichage.afficherNbPlacesDisponibles(self.parking)
        return places_disponibles
    def afficherDonneesClient(self):
        donnee = f"Votre adresse: {self.client.adresse}\n"

        if self.client.estSuperAbonne:
            donnee += "Vous êtes Super Abonnée\n"
        elif self.client.estAbonne:
            donnee += "Vous êtes Abonnée\n"
        else:
            donnee += "Vous êtes pas abonnée\n"

        donnee += (f"Données de Votre Véhicule: \n"
                   f"Immatriculation: {self.client.voiture.immatriculation}\n"
                   f"Hauteur: {self.client.voiture.hauteur}\n"
                   f"Longueur: {self.client.voiture.longueur}\n")

        return donnee


