using System;
using Aparatos;

namespace claseOOP
{
    class Program
    {
        static void Main(string[] args)
        {
            lavadora oLavadora = new lavadora();
            Console.WriteLine(oLavadora.prender());
        }
    }
}
