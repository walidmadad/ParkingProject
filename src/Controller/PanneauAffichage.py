from Model.Parking import Parking

class PanneauAffichage:
    """
    La classe `PanneauAffichage` représente un panneau d'affichage utilisé pour afficher
    des informations relatives au nombre de places disponibles dans un parking.

    Attributs :
        Aucun attribut n'est défini pour cette classe, car elle agit comme un service
        pour fournir des informations sur le parking.
    """

    def afficherNbPlacesDisponibles(self, p: Parking) -> str:
        """
        Affiche le nombre de places disponibles dans un parking donné.

        Cette méthode analyse les places disponibles dans le parking fourni et génère une
        chaîne de caractères indiquant le nombre total de places libres.

        Args:
            p (Parking): Une instance de la classe `Parking` contenant les informations sur les places.

        Returns:
            str: Une chaîne indiquant le nombre de places disponibles, au format :
                 "Il y a X places disponibles dans ce parking."
        """
        # Compter le nombre de places libres dans le parking
        places_disponibles = sum(1 for place in p.mes_places if place.estLibre)

        # Retourner le résultat sous forme de chaîne de caractères
        return f"Il y a {places_disponibles} places disponibles dans ce parking."
