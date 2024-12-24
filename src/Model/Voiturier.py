from Controller.Livraison import Livraison
from Model.Voiture import Voiture
from datetime import date

class Voiturier:
    """
    La classe Voiturier représente un voiturier qui est responsable de la livraison des voitures.

    Attributs :
        numVoiturier (int) : Numéro unique identifiant le voiturier.
    """

    def __init__(self, numVoiturier: int):
        """
        Initialise un nouveau voiturier avec un numéro unique.

        Args:
            numVoiturier (int) : Le numéro unique du voiturier.
        """
        self.numVoiturier = numVoiturier

    def livrerVoiture(self, v: Voiture, date_livraison: date, heure: int):
        """
        Livre une voiture à une date et une heure spécifiées.

        Args:
            v (Voiture) : L'objet Voiture représentant la voiture à livrer.
            date_livraison (date) : La date à laquelle la voiture doit être livrée.
            heure (int) : L'heure de livraison de la voiture (format 24h).

        """

