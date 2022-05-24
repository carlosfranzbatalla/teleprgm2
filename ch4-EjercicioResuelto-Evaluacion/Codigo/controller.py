#!/usr/bin/python3
import modelo
import vista


class terminalController:

    def __init__(self):
        self.view = vista.display()
        self.__tipoDeEmpleado = self.view.EscojeTipoEmpleado()
        # NOTA
        # el tema aqui, es que controller decide que clase instanciar, esta eso bien??
        # si, por que almacenista, chofer, contador estan en clases separadas
        if (self.__tipoDeEmpleado == '1'):
            self.model = modelo.Almacenista(
                self.view.EscojeEmpleado(), self.__tipoDeEmpleado)
        elif (self.__tipoDeEmpleado == '2'):
            self.model = modelo.chofer(
                self.view.EscojeEmpleado(), self.__tipoDeEmpleado)

    def run(self):        
        self.view.MuestraDatosDelEmpleado(list(self.model.__dict__.values()))
        vSalario = self.model.DeterminarSalario()
        print (vSalario)