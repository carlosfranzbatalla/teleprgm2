#!/usr/bin/python3

class vistaAxiomasPorTerminal:
    def mostrar(self, vAxioma):
        print("y el axioma es: ", vAxioma)

    def escojeAxioma(self):
        vResult = None
        vResult = input("Tipee el nro. de axioma que quiere ver: ")
        return vResult


class vistaAxiomasHTML:
    def mostrar(self, vAxioma):
        vArchivoHtml = open('vistaMVC.html', 'w')

        vPlantilla = """
        <html>
        <head>
        <title> Telematica - Prog2 </title>
        </head>
        <body> 
        <h1>Modelo-Vista-Controlador (MVC)</h1>
        <h2>Vista html</h2>
        <table border="1">
        <tbody>
        <tr>
        <td>y el Axioma es: </td>
        </tr>
        <tr>
        <td>        
        """
        vPlantilla += vAxioma
        vPlantilla += """
        </td>
        </tr>
        </tbody>
        </table>
        </body>
        </html>
        """

        vArchivoHtml.write(vPlantilla)
        vArchivoHtml.close()

    def escojeAxioma(self):
        vResult = None
        vResult = input("Tipee el nro. de axioma que quiere ver: ")
        return vResult
