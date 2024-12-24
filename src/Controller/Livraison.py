from Model.Service import Service
from datetime import datetime

class Livraison(Service):
    """
    La classe Livraison hérite de la classe Service et représente une opération de livraison.

    Elle permet d'effectuer une livraison en utilisant les informations héritées de la classe Service.
    """
    def __init__(self, date_demande: datetime, date_service: datetime, rapport: str):
        super().__init__(date_demande, date_service, rapport)

    def effectuerLivraison(self):
        """
        Effectue la livraison.

        Cette méthode effectue l'opération de livraison. La logique exacte de la livraison n'est pas encore définie (méthode vide).

        """
        return "Livraison effectuée."
