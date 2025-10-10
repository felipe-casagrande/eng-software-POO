'''Class Banco(numero, nome, saldo, nome do banco, agencia) <-- atributos
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
        self.nome_banco = nome_banco
        self.agencia = agencia
        self.saldo_emprestimo = 0
        self.fatura = []

    def sacar(self,valor):
        if self.saldo >=valor:
            self.saldo -=valor
            print("Saque Realizado")
        else:
            print('Saldo insuficiente para saque')

    def TED (self,valor,banco):
        if self.nome_banco != banco: #paga juros
            valor = valor +(valor*0.008)
            if self.saldo > valor:
                self.saldo -=valor
                print('Transferencia realizada para banco diferente com juros')
            else:
                print('Saldo insuficiente para realizar transferencia')
        else:   #sem juros
            if self.saldo>valor:
                self.saldo -=valor
                print('Transferencia realiazada com sucesso')
            else:
                print('Saldo insuficiente')   

    def pix (self,valor):
        if self.saldo > valor:
            self.saldo -=valor
            print("Pix realizado")
        else:
            print('Sem saldo para realizar pix')

    def cheque_especial(self,valor):
        if self.saldo >0:
            print('Voce tem saldo na conta, nao pode realizar cheque especial')
        else:
            valor = valor + (valor*0.005)
            self.saldo -=valor   #nao sei oq é cheque especial, mas vou dizer que deixaria a conta ainda mais negativa
            print('Cheque especial realizado')

    def emprestimo (self,valor,finalidade):
        print('perfil sendo avaliado')
        self.saldo_emprestimo += valor      #irei dizer que o emprestimo sera somado numa variavel de emprestimo
        print(f'O emprestimo de {valor} foi realizado para comprar {finalidade} ')

    def credito(self,valor:float,item:str):
        compra ={
            'item':item,
            'valor': valor
        }
        self.fatura.append(compra)

    def verFatura(self):
        total = 0
        print('HISTORICO DE CREDITO')
        print('-'*30)
        print(f'{'Item':<10} | {'Valor':<10}')
        for compra in self.fatura:
            print(f'{compra['item']:<10} | {compra['valor']:<10}')
            total += compra['valor']
        print('-'*30)    
        print(f'{'Total':<10} | {total:<10}')    

p1 = Banco(22222,'Felipe',1000,'itau',2211)
p1.credito(100,'celular')
p1.credito(200,'casa')
p1.emprestimo(1000,'casa')
print(p1.saldo_emprestimo)
p1.verFatura()        