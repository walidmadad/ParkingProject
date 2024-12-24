import tkinter as tk
from datetime import datetime

from Controller.BorneTicket import BorneTicket
from Controller.SeGarerController import SeGarerController
from Vue import Application


def seGarerMenu(frame, parking, client):
    """
    Affiche la vue pour se garer.
    """
    # Effacer le contenu précédent
    clear_frame(frame)

    seGarer = SeGarerController(client, parking)
    placeDispo = seGarer.afficherPlaceParking()

    tk.Label(frame, text="Bienvenue dans DreamPark !", font=("Arial", 20)).pack(pady=20)
    tk.Label(frame, text="Place Disponible : " + placeDispo, font=("Arial", 16)).pack(pady=20)

    # Contenu de la vue "Se Garer"
    tk.Label(frame, text=f"Bonjour {client.nom}", font=("Arial", 16)).pack(pady=20)
    tk.Label(frame, text=seGarer.afficherDonneesClient(), font=("Arial", 14)).pack(pady=10)


    next_button = tk.Button(frame, text="Suivant", command=lambda: teleportation(frame, parking, client))
    next_button.pack(pady=10)

def teleportation(frame, parking, client):
    seGarer = SeGarerController(client, parking)
    if client.estSuperAbonne:
        clear_frame(frame)
        tk.Label(frame, text=f"{client.nom}, vous êtes super abonnée", font=("Arial", 16)).pack(pady=20)
        tk.Label(frame, text=seGarer.se_garer(), font=("Arial", 14)).pack(pady=10)
        next_button = tk.Button(frame, text=f"Menu", command=lambda: Application.afficherMenu(frame, parking, client))
        next_button.pack(pady=10)

    elif client.estAbonne:
        clear_frame(frame)
        tk.Label(frame, text=f"{client.nom}, vous êtes abonnée", font=("Arial", 14)).pack(pady=10)
        tk.Label(frame, text=f"Veuillez choissir un servcie : ", font=("Arial", 14)).pack(pady=10)
        liste = tk.Listbox(frame)
        liste.insert(1, "1. Maintenance")
        liste.insert(2, "2. Entretien")
        liste.insert(3, "3. Livraison")
        liste.pack(pady=3)

        def valider_selection():
            selection = liste.curselection()
            if selection:  # Vérifie qu'une option est sélectionnée
                clear_frame(frame)
                index_selection = selection[0] + 1  # Récupère l'index de l'élément sélectionné
                if index_selection == 1 or index_selection == 2:
                    tk.Label(frame, text="Entrez la date du service (YYYY-MM-DD) :", font=("Arial", 14)).pack(pady=10)
                    date_service = tk.Entry(frame, font=("Arial", 14))
                    date_service.pack(pady=10)

                    next_button = tk.Button(frame, text="Suivant", command=lambda: suivant(date_service))
                    next_button.pack(pady=10)

                    def suivant(date_service):
                        date_str = date_service.get()
                        try:
                            date_service = datetime.strptime(date_str, "%Y-%m-%d").date()
                            tk.Label(frame, text=f"Date de service validée : {date_service}", font=("Arial", 14),
                                  fg="green").pack(pady=10)
                            BorneTicket.proposerServices(client, choix=index_selection, dateService=date_service)
                            clear_frame(frame)
                            tk.Label(frame, text=f"Félicitation {client.nom}", font=("Arial", 16)).pack(pady=10)
                            tk.Label(frame, text=seGarer.se_garer(), font=("Arial", 14)).pack(pady=10)
                            tk.Label(frame, text=f"Votre Ticket", font=("Arial", 16)).pack(pady=10)
                            tk.Label(frame, text=seGarer.recupererTicket(), font=("Arial", 14)).pack(pady=10)
                            next_button = tk.Button(frame, text=f"Menu",
                                                    command=lambda: Application.afficherMenu(frame, parking, client))
                            next_button.pack(pady=10)

                        except ValueError:
                            tk.Label(frame, text="Format de date invalide. Veuillez entrer une date au format YYYY-MM-DD.",
                                  font=("Arial", 12), fg="red").pack(pady=10)
                else:
                    tk.Label(frame, text="Entrez la date du livraison (YYYY-MM-DD) :", font=("Arial", 14)).pack(
                        pady=10)
                    date_livraison = tk.Entry(frame, font=("Arial", 14))
                    date_livraison.pack(pady=10)

                    tk.Label(frame, text="Entrez l'heure de livraison (HH:MM) :", font=("Arial", 14)).pack(
                        pady=10)
                    heure_livraison = tk.Entry(frame, font=("Arial", 14))
                    heure_livraison.pack(pady=10)

                    next_button = tk.Button(frame, text="Suivant", command=lambda: suivant(date_livraison, heure_livraison))
                    next_button.pack(pady=10)

                    def suivant(date_livraison, heure_livraison):
                        date_str = date_livraison.get()
                        try:
                            date_livraison = datetime.strptime(date_str, "%Y-%m-%d").date()
                            tk.Label(frame, text=f"Date de service validée : {date_livraison}", font=("Arial", 14),
                                     fg="green").pack(pady=10)
                            BorneTicket.proposerServices(client, choix=index_selection, dateLivraison=date_livraison, heureLivraison=heure_livraison)
                            clear_frame(frame)
                            tk.Label(frame, text=f"Félicitation {client.nom}", font=("Arial", 16)).pack(pady=10)
                            tk.Label(frame, text=seGarer.se_garer(), font=("Arial", 14)).pack(pady=10)
                            tk.Label(frame, text=f"Votre Ticket", font=("Arial", 16)).pack(pady=10)
                            tk.Label(frame, text=seGarer.recupererTicket(), font=("Arial", 14)).pack(pady=10)
                        except ValueError:
                            tk.Label(frame,
                                     text="Format de date invalide. Veuillez entrer une date au format YYYY-MM-DD.",
                                     font=("Arial", 12), fg="red").pack(pady=10)


            else:
                tk.Label(frame, text="Veuillez sélectionner une option.", font=("Arial", 14), fg="red").pack(pady=10)

        tk.Button(frame, text="Valider", command=valider_selection).pack(pady=10)
    else:
        clear_frame(frame)
        tk.Label(frame, text=f"{client.nom}, vous êtes non abonnée", font=("Arial", 14)).pack(pady=10)
        tk.Label(frame, text=f"Veuillez choissir votre Type de paiement: ", font=("Arial", 14)).pack(pady=10)
        listePaiement = tk.Listbox(frame)
        listePaiement.insert(1, "1. Carte Bancaire(Visa, MatserCard")
        listePaiement.insert(2, "2. Espéces")
        listePaiement.pack(pady=3)

        def valider_selection():
            selection = listePaiement.curselection()
            index_selection = selection[0] + 1  # Récupère l'index de l'élément sélectionné
            if index_selection == 1 or index_selection == 2:
                resultPaiement = BorneTicket.proposerTypePaiement(index_selection)
                next_button = tk.Button(frame, text="Suivant", command=lambda: suivant(resultPaiement))
                next_button.pack(pady=10)

                def suivant(resultPaiement):
                    clear_frame(frame)
                    tk.Label(frame, text=f"{client.nom}, vous êtes non abonnée", font=("Arial", 16)).pack(pady=10)
                    tk.Label(frame, text=resultPaiement, font=("Arial", 12)).pack(pady=10)

                    tk.Label(frame, text=f"Veuillez choissir une abonnement : ", font=("Arial", 14)).pack(pady=10)
                    liste = tk.Listbox(frame)
                    liste.insert(1, "1. Abonnement Standard : 100.0€ (sans pack garage)")
                    liste.insert(2, "2. Abonnement Premium : 150.0€ (avec pack garage)")
                    liste.insert(3, "3. Entrer sans abonnement")
                    liste.pack(pady=3)

                    def valider_selection1():
                        selection = liste.curselection()
                        index_selection = selection[0] + 1  # Récupère l'index de l'élément sélectionné
                        if index_selection == 1 or index_selection == 2 or index_selection == 3:
                            resultAbonnement = BorneTicket.proposerAbonnements(client,parking, index_selection)
                            next_button = tk.Button(frame, text="Suivant", command=lambda: suivant1(resultAbonnement))
                            next_button.pack(pady=10)

                            def suivant1(resultAbonnement):
                                clear_frame(frame)
                                tk.Label(frame, text=resultAbonnement, font=("Arial", 12)).pack(pady=10)
                                tk.Label(frame, text=f"Félicitation {client.nom}", font=("Arial", 16)).pack(pady=10)
                                tk.Label(frame, text=seGarer.se_garer(), font=("Arial", 14)).pack(pady=10)
                                tk.Label(frame, text=f"Votre Ticket", font=("Arial", 16)).pack(pady=10)
                                tk.Label(frame, text=seGarer.recupererTicket(), font=("Arial", 14)).pack(pady=10)
                                next_button = tk.Button(frame, text=f"Menu",
                                                        command=lambda: Application.afficherMenu(frame, parking, client))
                                next_button.pack(pady=10)
                        else :
                            tk.Label(frame,
                                     text="Choix Invalide",
                                     font=("Arial", 12), fg="red").pack(pady=10)

                    next_button = tk.Button(frame, text="Valider", command=valider_selection1)
                    next_button.pack(pady=10)



            else :
                tk.Label(frame,
                         text="Choix Invalide",
                         font=("Arial", 12), fg="red").pack(pady=10)

        tk.Button(frame, text="Valider", command=valider_selection).pack(pady=10)


def clear_frame(frame):
    """
    Efface tous les widgets d'un frame donné.
    """
    for widget in frame.winfo_children():
        widget.destroy()
