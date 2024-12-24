from Model.Service import Service
from datetime import datetime

class Entretien(Service):
    """
    La classe Entretien hérite de la classe Service et représente une opération d'entretien.

    Elle permet d'effectuer un entretien en utilisant les informations héritées de la classe Service.
    """
    def __init__(self, date_demande: datetime, date_service: datetime, rapport: str):
        super().__init__(date_demande, date_service, rapport)

    def effectuerEntretien(self):
        """
        Effectue l'entretien.

        Cette méthode effectue l'opération d'entretien. La logique exacte de l'entretien n'est pas encore définie (méthode vide).


        """
        return "Entretien effectué."
