using System;
using System.Collections.Generic;
using System.ComponentModel.DataAnnotations;
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

            Console.WriteLine("Digite seu cpf: ");
            string cpf_usuario = Console.ReadLine();
            
            //mudando nome
            
            // criando a pessoa

            Pessoa p1 = new Pessoa(nome_usuario,sobrenome_usuario,cpf_usuario);
            Console.WriteLine($"Pessoa 1: {p1.Nome} {p1.Sobrenome} tem {p1.Cpf} anos!");
            if (p1.Cpf.Length < 11) {
                Console.WriteLine("Nome pequeno");
            } else if (p1.Cpf.Length == 11) {
                Console.WriteLine("cpf valido");
            }else { Console.WriteLine("Cpf grande dms"); }
        }
        

    }
          
}