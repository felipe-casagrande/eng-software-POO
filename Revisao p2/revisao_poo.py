import pandas as pd
import random


class Pessoa:
    def __init__(self,nome,sobrenome,idade,altura):
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade
        self.altura = altura
        self.vida =100
        self.vivo = True

    def falar(self,mensagem):
        print(f'{self.nome} : {mensagem}')

    def andar(self):
        print(f'{self.nome} esta se movendo ...')   

    def parar(self):
        print(f'{self.nome} parou')

class Jogador(Pessoa):
    def __init__(self, nome, sobrenome, idade, altura,tipo,arma,ataque_nome,dano_ataque):
        super().__init__(nome, sobrenome, idade, altura)
        self.tipo = tipo
        self.arma = arma
        self.ataque_nome = ataque_nome
        self.dano_ataque = dano_ataque

    def receber_dano(self,dano):
        self.vida -= dano  
        if self.vida >0:
            print(f'{self.nome} {self.sobrenome} recebeu {dano} de dano. Vida atual {self.vida}')
        else:
            self.vida = 0
            self.vivo = False
            print(f"{self.nome} {self.sobrenome} morreu! ")     

    def atacar(self,alvo:"Jogador"):
        if not self.vivo:
            print(f'{self.nome} {self.sobrenome} ja morreu, nao pode atacar')
        else:
            dano_real = self.dano_ataque + random.randint(-8,+8)
            
            print(f'{self.nome} atacou {alvo.nome} com sua {self.arma} utilizando o ataque {self.ataque_nome}')
            alvo.receber_dano(dano_real)


j1 = Jogador('felipe','casagrande',21,1.75,'monstro','espada','rasagui',20)
j2 = Jogador('Pl','coelho',21,1.75,'monstro','espada','rasagui',20)


class CadastrarJogadores:
    def __init__(self):
        self.df = pd.DataFrame(columns=[
           'nome','sobrenome','idade','altura','tipo','arma','ataque_nome','dano_ataque'
        ])

    def cadastrar(self,jogador:'Jogador'):
        nova_linha = {
            'nome': jogador.nome,
            'sobrenome':jogador.sobrenome,
            'idade': jogador.idade,
            'altura': jogador.altura,
            'tipo': jogador.tipo,
            'arma': jogador.arma,
            'ataque_nome':jogador.ataque_nome,
            'dano_ataque':jogador.dano_ataque
        } 
        self.df = pd.concat([self.df,pd.DataFrame([nova_linha])],ignore_index=True)

    def listar(self):
        print('Jogadores cadastrados!!')
        print(self.df.to_string(index=False))


class CadastroAmbiente:
    def __init__(self,nome_ambiente):
        self.nome_ambiente = nome_ambiente
        self.jogadores = []
        self.historico = pd.DataFrame(columns=[
             'rodada', 'atacante', 'defensor', 'dano_causado', 'vida_restante'
        ])

    def adicionar_jogador(self,jogador:"Jogador"):
        self.jogadores.append(jogador)
        print(f'{jogador.nome} {jogador.sobrenome} adicionado ao ambiente {self.nome_ambiente}')

    
    def listar_jogadores(self):
        print(f'Jogadores na arena {self.nome_ambiente}')
        for j in self.jogadores:
            if j.vivo:
                status = 'vivo'
            else:
                status ='morto'

            print(f'{j.nome} {j.sobrenome} {j.tipo} |Vida: {j.vida} |Status: {status} ')    







ambiente = CadastroAmbiente('puteiro')
ambiente.adicionar_jogador(j1)
ambiente.listar_jogadores()



cad = CadastrarJogadores()
cad.cadastrar(j1)
cad.cadastrar(j2)
cad.listar()