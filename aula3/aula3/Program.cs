using System;
using System.Collections.Generic;
using System.Linq;
using System.Runtime.CompilerServices;
using System.Text;
using System.Threading.Tasks;

namespace aula3
{
    public class Programa
    {
        public static void Main(string[] args)
        {

            // criando nome

            Console.WriteLine("Digite seu nome: ");
            string nome_usuario = Console.ReadLine();

            //criando sobrenome

            Console.WriteLine("Digite seu sobrenome: ");
            string sobrenome_usuario = Console.ReadLine();

            //criando idade

            Console.WriteLine("Digite sua idade: ");
            string idade_texto = Console.ReadLine();
            int idade_usuario = int.Parse(idade_texto);
            //mudando nome
            Console.WriteLine("Digite um novo nome");
            nome_usuario = Console.ReadLine();
            // criando a pessoa

            Pessoa p1 = new Pessoa(nome_usuario,sobrenome_usuario,idade_usuario);
            Console.WriteLine($"Pessoa 1: {p1.Nome} {p1.Sobrenome} tem {p1.Idade} anos!");
        }
    }
          
}