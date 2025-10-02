
class Chave:
    def __init__(self, id_chave: str):
        self.id_chave = id_chave


class Carro:
    def __init__(self, id_chave: str):
        self.chave = id_chave
        self.porta_aberta = False
        self.ligado = False
        self.velocidade = 0.0
        self.marcha = 0
        self.pessoa_dentro:'Pessoa' = None
        self.historico = []

    def abrir(self, chave):
        if self.chave == chave:
            self.porta_aberta = True
            print('Abrindo carro')
            self.historico.append('Abrir carro')    
            
        else:
            print('Chave nao compativel ')

    def fechar(self, chave):
        if self.chave == chave:
            self.porta_aberta = False
            print('Fechando carro')
            self.historico.append('Fechar carro')    
        else:
            print('Chave nao compativel para fechar')
 
    def ligar(self, pessoa: "Pessoa"):
        if self.chave == pessoa.chave.id_chave:
            if not self.porta_aberta and pessoa.dentro_carro:
                self.ligado = True
                print(f'Ligando carro!')
                self.historico.append('Ligar carro')
            else:
                print('algo esta errado, nao posso ligar')
        else:
            print('Chave Incorreta')
    

    def desligar(self, pessoa: "Pessoa"):
        #nao esta no texto, mas irei colocar para apenas desligar se estiver parado, se nao a pessoa pode desligar o carro e sair dele c ele em movimento
        if self.chave == pessoa.chave.id_chave:
            if not self.porta_aberta and pessoa.dentro_carro and self.velocidade == 0.0:
                self.ligado = False
                print('desligando...')
                self.historico.append('Desligar carro')
            else:
                print('Nao posso desligar')   

        else:
            print('Chave nao esta valida')        

    def acelerar(self,pessoa: "Pessoa"):
        #pelo que entendi, dependendo da marcha que estiver a aceleração vai ser diferente, entao vamos lá, irei fazer até a quinta marcha
        # nao entendi a necessidade do pessoa.., entao irei colocar que apenas a pessoa que esta dentro pode acelerar ou frear

        if self.chave == pessoa.chave.id_chave:   #verificando se a chave é a certa
            if self.porta_aberta or not self.pessoa_dentro:     
                print('Nao tem como acelerar com a porta aberta ou sem pessoas dentro...')
            else:
                if self.ligado:
                    if self.marcha == 1:
                        self.velocidade += 5.0
                        print('Acelerando 5km')
                        self.historico.append('Acelerando carro')
                    elif self.marcha == 2:
                        self.velocidade += 10.0
                        print('Acelerando 10km')
                        self.historico.append('Acelerando carro')
                    elif self.marcha == 3:
                        self.velocidade += 15.0 
                        print('Acelerando 15km')
                        self.historico.append('Acelerando carro')
                    elif self.marcha == 4:
                        self.velocidade += 20.0
                        print('Acelerando 20km')
                        self.historico.append('Acelerando carro')
                    elif self.marcha == 5:
                        self.velocidade += 25.0
                        self.historico.append('Acelerando carro')
                        print('Acelerando 25km')
                        self.historico.append('Acelerando carro')   
                    elif self.marcha == 6:
                        self.velocidade += 30.0
                        print('Acelerando 30km')
                        self.historico.append('Acelerando carro')
                    else:
                        print('Passe uma marcha primeiro para acelerar!')    
                else:
                        print('Carro nao esta ligado para acelerar')
        else:
            print('Chave nao esta valida')                

    def frear(self,pessoa:"Pessoa"):
        if self.chave == pessoa.chave.id_chave:
            if self.porta_aberta or not self.pessoa_dentro:     
                print('Nao tem como frear com a porta aberta ou sem pessoas dentro...')
            else:
                if self.ligado and self.velocidade>0:
                    self.velocidade -=5
                    print(f'Diminuindo.., velocidade atual : {self.velocidade}')
                    self.historico.append('Freando carro')
                else:
                    print('Carro nao esta em movimento para ser freiado')
        else:
            print('Chave nao esta valida')

    def trocar_marcha(self,marcha):
        
        if marcha <0:
            print('Nao pode trocar marcha para valores negativos..')
        elif marcha == 0:
            print('Marcha trocada para o neutro 0')    
        elif marcha >7:
            print('Nao tem carro com essa quantidade de marcha, passe ate a sexta marcha!')
        else:
            if marcha < self.marcha:
                #nao sei quanto diminuir, irei tirar 5km
                self.velocidade -=5.0
                print(f"Diminuindo velocidade com freio motor, velocidade atual {self.velocidade}km/h")
            self.marcha = marcha
            self.historico.append('Trocando de marcha')
    

    def calcular_aceleracao(self):
        print('')

    def permitir_saida(self,pessoa:"Pessoa"):
        if self.chave == pessoa.chave.id_chave:
            if not self.ligado and self.porta_aberta and self.pessoa_dentro == pessoa:  #só pode sair com o carro desligado, depois de abrir a porta e se a pessoa que esta fazendo o comando é a que esta no carro. 
                pessoa.dentro_carro = False
                print('Saida autorizada,saindo')
                self.historico.append('Sair do carro')
            else:
                print('Saida nao autorizada, desligue o carro, abra a porta ou verifique se é a pessoa correta')
        else:
            print('Chave nao esta valida')

    def esta_parado(self):
        if self.velocidade == 0.0:
            print('Carro esta parado')
        else:
            print('Carro nao esta parado')

    def ver_historico(self,carro):
        print(f'HISTORICO DE AÇÕES DO CARRO SOLICITADO')
        print('-'*30)
        
        for c in self.historico:
            print(f'Ação realizada: {c}')


class Pessoa:
    def __init__(self, nome, sobrenome, idade: int, altura: float, chave: Chave):
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade
        self.altura = altura
        self.velocidade: float = 0.0
        self.chave = chave
        self.dentro_carro = False

    def abrir_carro(self, carro: "Carro"):
        if carro.porta_aberta:
            print('Carro ja esta aberto!')
        else:
            if self.chave.id_chave == carro.chave:
                carro.abrir(self.chave.id_chave)
               

    def fechar_carro(self, carro: "Carro"):
        if not carro.porta_aberta:
            print('Porta ja esta fechada!')
        else:

            if self.chave.id_chave == carro.chave:
                carro.fechar(self.chave.id_chave)
             

    def entrar_carro(self,carro: 'Carro'):
        if self.dentro_carro:
            print('Voce ja esta dentro do carro!')
        else:
            if carro.porta_aberta == False:
                print('Primeiro abra a porta para poder entrar!')
            else:
                self.dentro_carro = True
                carro.pessoa_dentro = self
                print("Entrando no carro!")


    def sair_carro(self,carro: 'Carro'):
        if carro.ligado:
            print('Desligue o carro primeiro para sair!')
        else:
            carro.permitir_saida(self)
            
            

    
             


