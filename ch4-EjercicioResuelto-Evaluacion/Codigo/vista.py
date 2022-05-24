#!/usr/bin/python3
from __future__ import print_function
from colorclass import Color
from terminaltables import SingleTable


class display:    

    def EscojeTipoEmpleado(self):
        vResult = None
        vResult = input("seleccione el tipo de empleado:")
        return vResult

    def EscojeEmpleado(self):
        vResult = None
        vResult = input("Tipee el nro. de cédula del empleado: ")
        return vResult

    def MuestraDatosDelEmpleado(self, vEmpleado):        
        vData = [
            [Color('Cédula'), Color('{autocyan}Nombre{/autocyan}'), Color(
                '{autocyan}Apellido{/autocyan}'), Color('Salario'), Color('F. Nac')],
            [vEmpleado[0], vEmpleado[2], vEmpleado[3], vEmpleado[4], vEmpleado[5]]
        ]

        vResult = SingleTable(vData, ' '+' '.join(vEmpleado[2:4])+' ')
        vResult.inner_heading_row_border = False
        vResult.inner_row_border = True

        vResult.justify_columns = {0: 'center', 1: 'center', 2: 'center'}
        print(vResult.table)


