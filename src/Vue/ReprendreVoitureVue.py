import tkinter as tk

from Controller.ReprendreVoitureControlleur import ReprendreVoitureController
from Vue import Application


def reprise_voiture(frame, parking, client):

    # Effacer le contenu précédent
    clear_frame(frame)
    tk.Label(frame, text="Bienvenue dans DreamPark !", font=("Arial", 20)).pack(pady=20)
    tk.Label(frame, text=f"Bonjour {client.nom}", font=("Arial", 16)).pack(pady=20)

    next_button = tk.Button(frame, text=f"Recuperer ma voiture {client.voiture.immatriculation}", command=lambda: recupererVoiture(frame, parking, client))
    next_button.pack(pady=10)

def recupererVoiture(frame, parking, client):
    reprendreVoiture = ReprendreVoitureController(client, parking)
    tk.Label(frame, text=reprendreVoiture.reprendre_voiture(), font=("Arial", 16)).pack(pady=20)
    next_button = tk.Button(frame, text=f"Menu", command=lambda: Application.afficherMenu(frame, parking, client))
    next_button.pack(pady=10)


def clear_frame(frame):
    """
    Efface tous les widgets d'un frame donné.
    """
    for widget in frame.winfo_children():
        widget.destroy()

