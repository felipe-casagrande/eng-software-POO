from Pessoa import Pessoa
from Objeto import Carro
from Banco import Banco
# Como usar os metodos do banco:
    #parametros
    # TED - informar o banco de destino e o valor 
    # saque - apenas o valor
    # Pix - Apenas o valor
    # chequeEspecial - Apenas o valor, liberado para contas negativadas ou com 0 reais
    # Emprestimo - Apenas o valor, mas tera uma condição de apenas usuario com idade >=18 anos pode realizar (fiz só pra ter algo para o perfil ser avaliado)
    # Credito - Informar o que esta comprando ou loja e depois o valor. Exemplo: ("Celular",1000.00) ou ("Americanas",5.99) 
    # VerFatura_credito - Só chamar a funçao e tera o relatorio das compras do cartao de credito

# Objetos vou criar de carro e tera 5 atributos - modelo, ano, cor, potencia e placa
# Pessoa tera 3 atributos, Nome, idade e sexo
# No banco utilizei a agregação de pessoa para o Nome e no emprestimo utilzei para criar uma variavel e usar a idade.

#--------------------------------------------------------------------//-----------------------------------

pessoa1 = Pessoa('Felipe Casagrande',22,'Masculino')
pessoa2 = Pessoa('Diego Ramos', 30,'Masculino')

Carro1= Carro('Toyota Etios',2025,'Preta',2.0,'KPH227')

conta1 = Banco(21,pessoa1,100,"Itau",2021)
conta2 = Banco(22,pessoa2,10000,'Bradesco',2222)

    

conta1.saque(1000)
conta1.Pix(0)
conta1.Emprestimo(0)
conta1.TED('BRADESCO',50)
conta1.chequeEspecial(10)
conta1.Credito('celular',1000)
conta1.Credito('casa',5000)
conta1.VerFatura_credito()
