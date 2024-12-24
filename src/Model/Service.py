from datetime import date
from datetime import datetime
class Service:
    """
    La classe Service représente un service avec une demande et une date de service, ainsi qu'un rapport associé.

    Attributs :
        dateDemande (date) : La date à laquelle la demande de service a été faite.
        dateService (date) : La date à laquelle le service a été effectué.
        rapport (str) : Un rapport décrivant le service effectué.
    """

    def __init__(self, dateDemande: datetime, dateService: datetime, rapport: str):
        """
        Initialise un nouveau service avec les informations spécifiées.

        Args:
            dateDemande (date) : La date de la demande de service.
            dateService (date) : La date à laquelle le service a été réalisé.
            rapport (str) : Le rapport décrivant le service effectué.
        """
        self.dateDemande = dateDemande
        self.dateService = dateService
        self.rapport = rapport

    def effectuer_service(self):
        raise NotImplementedError("Cette méthode doit être implémentée par les sous-classes.")
