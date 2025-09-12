class Chave:
    # metodo construtor 
    def __init__(self,marca):
        self.marca = marca
        self.ativa = False
# definindo a classe
class Car:
    # metedo construtor
    def __init__(self,modelo,ano,cor,potencia,placa,chave:Chave):           #obrigando o parametro chave a ser do tipo classe chave
        self.modelo = modelo
        self.ano = ano
        self.cor = cor
        self.potencia = potencia
        self.placa = placa
        self.ligado = False
        self.aberto = False
        self.chave = chave
        self.velocidade = 0

    def AbrirCarro(self,chave):
        if not self.ligado and not self.aberto and self.chave.marca == chave.marca:
            self.aberto = True
            self.ativa = True
            print("O carro está aberto!")
        else:
            print("O carro ja esta aberto, ou ligado ou a chave esta errada!")

    def LigarCarro(self):
        if not self.ligado and self.aberto:
            self.ligado=True
            print('Carro esta ligado RUUUUUUUUUUUUUUUUUUUM!')
        else:
            print('O carro ou nao esta ligado ou nao esta aberto')       

    def AcelerarCarro(self):
        if self.ligado and self.velocidade >=0:
            self.velocidade += 5
            print(f"O carro {self.modelo} velocidade {self.velocidade} Km")
        else:
            print(f"O carro {self.modelo} esta desligado, precisa ligar primeiro!")

    def FrearCarro(self):
        if self.ligado and self.velocidade >0 :
            self.velocidade -= 5
            print(f"O carro {self.modelo} velocidade {self.velocidade} Km")
        else:
            print(f"O carro {self.modelo} esta desligado, precisa ligar primeiro!")    

    def desligarCarro(self):
        if self.velocidade == 0:
            print('Carro desligado!')
        else:
            print("O carro ainda esta acelerado, reduza a velocidade para poder desligar!")       
         
        






#o carro tem q desligar, mas nao pode desligar acelerado
#tem q ter um metodo de frear 5 em 5 
#e tem q ter a inserção da ativa da chave assim que o metodo abrir for true

