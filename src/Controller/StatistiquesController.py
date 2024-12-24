class StatistiquesController:

    def __init__(self, parking):
        self.parking = parking

    def recpuererStatsVoitures(self):
        return self.parking.nbVoituresStatistiques

    def recpuererStatsClientNonAbonnes(self):
        return self.parking.nbClientNonAbonnes

    def recpuererStatsClientAbonnes(self):
        return self.parking.nbClientAbonnes

    def recpuererStatsNouveauxAbonnement(self):
        return self.parking.nbNouveauAbonnement

    def recpuererStatsClientSuperAbonnes(self):
        return self.parking.nbClientSuperAbonnes

