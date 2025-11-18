class Chave:
     def __init__(self,id_chave):
          self.id_chave = id_chave


class Carro:
    def __init__(self,id_chave):
        self.chave = id_chave
        self.porta_aberta = False
        self.ligado = False
        self.velocidade = 0.0
        self.marcha = 0
        self.pessoa_dentro = None
        self.historico = []

        # Validar chave para facilitar verificação futura
    def validar_chave(self,chave: "Chave"):
        if self.chave == chave.id_chave:
            return True
        else:
            return False
        
    def abrir(self,chave):
        if not self.validar_chave(chave):
            print('Chave incorreta')
        elif self.porta_aberta:
            print('Porta ja esta aberta')
        else:
            self.porta_aberta = True
            print('Abrindo porta')
            self.historico.append('Abrir porta')

    def fechar(self,chave):
        if not self.validar_chave(chave):
            print('Chave incorreta')
        elif not self.porta_aberta:
            print('Porta ja esta fechada')
        else:
            self.porta_aberta = False
            print('Fechando porta')
            self.historico.append('Fechando porta')


    def ligar(self,pessoa:'Pessoa'):
        if self.validar_chave(pessoa.chave):
            if not self.porta_aberta and self.pessoa_dentro:
                self.ligado = True
                print('Ligando carro')
                self.historico.append('Ligando carro')
            elif self.porta_aberta:
                print('Fecha a porta para ligar')
            elif not self.pessoa_dentro:
                print('Tem que ter uma pessoa dentro para ligar o carro')
        else:
            print('Chave Incorreta')

    def desligar(self,pessoa: 'Pessoa'):
        if self.validar_chave(pessoa.chave):
            if not self.porta_aberta and self.pessoa_dentro and self.velocidade==0:  #nao pode desligar com o carro em movimento
                self.ligado = False
                print('desligando o carro')
                self.historico.append('desligando carro')
            elif self.porta_aberta:
                print('Fecha a porta primeiro')
            elif not self.pessoa_dentro:
                print('Tem que ter uma pessoa dentro do carro')
            elif self.velocidade>0:
                print('Freiar o carro antes de desligar.')
        else:
            print("Chave incorreta")        

    def acelerar(self,pessoa: "Pessoa"):
        if self.validar_chave(pessoa.chave):
            if self.porta_aberta:
                print('Nao tem como acelerar com a porta aberta')
            elif not self.pessoa_dentro:
                print('Nao tem como acelerar sem uma pessoa dentro')
            elif self.marcha == 0:
                print('Marcha no neutro, troque para acelerar')
            else:
                self.velocidade += self.calcular_acelerecao()
                print(f'Acelerando {self.calcular_acelerecao()}km , velocidade atual {self.velocidade}km')
                self.historico.append('acelerando carro') 
        else:
            print('Chave incorreta')


    def trocar_marcha(self,marcha):
        if not self.ligado:
            print('Ligue o carro para trocar de marcha')
        elif marcha < 0:
            print('Nao pode trocar para numeros negativos')
        elif marcha >5:
            print('Nao temos carro com mais de 5 marchas')
        elif marcha == 0:
            self.marcha = marcha
            print('Marcha trocado para neutro')        
        else:
            if marcha <self.marcha:
                self.velocidade -= 5.0
                self.marcha = marcha
                print(f'Engatando {marcha} marcha!')
                print(f'Freio motor ativado, diminuindo 5km. Velocidade atual: {self.velocidade}km')
                self.historico.append('Trocando marcha')
            else:
                print(f'Engatando {marcha} marcha!')    
                self.marcha = marcha
                self.historico.append('Trocando marcha')
                

    def calcular_acelerecao(self):
        if self.marcha == 1:
            return 5.0
        elif self.marcha == 2:
            return 10.0
        elif self.marcha == 3:
            return 15.0
        elif self.marcha == 4:
            return 20.0
        elif self.marcha == 5:
            return 25.0
        
    def frear(self,pessoa:"Pessoa"):
        if self.validar_chave(pessoa.chave):
            if not self.pessoa_dentro:
                print('Tem que ter alguem dentro para frear')
            elif not self.ligado:
                print('Carro tem que estar ligado para freiar')
            else:
                self.velocidade -=5.0
                print(f'Freiando..., velocidade atual {self.velocidade}')
                self.historico.append('Freiando carro')
                  
        
    def permitir_saida(self,pessoa:"Pessoa"):
        if self.validar_chave(pessoa.chave):
            if not self.ligado:
                print('Saindo do carro')
                self.pessoa_dentro = None
                pessoa.dentro_carro = False
                self.historico.append('Permitindo saida do carro')
            else:
                print('Desligue o carro para sair')

    def esta_parado(self):
        if self.velocidade == 0:
            print('Esta parado')
        else:
            print('Carro em movimento')    

    def VerHistorico(self):
        print('-'*30)
        print('HISTORICO DE AÇÕES')
        print('-'*30)
        for c in self.historico:
            print(f"Ação realizada: {c}")   
            
class Pessoa:
    def __init__(self,nome,sobrenome,idade,altura,chave: Chave):
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade
        self.altura = altura
        self.chave = chave
        self.dentro_carro = False

    def abrir_carro(self,carro:"Carro"):
        return carro.abrir(self.chave)
    def fechar_carro(self,carro:"Carro"):
        return carro.fechar(self.chave)    
    def entrar_carro(self,carro:"Carro"):
        if not carro.porta_aberta:
            print('Abra a porta para entrar no carro')
        elif carro.pessoa_dentro:
            print('Ja tem uma pessoa dentro')
        else:
            self.dentro_carro = True
            carro.pessoa_dentro = self
            print('Entrando no carro')

    def sair_carro(self,carro:"Carro"):
        return carro.permitir_saida(self)        

#-----------------------------------------------------------EXECUTANDO--------------------------------------------------------------------------

ch1 = Chave('aa')
carro1 = Carro('aa')
p1 = Pessoa('felipe','Casagrande',10,1.87,ch1)

p1.abrir_carro(carro1)
p1.entrar_carro(carro1)
p1.fechar_carro(carro1)

carro1.ligar(p1)
carro1.trocar_marcha(1)
carro1.acelerar(p1)
carro1.trocar_marcha(2)
carro1.trocar_marcha(3)
carro1.acelerar(p1)
carro1.trocar_marcha(2)
carro1.permitir_saida(p1)
carro1.desligar(p1)
carro1.frear(p1)
carro1.frear(p1)
carro1.frear(p1)
carro1.desligar(p1)
carro1.permitir_saida(p1)
carro1.VerHistorico()
        