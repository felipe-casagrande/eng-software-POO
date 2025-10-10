'''Crie uma classe que apresente os seguinte atributos:
      Class Banco(numero, nome, saldo, nome do banco, agencia) <-- atributos
        - Métodos
            - transferir - TED, sacar, PIX, Cheque_especial, emprestimo, crédito
            - transferir - TED se eu tiver a quantia em conta -- tem um % cobrado se o banco for diferente
            - PIX só posso realizar o pix se eu tiver isso em conta
            - Cheque_especial --> o seu saldo precisa ser < 0 ele tem juros -- nada de ter time
            - Empréstimo --> Comprar um casa e solicita um empréstimo ao banco e seu perfil será avaliado
             - Crédito --> é quando você quer comprar algo e ter um saldo < ou > que o valor do produto e terá um cobrança no final do mês
            - Crédito deve ter um relatório de ações.'''


class Banco:
    def __init__(self,numero,nome,saldo,nome_banco,agencia):
        self.numero = numero
        self.nome = nome
        self.saldo = saldo
        self.nome_banco = nome_banco.lower()
        self.agencia = agencia
        self.Fatura = []

    def sacar(self,valor):
        if self.saldo >= valor:
            self.saldo -=valor
            return f"{self.nome}: Saque de R${valor} realizado com sucesso!"
        else:
            return f'{self.nome}: Saldo insuficiente para realizar saque'
        

    def TED(self,valor,banco_transferencia):
        if self.nome_banco.lower() != banco_transferencia.lower():
            valor = valor +(valor*0.005)  # se for de banco diferente taxa de 5%
            if self.saldo >= valor:
                self.saldo -= valor
                return f"{self.nome}: Transferencia TED entre bancos diferentes, valor foi de R${valor}"
            else:
                return f"{self.nome}: Saldo insuficiente para realizar TED"
        else:   
            if self.saldo >= valor:
                self.saldo -= valor
                return f"{self.nome}: Transferencia TED do mesmo banco, valor foi de R${valor}"
            else:
                return f"{self.nome}: Saldo insuficiente para realizar TED"
            
    def pix(self,valor):
        if self.saldo >= valor:
            self.saldo -= valor
            return f"{self.nome}: Pix realizado no valor de {valor}"
        else:
            return f'{self.nome}: Saldo insuficiente para realizar pix'
        


    def cheque_especial(self,valor):
        if self.saldo >=0:
            return f"{self.nome}: Seu saldo nao é negativo, nao pode realizar cheque especial"
        else:
            #calculando valor 
            valor = valor +(valor*0.008)
            self.saldo -=valor 
            return f'{self.nome}: Cheque especial realizado no valor de R${valor}!'
        
        
    def emprestimo(self,valor,finalidade):
        print('perfil sendo avaliado..')
        
        print('Perfil aprovado')
        return f'{self.nome}: Emprestimo de R${valor} foi realizado para comprar {finalidade} '  
    
    def credito(self,nomeProduto,valor):
        compra = {
            'item' : nomeProduto,
            'valor': valor
        }
        self.Fatura.append(compra)
        return f'item {nomeProduto} foi comprado no valor de {valor}'

    def fatura(self):
        total = 0
        print(f'{'-'*10} {'Fatura'}{'-'*10}')
        print(f'{'item':<10}|{'valor':<10}')
        print('-'*30)
        for compra in self.Fatura:
            print(f'{compra['item']:<10}|R${compra['valor']:<10}')
            total += compra['valor']    
        print('-'*30)    
        print(f'{'total':<10}|R${total:<10}')    
            


p1 = Banco(222131,'Felipe',1000,'itau',2122)
p1.credito('Celular',100)
p1.credito('Casa',10)
print(p1.credito('celular',100))
print(p1.sacar(500))
print(p1.cheque_especial(10))
print(p1.emprestimo(500,'casa'))
print(p1.TED(200,'itau'))
print(p1.pix(50))
print(p1.saldo)
print(p1.credito('Mercedes',1000))
p1.fatura()