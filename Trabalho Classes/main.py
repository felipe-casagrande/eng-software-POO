from Pessoa import Pessoa, Objeto
from Banco import Banco

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
