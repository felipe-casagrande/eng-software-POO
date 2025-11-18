class Funcionario:
    def __init__(self,nome:str,salario:float):
        if salario < 0:
            raise ValueError('O salario não pode ser negativo')
        self.nome = nome
        self.salario = salario
        
    
    def descrever(self):
        print(f'Descrição do funcionario\nNome: {self.nome}\nSalario: {self.salario:.2f}')
        print('-'*30)

    def calcular_bonus(self):
        bonus = self.salario*0.05
        total = self.salario + bonus
        print(f'Calculando bônus do {self.nome}..\nO salario de R${self.salario:.2f},com um bônus de 5% é de R${total:.2f}')    

class Gerente(Funcionario):
    def __init__(self,nome,salario):
        super().__init__(nome,salario)
        self.equipe = []
    def calcular_bonus(self):
        bonus = self.salario*0.1
        total = self.salario + bonus
        print(f'Calculando bônus do {self.nome}..\nO salario de R${self.salario:.2f},com um bônus de 10% é de R${total:.2f}') 
        print('-'*30)

    def adicionar_membro(self,nome:str):
        self.equipe.append(nome)
    
    def descrever(self):
        print(f'Descrição do funcionario\nNome: {self.nome}\nSalario: R${self.salario:.2f}')
        # nao irei apenas mostrar o tamanho da equipe, irei mostrar a equipe toda logo com um laço for
        cont =0
        print(f'EQUIPE DO {self.nome}')
        for pessoa in self.equipe:
            print(f'Nome: {pessoa}')
            cont +=1
        print(f'Tamanho da equipe: {cont}')   
        print('-'*30) 

class Desenvolvedor(Funcionario):
    def __init__(self, nome:str, salario:float,linguagem:str):
        super().__init__(nome, salario)
        self.linguagem = linguagem

    def calcular_bonus(self):
        bonus = self.salario*0.08
        total = self.salario + bonus
        print(f'Calculando bônus do {self.nome}..\nO salario de R${self.salario:.2f},com um bônus de 8% é de R${total:.2f}') 
        print('-'*30)

    def descrever(self):
        print(f'Descrição do funcionario\nNome: {self.nome}\nSalario: R${self.salario:.2f}\nLinguagem: {self.linguagem}')
        

def imprimir_resumo(funcionario:Funcionario):
    funcionario.descrever()
    funcionario.calcular_bonus()

f2 = Gerente('pl',1000)
f3 = Desenvolvedor('felipao',1000,'c#')
f2.descrever()
f3.descrever()
f2.calcular_bonus()
f3.calcular_bonus()
f2.adicionar_membro('Joao')
f2.adicionar_membro('Teteu')
f2.descrever()
imprimir_resumo(f2)

