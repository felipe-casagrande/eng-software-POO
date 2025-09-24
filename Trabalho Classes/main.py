from Pessoa import Pessoa, Objeto
from Banco import Banco

# Como usar os metodos:
#parametros
    # TED - informar o banco de destino e o valor 
    # saque - apenas o valor
    # Pix - Apenas o valor
    # Cheque especial - Apenas o valor, liberado para contas negativadas ou com 0 reais
    # Emprestimo - Apenas o valor, mas tera uma condição de apenas usuario com 21 anos realizar (fiz só pra ter algo para o perfil ser avaliado)
    # Credito - Informar o que esta comprando ou loja e depois o valor. Exemplo: ("Celular",1000.00) ou ("Americanas",5.99) 
    # Ver fatura - Só chamar a funçao e tera o relatorio das compras do cartao de credito

pessoa1 = Pessoa('felipe',22)
pessoa2 = Pessoa('Diego', 30)

conta1 = Banco(21,pessoa1,100,"itau",2021)
conta2 = Banco(22,pessoa2,10000,'Bradesco',2222)

    

conta1.saque(10)
conta1.Pix(10)
conta1.Emprestimo(1000)
conta1.TED('itau',50)
conta1.chequeEspecial(10)
conta1.Credito('celular',1000)
conta1.Credito('casa',5000)
conta1.VerFatura_credito()
