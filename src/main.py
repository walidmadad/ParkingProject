from tkinter import Frame, Tk

from Controller.SeGarerController import SeGarerController
from Controller.StatistiquesController import StatistiquesController
from Model.Client import Client
from Model.Parking import Parking
from Model.Voiture import Voiture
from Vue import Application

parking = Parking(25, 3, 10, 3)

# Création d'une voiture et de plusieurs clients
voiture1 = Voiture("ABC-123", 3.5, 3.9, False)
voiture2 = Voiture("EFG-2351", 2.5, 3.3, False)
voiture3 = Voiture("FR-18823", 1.5, 2.9, False)

client1 = Client("Alice", "Rue des Lilas", True, True, 5, voiture1)  # Super abonné
client2 = Client("Bob", "Rue des Fleurs", True, False, 3, voiture2)  # Abonné
client3 = Client("Charlie", "Rue des Vignes", False, False, 1, voiture3)  # Non abonné

SeGarerController(client1, parking).se_garer()
SeGarerController(client1, parking).se_garer()
SeGarerController(client1, parking).se_garer()

root = Tk()
root.title("DreamPark")
root.geometry("650x500")

frame = Frame(root)
frame.pack(expand=True, fill="both")

# Affichage du menu
Application.afficherMenu(frame, parking, client3)

root.mainloop()
