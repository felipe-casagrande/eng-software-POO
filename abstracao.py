class veiculo:
    def __init__(self,marca,modelo,ano,tipo):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.ligado = False
        self.tipo = tipo
        self.velocidade = 0
        self.marcha = 0
        

    # metodos : apresentar, ligar, desligar, acelerar,passa_marcha

    #apresentar
    def __str__(self):
        return f"O veiculo é da marca: {self.marca} e  Ano: {self.ano} e tipo {self.tipo}"
    
    # ligar
    def ligar(self):
        if not self.ligado:
            self.ligado = True
            print('O carro carro esta ligado!! RUUUUMM!')
        else:
            print('Carro já esta ligado nesse momento!')

    # desligar
    def desligar(self):
        if self.ligado and self.velocidade == 0:
            self.ligado = False
            print("Desligando carro..")
        else:
            print('Carro ja esa desligado no momento!!')

    def acelerar(self):
        pass  # que pode dar continuidade -  no momento esse metodo nao sera definido

    def mudar_marcha(self):
        print('Nao possui marcha')
        pass # que pode da continuidade - no momento nao sera definido        


class bike(veiculo):
    def __init__(self, marca, modelo, ano,tipo,autonomia):
        super().__init__(marca, modelo, ano, tipo)
        self.autonomia = autonomia

    def __str__(self):
        return f"{super().__str__()}"    

    def acelerar(self):
        if self.ligado and self.velocidade<=60:
            self.velocidade += 5
            print(f'Acelerando 5km, velocidade atual : {self.velocidade}')
        else:
            print('Nao esta ligado')
    def frear(self):
        if self.velocidade == 0:
            print('Ja esta parado..')
        else:
            self.velocidade -=5
            print(f"Freiando..., velocidade atual: {self.velocidade}")       

b1 = bike("caloi",'aro 25','2025','Bike','20')


class Aviao(veiculo):
    def __init__(self, marca, modelo, ano, tipo):
        super().__init__(marca, modelo, ano, tipo)
    def acelerar(self):
        if self.ligado:
            self.velocidade +=50
            print(f'Acelerando 50km, velocidade atual {self.velocidade}')    
        else:
            print('ligue o aviao para acelerar')

    def mudar_marcha(self,marcha):
        print(f'Mudando de {self.marcha} para {marcha}')
        self.marcha = marcha
        
print(b1)
a1 = Aviao('gol','voa','2025','aviao')
a1.ligar()
a1.mudar_marcha(1)
a1.acelerar()
a1.mudar_marcha(2)
