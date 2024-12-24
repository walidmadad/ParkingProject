from Controller.BorneTicket import BorneTicket
from Model.Voiture import Voiture
from Model.Place import Place
from Model.Placement import Placement
from Model.Parking import Parking
from datetime import date, timedelta


class Teleporteur:
    """
    La classe `Teleporteur` représente un service de gestion de placement pour téléporter des voitures
    vers des places spécifiques dans un parking. Elle gère à la fois les placements simples et ceux
    dédiés aux super abonnés.

    Responsabilités :
    - Vérifier et réserver une place libre pour une voiture.
    - Créer et gérer des objets de type `Placement` liés à des places dans un parking.
    - Manipuler des places dans le respect des règles de gestion du parking.
    """

    def teleporterVoiture(self, v: Voiture, p: Place) -> Placement:
        """
        Téléporte une voiture vers une place spécifique en créant un placement.

        Cette méthode s'assure que la place est libre avant d'effectuer l'opération. Elle crée ensuite
        un objet `Placement` et met à jour l'état de la place pour la marquer comme occupée.

        Args:
            v (Voiture): L'objet représentant la voiture à téléporter.
            p (Place): L'objet représentant la place cible où téléporter la voiture.

        Returns:
            Placement: Un objet `Placement` contenant les informations sur le stationnement.

        Raises:
            ValueError: Si la place spécifiée est déjà occupée ou si l'ajout du placement échoue.
        """
        if not p.estLibre:
            raise ValueError(f"La place {p.id_parking} est déjà occupée.")

        # Créer le placement
        dateDebut = date.today()
        dateFin = dateDebut + timedelta(days=1)
        placement = Placement(voiture=v, place=p, dateDebut=dateDebut, dateFin=dateFin, estEnCours=True)

        # Ajouter le placement à la place (avec gestion stricte)
        try:
            p.addPlacementP(placement)
            v.estDansParking = True
        except ValueError as e:
            raise ValueError(f"Erreur lors de l'ajout du placement : {str(e)}")

        # Marquer la place comme occupée uniquement après ajout réussi
        p.estLibre = False

        return placement

    def teleporterVoitureSuperAbonne(self, v: Voiture, parking: Parking) -> str:
        """
        Téléporte une voiture d'un super abonné vers une place disponible dans le parking.

        Cette méthode recherche automatiquement une place libre dans le parking correspondant
        aux besoins de la voiture et effectue la téléportation si une place est disponible.

        Args:
            v (Voiture): La voiture du super abonné à téléporter.
            parking (Parking): L'objet `Parking` où chercher une place.

        Returns:
            str: Un message indiquant le résultat de la téléportation. Ce message est de la forme :
                 - "La voiture a été téléportée avec succès à la place X."
                 - "Aucune place libre n'est disponible pour téléporter la voiture du super abonné."
        """
        # Recherche une place libre compatible
        place = parking.rechercherPlace(v)
        if place is not None:
            placement = self.teleporterVoiture(v, place)
            v.placement = placement
            parking.occuperPlace(place)
            return f"La voiture a été téléportée avec succès à la place {placement.place.id_parking}."

        # Aucun emplacement compatible trouvé
        return "Aucune place libre n'est disponible pour téléporter la voiture du super abonné."


    def recupererVoiture(self, v:Voiture, parking: Parking):
        place = v.placement.place
        parking.libererPlace(v.placement.place)
        v.placement.partirPlace()
        return "Voiture recuperer avec succes"

