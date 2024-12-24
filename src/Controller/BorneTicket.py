import uuid

from Model.Abonnement import Abonnement
from Model.Client import Client
from Model.Parking import Parking
from datetime import datetime

class BorneTicket:
    """
    La classe BorneTicket représente une borne de ticket dans un parking.
    Elle permet de délivrer des tickets, proposer des services et abonnements,
    récupérer des informations de carte et suggérer des types de paiement.
    """

    def deliverTicket(self, c: Client) -> str:
        """
        Délivre un ticket au client à l'entrée du parking.

        Args:
            c (Client): Le client à qui délivrer un ticket.

        Returns:
            str: Le ticket délivré au client.
        """
        # Générer un numéro de ticket unique avec uuid
        ticket_id = str(uuid.uuid4())  # Un identifiant unique pour le ticket

        # Obtenir la date et l'heure de délivrance
        now = datetime.now()
        date_heure = now.strftime("%Y-%m-%d %H:%M:%S")

        # Créer un message de ticket avec les informations du client et la date d'entrée
        ticket_message = (
            f"Ticket délivré pour {c.nom}.\n"
            f"Numéro de ticket: {ticket_id}\n"
            f"Date et heure d'entrée: {date_heure}\n"
            f"Nom du client: {c.nom}\n"
            f"Adresse: {c.adresse}\n"
        )

        # Retourner le message du ticket
        return ticket_message

    def proposerServices(c: Client, choix,dateService = None, dateLivraison=None, heureLivraison=None) -> str:
        """
        Propose des services au client selon son statut.

        Args:
            c (Client): Le client pour qui proposer des services.

        Returns:
            str: Les services proposés au client.
        """

        if choix == 1:
            return c.demanderMaintenance(dateService)
        elif choix == 2:
            return c.demanderEntretien(dateService)
        elif choix == 3:
            return c.demanderLivraison(dateLivraison, heureLivraison, c.adresse)
        else:
            return "Choix invalide, aucun service n'a été sélectionné."

    def proposerAbonnements(c: Client,p: Parking, choix) -> str:
        """
        Propose des abonnements au client en fonction du parking et permet de choisir un abonnement
        par numéro.

        Args:
            c (Client) : Le client à qui proposer un abonnement.
            p (Parking) : Le parking où proposer l'abonnement.

        Returns:
            str : Le message retourné avec l'abonnement sélectionné par le client.
        """

        # Liste des abonnements disponibles dans le parking
        abonnements_disponibles = [
            Abonnement("Abonnement Standard", 100.0, False),  # Abonnement sans pack garage
            Abonnement("Abonnement Premium", 150.0, True),  # Abonnement avec pack garage
        ]

        # Gérer la sélection
        if choix == 1:
            # Le client choisit l'abonnement Standard
            c.sAbonner(abonnements_disponibles[0])
            p.addAbonnement(abonnements_disponibles[0])
            return "Vous avez choisi l'abonnement Standard pour 100.0€."

        elif choix == 2:
            # Le client choisit l'abonnement Premium
            c.sAbonner(abonnements_disponibles[1])
            p.addAbonnement(abonnements_disponibles[1])
            return "Vous avez choisi l'abonnement Premium pour 150.0€."

        elif choix == 3:
            # Le client choisit d'entrer sans abonnement
            p.nbClientNonAbonnes += 1
            return "Vous avez choisi d'entrer sans abonnement."

    def recupererInfosCarte(self, c: Client) -> str:
        """
        Récupère les informations de la carte du client.

        Args:
            c (Client) : Le client dont les informations de carte sont récupérées.

        Returns:
            str : Les informations de la carte du client.
        """
        return (f"Informations de la carte du client {c.nom} :"
                f"Nom: {c.nom}"
                f"Adresse: { c.adresse}"
                f"Abonne: {"oui" if c.estAbonne else "non"}"
                f"Super abonne: {"oui" if c.estSuperAbonne else "non"}"
                f"N° Frequentations: {c.nbrFrequentations}"
                f"Abonnement: {c.mon_abonnement}"
                f"Immatricule: {c.voiture.immatriculation}"
                f"Hauteur: {c.voiture.hauteur}"
                f"Longueur: {c.voiture.longueur}")

    def proposerTypePaiement(choix) -> str:
        """
        Propose un type de paiement pour le ticket ou les services.

        Returns:
            str: Le type de paiement proposé (ex. carte bancaire, espèces, etc.).
        """
        # Liste des méthodes de paiement possibles
        types_de_paiement = [
            "Carte bancaire",
            "Espèces",
        ]


        if choix == 1:
            return f"Vous avez choisi de payer par Carte Bancaire."
        elif choix == 2:
            return f"Vous avez choisi de payer en Espéces."

