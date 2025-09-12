class Escola:

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentacao(self):
        print(f"Nome: {self.nome} / Idade: {self.idade}")

    

dados1 = Escola("Pedro", 18)
dados2 = Escola("Felipe", 19)

dados = [dados1,dados2]

for i in dados:
    print(i)