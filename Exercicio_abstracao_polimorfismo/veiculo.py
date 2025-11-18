class Veiculo:
    def __init__(self,marca:str,modelo:str,ano:int):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.velocidade = 0
        self.ligado = False
    def __str__(self):
        return f'Marca: {self.marca}\nModelo: {self.modelo}\nAno: {self.ano}'
    
    
    def ligar(self):
        pass
    
    def acelerar(self):
        pass


class Carro(Veiculo):
    def __init__(self, marca:str, modelo:str, ano:int,qnt_portas:int):
        super().__init__(marca, modelo, ano)
        self.qnt_portas = qnt_portas

    def __str__(self):
        return f'{super().__str__()}\nPortas: {self.qnt_portas}'   

    def ligar(self):
        if not self.ligado and self.velocidade == 0:
            self.ligado = True
            return f"Ligando carro..."
        elif self.ligado:
            return f"Carro ja esta ligado"
        elif self.velocidade != 0:
            return f"Carro tem que estar parado para ligar!"
    
    def desligar(self):
        if self.ligado and self.velocidade == 0:
            self.ligado = False
            return f"Desligando carro..."
        elif not self.ligado:
            return 'Carro já esta desligado'
        elif self.velocidade != 0:
            return "Pare o carro para poder desligar!"
                         
    def acelerar(self):
        if self.ligado:
            self.velocidade += 5
            return f"Acelerando carro, velocidade atual {self.velocidade}"
        elif not self.ligado:
            return 'Nao tem como acelerar com o carro desligado..'
        
    def frear(self):
        if self.ligado:
            self.velocidade -= 5
            if self.velocidade < 0:
                self.velocidade = 0   # nao deixa o carro ficar com velocidade negativa!
            return f"Freiando carro, velocidade atual {self.velocidade}"
        elif not self.ligado:
            return 'Nao tem como frear com o carro desligado..'
        

class Moto(Veiculo):
    def __init__(self, marca, modelo, ano):
        super().__init__(marca, modelo, ano)       

    def __str__(self):
        return super().__str__()
    
    def ligar(self):
        if not self.ligado and self.velocidade == 0:
            self.ligado = True
            return "Ligando moto..."
        elif self.ligado:
            return "Moto já esta ligada"
        elif self.velocidade != 0:
            return "Moto em movimento, pare para poder ligar"
        
    def desligar(self):
        if self.ligado and self.velocidade == 0:
            self.ligado = False
            return "Desligando moto..."
        elif not self.ligado:
            return "Moto já esta desligada"
        elif self.velocidade != 0:
            return "Moto em movimento, pare para poder desligar"
        
    def acelerar(self):
        if self.ligado:
            self.velocidade +=5
            return f"Acelerando moto..., velocidade atual: {self.velocidade}"
    def frear(self):
        if self.ligado:
            self.velocidade -= 5
            if self.velocidade < 0:
                self.velocidade = 0   # nao deixa a moto ficar com velocidade negativa!
            return f"Freiando moto, velocidade atual {self.velocidade}"
        elif not self.ligado:
            return 'Nao tem como frear com a moto desligada..'    


## comandos
carro1 = Carro("Fiat","Toro",2025, 4)
print(carro1)
print(carro1.ligar())
print(carro1.desligar())
print(carro1.acelerar())

moto1 = Moto('yamaha',"Fazer",2025)
print(moto1)
print(moto1.desligar())
print(moto1.ligar())
print(moto1.acelerar())
print(moto1.desligar())
print(moto1.ligar())
print(moto1.frear())
print(moto1.desligar())    