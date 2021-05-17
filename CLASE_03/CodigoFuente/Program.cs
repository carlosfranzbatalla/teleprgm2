using System;
using Aparatos;

namespace claseOOP
{
    class Program
    {
        static void Main(string[] args)
        {
            DateTime vAhora = DateTime.Now;
            lavadora oLavadora1 = new lavadora();
            lavadora oLavadora2 = new lavadora(vAhora);
            Console.WriteLine(oLavadora2.prender());
            Console.ReadKey();
        }
    }
}
