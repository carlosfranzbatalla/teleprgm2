using System;

namespace Aparatos
{
    abstract class electrodomestico
    {
        private string marca;
        private string nroDeSerie;
        private float capacidad;
        private float potencia;
        private double precio;
        private string modoDeOperacion;
        public string Marca
        {
            get { return marca; }
            set { marca = value; }
        }
        public string NroDeSerie
        {
            get { return this.nroDeSerie; }
            set { this.nroDeSerie = value; }
        }
        public float Capacidad
        {
            get { return this.capacidad; }
            set { this.capacidad = value; }
        }
        public float Potencia
        {
            get { return this.potencia; }
            set { this.potencia = value; }
        }
        public double Precio
        {
            get { return precio; }
            set
            {
                if (value == 0) { precio = 10; }
                precio = value;
            }
        }
        public string ModoDeOperacion
        {
            get { return this.modoDeOperacion; }
            set { this.modoDeOperacion = value; }
        }

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
        //  Ejemplo de constructor no parametrizado
        public lavadora()
        {
            Console.WriteLine("Lavadora lista para iniciarse cuando lo indique");
        }

        // Ejemplo de constructor parametrizado
        public lavadora(DateTime vFechaActual)
        {
            if (vFechaActual.Hour > 7 && vFechaActual.Hour < 14)
            { this.ModoDeOperacion = "Normal"; }
            else
            { this.ModoDeOperacion = "Lento"; }
            Console.WriteLine("La lavadora esta lista para iniciarse y su modo de Operación será {0}", this.ModoDeOperacion);
        }

        public void lavar() { }
        public void centrifugar() { }
        public override string prender()
        {
            String vResult = "Se inicia encendido de la lavadora. Asegúrese de tener agua";
            return vResult;
        }
    }

    class telefono { }
    class vehiculo { }


}