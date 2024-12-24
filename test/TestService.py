import unittest
from datetime import datetime
from src.Model.Service import Service

class TestService(unittest.TestCase):
    """
    Classe de test pour la classe `Service`.

    Cette classe contient des tests unitaires pour vérifier la création d'un service et les méthodes associées.
    """

    def test_creation_service(self):
        """
        Teste la création d'un service avec des dates de demande, de service et un rapport initial.
        """
        date_demande = datetime(2024, 12, 15, 14, 30)
        date_service = datetime(2024, 12, 16, 10, 0)
        rapport = "Révision complète effectuée."

        service = Service(dateDemande=date_demande, dateService=date_service, rapport=rapport)

        # Vérifie que les attributs sont correctement initialisés
        self.assertEqual(service.dateDemande, date_demande)
        self.assertEqual(service.dateService, date_service)
        self.assertEqual(service.rapport, rapport)

    def test_effectuer_service_non_implemente(self):
        """
        Teste que la méthode `effectuer_service` lève une NotImplementedError.
        """
        date_demande = datetime(2024, 12, 15, 14, 30)
        date_service = datetime(2024, 12, 16, 10, 0)
        rapport = "Service en attente."

        service = Service(dateDemande=date_demande, dateService=date_service, rapport=rapport)

        with self.assertRaises(NotImplementedError):
            service.effectuer_service()

if __name__ == '__main__':
    """
    Exécute les tests unitaires lorsque le script est exécuté directement.
    """
    unittest.main()
