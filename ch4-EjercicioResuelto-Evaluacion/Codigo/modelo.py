#!/usr/bin/python3
import datetime
from abc import (ABC, abstractmethod)

vDiccionarioTiposDeEmpleados = {
    1: 'almacenista', 2: 'chofer', 3: 'contador'
}

vAlmacenDeDatos = {
    'empleado': {
        'almacenista': [
            {
                "ci": "20111222", "nombre": "Truman", "apellido": "Capote", "salario": 7, "fechaDeNacimiento": datetime.datetime(2012, 12, 20, 0, 0), "fechaDeIngreso": datetime.datetime(2012, 12, 20, 0, 0)},
            {
                "ci": "20333444", "nombre": "Albert", "apellido": "Camus", "salario": 4, "fechaDeNacimiento": datetime.datetime(2012, 12, 20, 0, 0), "fechaDeIngreso": datetime.datetime(2012, 12, 20, 0, 0)}],
        'chofer': [
            {
                "ci": "20555666", "nombre": "Gustav", "apellido": "Flaubert", "salario": 3, "fechaDeNacimiento": datetime.datetime(2012, 12, 20, 0, 0), "fechaDeIngreso": datetime.datetime(2012, 12, 20, 0, 0)},
            {
                "ci": "20777888", "nombre": "Emile", "apellido": "Cioran", "salario": 4, "fechaDeNacimiento": datetime.datetime(2012, 12, 20, 0, 0), "fechaDeIngreso": datetime.datetime(2012, 12, 20, 0, 0)}]
    }
}


class Empleado(ABC):  # Super Clase o Clase Base
    __salario = 0
    nombre = None
    apellido = None
    fechaDeNacimiento = None
    vFechaDeIngreso = None
    vEmailPersonal = None
    vEmailCorporativo = None
    vCargo = None
    vDepartamento = None

    def __init__(self, vCedula, vTipoDeEmpleado):  # constructor de la superclase
        self.cedulaDeIdentidad = vCedula
        self.__tipoDeEmpleado = vTipoDeEmpleado
        vDatosDelEmpleado = self.extraeDatosDelEmpleado(
            vCedula, vTipoDeEmpleado)
        if vDatosDelEmpleado != []:
            self.nombre = vDatosDelEmpleado[1]
            self.apellido = vDatosDelEmpleado[2]
            self.__salario = vDatosDelEmpleado[3]
            self.fechaDeNacimiento = vDatosDelEmpleado[4]
        else:            
            self.nombre = self.apellido = self.__salario = self.fechaDeNacimiento = "Empleado no encontrado"

    def extraeDatosDelEmpleado(self, cedulaDeIdentidad, vTipoDeEmpleado):
        vResult = []
        vAlmacenistas = vAlmacenDeDatos['empleado'][vDiccionarioTiposDeEmpleados[int(
            vTipoDeEmpleado)]]
        for vIndex in vAlmacenistas:
            if vIndex.get('ci') == cedulaDeIdentidad:
                vResult = list(vIndex.values())
            else:
                pass
        return vResult

    

    def asignarElSalario(self, vSalario):  
        vResult = None
        vResult = "no puede pagar 0 a un empleado" if vSalario <= 0 else "Salario asignado correctamente"
        return vResult

    def aumentarSalario(self, vAumento):
        pass

    def agregaHorasExtras(self):
        pass


class Almacenista(Empleado):
    vCodigoDeProducto = None

    def chekaStock(self, vCodigoDeProducto):
        pass

    def preparaPedido(self):
        pass

    def recibeLotedeProducto(self, vCodigoDeProducto):
        pass


class Contador(Empleado):
    def registraEgresosPorSalarios(self):
        pass

    def pagaServiciosBasicos(self):
        pass

    def registraIngresosPorServiciosRealizados(self):
        pass

    def registraEnElLibroDiario(self):
        pass

    def llevaCajaChica(self):
        pass


class Chofer(Empleado):
    vNumeroDeLicencia = ""

    def asignarVehiculo(self):
        pass

    def calculaKilometrosRecorridos(self, vPeriodo):
        vResult = 0
        return vResult

    def asignarRuta(self, vDireccion):
        pass

    def aumentarSalario(self, vAumento):  
        __bonoChoferes = 10
        vAumento += __bonoChoferes
        self.__salario += vAumento
