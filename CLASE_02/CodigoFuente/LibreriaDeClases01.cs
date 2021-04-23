using System;

namespace Aparatos
{
    abstract class electrodomestico
    {
        //declaracion de datos de la clase
        string marca;
        private string nroDeSerie;
        private float capacidad;
        private float potencia;
        private double precio;

        // Funciones de acceso
        // a los datos de la clase
        public string Marca
        {
            get { return marca; }
            set { marca = value; }
        }
        //ponemos validacion que no permite
        //colocar el precio igual a 0.

        public double Precio
        {
            get { return precio; }
            set
            {
                if (value == 0) { precio = 10; }
                precio = value;
            }
        }

        //métodos de la clase
        public virtual string prender()
        {
            String vResult = "Se inicia encendido de este aparato";
            return vResult;
        }
        public void apagar()
        {
            Console.WriteLine("Se inicia apagado de este aparato");
        }
    }
    class lavadora : electrodomestico
    {
        public void lavar() { }
        public void centrifugar() { }

        public override string prender()
        {
            String vResult = "Se inicia encendido de la lavadora. Asegurese de tener agua";
            return vResult;
        }

    }
    class telefono { }
    class vehiculo { }


}