using System;
using System.Numerics;
public class Funcionario        // criando a classe e definindo os paramentros
{
    public string Nome { get; set; }                      // para colocar atributos, sempre colocar o public na frente 
    public double Salario { get; set; }
    // METODO CONSTRUTOR. tipo o init
    public Funcionario(string nome, double salario)  //inves de colocar um init, tem q colocar o nome da class
    {
        this.Nome = nome;                                         // this funciona como um self
        this.Salario = salario;
    }
    public virtual void Descrever()                                // Virtual na classe pai para dizer que pode ser trocado, nas heranças sera overrited
    {
        Console.WriteLine(new string('-', 30));
        Console.WriteLine($"Descrição do {this.Nome}");
        Console.WriteLine($"Nome: {this.Nome}\nSalario: {this.Salario}");  //aprender a formatar o :.2f em c#
    
    }
    public virtual void CalcularBonus() 
    {
        Console.WriteLine(new string('-', 30));
        const double percentual_bonus = 0.05;
        double total = this.Salario *(1 + percentual_bonus);
        Console.WriteLine($"O salario do {this.Nome} com um aumento de 5% foi para {total}");
    }
}
//--------------------------------------------------------------------GERENTE------------------------------------------------------------------------------------------//
public class Gerente: Funcionario 
{ 
    public List<string> Equipe { get; set; }
    public Gerente(string nome,double salario) : base(nome,salario)    // o base serve como um super, tudo que herdar da outra classe use o base.
    { 
        this.Equipe = new List<string>();
    
    }
    public override void CalcularBonus()
    {
        Console.WriteLine(new string('-', 30));
        const double percentual_bonus = 0.10;
        double total = this.Salario * (1 + percentual_bonus);
        Console.WriteLine($"O salario do {this.Nome} com um aumento de 5% foi para {total}");
        Console.WriteLine(new string('-', 30));
    }
    public void Adicionar_membro(string nome) 
    { 
        this.Equipe.Add(nome);                                //add == append
    
    }
    public override void Descrever()
    {
        Console.WriteLine(new string('-', 30));
        Console.WriteLine($"Descrição do {this.Nome}");
        Console.WriteLine($"Nome: {this.Nome}\nSalario: {this.Salario}");
        Console.WriteLine("Equipe:");
        foreach (string pessoa in this.Equipe)             //foreach é usado nesses casos de percorrer listas, dicionarios etc.
        { 
            Console.WriteLine($"Nome: {pessoa}");

        }
        Console.WriteLine($"O tamanho da equipe é {this.Equipe.Count}");
    }   
}

//----------------------------------------------------------------------DESENVOLVEDOR------------------------------------------------------------//

public class Desenvolvedor: Funcionario 
{
    public string linguagem { get; set; }           // para colocar atributos, sempre colocar o public na frente 

    public Desenvolvedor(string nome, double salario, string linguagem) :base(nome,salario) 
    { 
        this.linguagem = linguagem;
    }
    public override void CalcularBonus() 
    {
        Console.WriteLine(new string('-', 30));
        const double percentual_bonus = 0.08;
        double total = this.Salario * (1 + percentual_bonus);
        Console.WriteLine($"O salario do {this.Nome} com um aumento de 5% foi para {total}");
        
    }
    public override void Descrever() 
    {
        Console.WriteLine(new string('-', 30));
        Console.WriteLine($"Descrição do {this.Nome}");
        Console.WriteLine($"Nome: {this.Nome}\nSalario: {this.Salario}\nLinguagem: {this.linguagem}");
    }
}


public class program                                                // para rodar sempre ter um main
{
    public static void Main(string[] args)
    {
        Funcionario f1 = new Funcionario("Felipe", 1000);            // sempre tipar a variavel para poder cria la
        f1.Descrever();
        Gerente Gerente1 = new Gerente("Vitao", 1000);
        Gerente1.Adicionar_membro("Leozin Viado");
        Desenvolvedor Desenvoledor1 = new Desenvolvedor("Joao gomes",1000,"c#");
        Desenvoledor1.CalcularBonus();
        Gerente1.Descrever();
    }
}
