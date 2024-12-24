import tkinter as tk
from Vue import SeGarerVue
from Vue import ReprendreVoitureVue
from Vue import StatistiqueVue

def afficherMenu(frame, parking, client):
    """
    Affiche le menu principal dans le frame donné.
    """
    # Effacer le contenu précédent
    clear_frame(frame)

    # Contenu du menu principal
    tk.Label(frame, text="Bienvenue dans DreamPark !", font=("Arial", 20)).pack(pady=20)
    park_button = tk.Button(
        frame,
        text="Se Garer",
        command=lambda: SeGarerVue.seGarerMenu(frame, parking, client),
        font=("Arial", 14)
    )
    park_button.pack(pady=10)

    retrieve_button = tk.Button(frame, text="Reprendre Voiture", command=lambda : ReprendreVoitureVue.reprise_voiture(frame, parking, client), font=("Arial", 14))
    retrieve_button.pack(pady=10)

    statistics_button = tk.Button(frame, text="voir les statistiques", command=lambda : StatistiqueVue.afficherStats(frame, parking, client), font=("Arial", 14))
    statistics_button.pack(pady=10)

def clear_frame(frame):
    """
    Efface tous les widgets d'un frame donné.
    """
    for widget in frame.winfo_children():
        widget.destroy()
