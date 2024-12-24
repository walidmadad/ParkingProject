from Model.Contrat import Contrat

class Abonnement:
    """
    La classe Abonnement représente un abonnement à un service avec un libellé,
    un prix et une indication si l'abonnement comprend un pack garage.
    """

    def __init__(self, libelle: str, prix: float, estPackGar: bool):
        """
        Initialise un nouvel abonnement avec les informations suivantes.

        Args:
            libelle (str) : Le nom ou libellé de l'abonnement.
            prix (float) : Le prix de l'abonnement.
            estPackGar (bool) : Indique si l'abonnement inclut un pack garage (True ou False).
        """
        self.libelle = libelle
        self.prix = prix
        self.estPackGar = estPackGar
        self.mes_contrats = []

    def addContrat(self, contrat: Contrat):
        """
        Ajoute un contrat à cet abonnement.

        Args:
            contrat (Contrat) : L'objet Contrat à ajouter à l'abonnement.

        Returns:
            None
        """
        self.mes_contrats.append(contrat)
