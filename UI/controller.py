import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handleCreaGrafo(self, e):
        y = self._view._ddAnno.value
        self._model.build_graph(y)
        self._view._txt_result.controls.append(ft.Text(f"Grafo creato con {self._model.getNumNodi()} nodi e {self._model.getNumArchi()} archi"))
        self._view.update_page()

    def handleDettagli(self, e):
        n = self._model._idMap[int(self._view._ddSquadra.value)]
        vic = self._model.getNeighbors(n)
        for v,p in vic:
            self._view._txt_result.controls.append(ft.Text(f"{v.teamCode} ({v.name}) --> {p}"))
        self._view.update_page()

    def handlePercorso(self, e):
        pass

    def fillddAnno(self):
        anni = self._model.getAnni()
        for a in anni:
            self._view._ddAnno.options.append(ft.dropdown.Option(a))

        self._view.update_page()


    def handle_squadre(self,e):
        self._view._txtOutSquadre.controls.clear()
        self._view._ddSquadra.options.clear()
        y = self._view._ddAnno.value
        squadre = self._model.getSquadreAnno(y)
        self._view._txtOutSquadre.controls.append(ft.Text(f"Squadre presenti nell'anno {y} = {len(squadre)}"))
        for s in squadre:
            self._view._txtOutSquadre.controls.append(ft.Text(s))
            self._view._ddSquadra.options.append(ft.dropdown.Option(text=f"{s}", key = s.ID))

        self._view.update_page()



