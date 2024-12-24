from datetime import datetime

from Model.Service import Service
from Model.Voiture import Voiture

class Maintenance(Service):
    """
    La classe Maintenance hérite de la classe Service et représente une opération de maintenance effectuée sur une voiture.

    Elle permet d'effectuer une maintenance sur une voiture en utilisant les informations héritées de la classe Service.
    """

    def __init__(self, date_demande: datetime, date_service: datetime, rapport: str):
        super().__init__(date_demande, date_service, rapport)

    def effectuerMaintenance(self, v: Voiture):
        """
        Effectue la maintenance sur une voiture donnée.

        Cette méthode prend un objet Voiture en entrée et effectue la maintenance sur cette voiture. La logique exacte de la maintenance n'est pas encore définie (méthode vide).

        Args:
            v (Voiture) : L'objet Voiture sur lequel la maintenance doit être effectuée.

        """
        return f"Effectuer maintenance sur la voiture : {v.immatriculation}"
