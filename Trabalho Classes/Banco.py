from Pessoa import Pessoa


class Banco:
    #metodo  construtor
    # único atributo que adicionei além foi o titular para podermos utilizarmos a class Pessoa para usar o nome e idade posteriormente!

    def __init__(self,numero,titular:Pessoa,saldo,nome_do_banco,agencia):
        self.numero = numero
        self.titular = titular
        self.nome = titular.nome    
        self.saldo = saldo
        self.nome_do_banco = nome_do_banco.lower()
        self.agencia = agencia
        self.credito = []
        

    #metodos
    def TED(self,banco_destino,valor):
        taxa = 0
        if banco_destino.lower()!= self.nome_do_banco:
            taxa = 0.005
            valor = valor + (valor*taxa)
            if valor > self.saldo:
                print(f'{self.nome}: Saldo insuficiente para realizar transferencia')
            else:
                self.saldo -= valor
                print(f'{self.nome}: Transferencia realizada para banco diferente')
                print(f"{self.nome}: Transferencia de R${valor}")
        else:
            if valor > self.saldo:
                print(f'{self.nome}: Saldo insuficiente para realizar transferencia')
            else:
                self.saldo -= valor
                print(f'{self.nome}: Transferencia realizada para o mesmo banco')
                print(f"{self.nome}: Transferencia de R${valor}")



    def saque(self, valor):
        if valor > self.saldo:
            print(f'{self.nome}: Saldo indisponivel para realizar esse saque!')
        else:
            self.saldo -= valor
            print(f'{self.nome}: Saque de R${valor} realizado!')


    def Pix(self,valor):
        if valor > self.saldo:
            print(f"{self.nome}: Saldo insuficiente para fazer Pix!")
        else:
            self.saldo -= valor
            print(f"{self.nome}: pix de R${valor} realizado.")

    def chequeEspecial(self,valor):
        if self.saldo <= 0:
            self.saldo -=valor
            print(f'{self.nome}: Cheque especial utilizado no valor de R${valor}')

        else:
            print(f'{self.nome}: Nao pode realizar cheque especial com saldo na conta!')

    def Emprestimo(self,valor):
        perfil_cliente = self.titular # titular foi feito com a class Pessoa, portanto tem idade
        print(f'{self.nome}:Analisando seu perfil...')
        if perfil_cliente.idade < 18:
            print(f'{self.nome}: Idade insuficiente para fazer emprestimos')
        else:
            self.saldo += valor
            print(f'{self.nome}: Emprestimo de R${valor} realizado!')

    def Credito(self,item,valor):
        cobrança = {
            'item' : item,
            'valor':valor,
        }
        self.credito.append(cobrança)
        print(f'{self.nome}: Compra no credito realizada no valor de R${valor}')


    def VerFatura_credito(self):
        total_fatura = 0
        print(f'Fatura do {self.nome}')
        for compra in self.credito:
            print(f'Item : {compra['item']} | Valor :{compra['valor']}')
            total_fatura += compra['valor']
        print(f'total da fatura: R${total_fatura}')    






    



