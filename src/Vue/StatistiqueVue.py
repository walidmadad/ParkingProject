import tkinter as tk

from Controller.StatistiquesController import StatistiquesController
from Vue import Application


def afficherStats(frame, parking, client):

    # Effacer le contenu précédent
    clear_frame(frame)
    tk.Label(frame, text="Bienvenue dans les statistiques de DreamPark !", font=("Arial", 20)).pack(pady=20)
    tk.Label(frame, text=f"Voitures entrées dans le parking: {StatistiquesController(parking).recpuererStatsVoitures()}", font=("Arial", 16)).pack(pady=20)
    tk.Label(frame, text=f"Clients Super Abonnés : {StatistiquesController(parking).recpuererStatsClientSuperAbonnes()}", font=("Arial", 16)).pack(pady=20)
    tk.Label(frame, text=f"Clients Abonnés : {StatistiquesController(parking).recpuererStatsClientAbonnes()}", font=("Arial", 16)).pack(pady=20)
    tk.Label(frame, text=f"Nouveaux Abonnements : {StatistiquesController(parking).recpuererStatsNouveauxAbonnement()}", font=("Arial", 16)).pack(pady=20)
    tk.Label(frame, text=f"Clients Non Abonnés : {StatistiquesController(parking).recpuererStatsClientNonAbonnes()}", font=("Arial", 16)).pack(pady=20)

    next_button = tk.Button(frame, text=f"Menu", command=lambda: Application.afficherMenu(frame, parking, client))
    next_button.pack(pady=10)


def clear_frame(frame):
    """
    Efface tous les widgets d'un frame donné.
    """
    for widget in frame.winfo_children():
        widget.destroy()

