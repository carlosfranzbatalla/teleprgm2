#!/usr/bin/python3

# esto es una estructura de datos llamada lista. nom vLista=[1,32,3]
vAxiomas = ["Entre tres puntos, solo pasa una línea recta", "Una proposición no puede ser verdadera y falsa al mismo tiempo", "Si dos números naturales tienen el mismo sucesor, esos dos números son el mismo número.",
            "Todas las rectas tienen una cantidad infinita de puntos.", "Dos rectas paralelas nunca se tocan", "Dos líneas rectas nunca encierran algo."]


class axiomaModel:
    def obtenerAxioma(self, vNroEscogido):
        vResult = vAxiomas[vNroEscogido]
        return vResult
