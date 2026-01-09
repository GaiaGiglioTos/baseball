import itertools

import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self._grafo = nx.Graph()
        self._idMap = {}

    def build_graph(self, y):
        self._grafo.clear()
        self._idMap.clear()
        squadre = DAO.getSquadreAnno(y)
        self._grafo.add_nodes_from(squadre)
        for s in squadre:
            self._idMap[s.ID] = s

        salari = DAO.getSalari(y,self._idMap)
        for s1, s2 in itertools.combinations(squadre, 2):
            peso = salari[s1] + salari[s2]
            self._grafo.add_edge(s1, s2, weight=peso)

    def getNumNodi(self):
        return self._grafo.number_of_nodes()

    def getNumArchi(self):
        return self._grafo.number_of_edges()

    def getAnni(self):
        return DAO.getAnni()

    def getSquadreAnno(self, y):
        return DAO.getSquadreAnno(y)

    def getNeighbors(self, n):
        vicini = self._grafo.neighbors(n)
        vic = {}
        for v in vicini:
            vic[v] = self._grafo[n][v]["weight"]
        sorted_vic = sorted(vic.items(), key=lambda item: item[1], reverse=True)

        return sorted_vic
