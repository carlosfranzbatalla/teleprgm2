#!/usr/bin/python3
import modelo
import vista


class axiomaTerminalController:
    def __init__(self):
        self.model = modelo.axiomaModel()
        # self.view = vista.vistaAxiomasPorTerminal()
        self.view = vista.vistaAxiomasHTML()

    def run(self):
        vNroDeAxiomaEscogido = int(self.view.escojeAxioma())
        vAxioma = self.model.obtenerAxioma(vNroDeAxiomaEscogido)
        self.view.mostrar(vAxioma)
