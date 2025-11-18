import time
import pandas as pd

# --- CLASSES  ---

class Pessoa:
    def __init__(self, nome, sobrenome, idade, altura):
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade
        self.altura = altura
        self.vida = 100
        self.vivo = True
    
    # Métodos Abstratis
    def falar(self):
        pass
    def andar(self):
        pass
    def parar(self):
        pass

class Jogador(Pessoa):
    def __init__(self, nome, sobrenome, idade, altura, tipo, arma, qnt_vidas, nome_ataque, dano_ataque):
        super().__init__(nome, sobrenome, idade, altura)
        self.tipo = tipo
        self.qnt_vidas = qnt_vidas
        self.arma = arma
        self.nome_ataque = nome_ataque
        self.dano_ataque = dano_ataque
    
    def atacar(self, player2: "Jogador"):
        time.sleep(0.1) 

        # Checa se o atacante ou o alvo já estão mortos
        if not self.vivo or not player2.vivo:
            return # Sai da função se alguém já estiver morto

        # Aplica o dano
        player2.vida -= self.dano_ataque    
        print(f'⚔️ {self.nome} atacou {player2.nome} com {self.nome_ataque} (-{self.dano_ataque} Dano). Vida de {player2.nome}: {player2.vida}')
        
        # Lógica de morte/renascimento
        if player2.vida <= 0:
            player2.qnt_vidas -= 1 
            
            if player2.qnt_vidas == 0:
                player2.vivo = False # Morte definitiva
                print(f'💀 {player2.nome} foi derrotado!')
            else:
                player2.vida = 100 # Renasce
                print(f'🌟 {player2.nome} perdeu uma vida extra, mas renasceu! Vidas restantes: {player2.qnt_vidas}')
    
    # Implementações dos métodos de Pessoa
    def falar(self):
        print(f'{self.nome}: Pronto para o combate!')
    def andar(self):
        print(f'{self.nome} está se movimentando.')
    def parar(self):
        print(f'{self.nome} parou.')

 
# --- CLASSES DE CADASTRO COM PANDAS ---

class CadastroJogadores:
    # Cadastro de Jogadores, usa Pandas DataFrame
    def __init__(self):
        self.df_jogadores = pd.DataFrame(columns=["Nome","Sobrenome","Tipo", "Arma","Vidas","Ataque","Dano"])
    
    def cadastrar(self, jogador: Jogador):
        novo = {
            "Nome" :    jogador.nome,
            "Sobrenome":jogador.sobrenome,
            "Tipo" :    jogador.tipo,
            "Arma" :    jogador.arma,
            'Vidas' :   jogador.qnt_vidas,
            "Ataque":   jogador.nome_ataque,
            "Dano"  :   jogador.dano_ataque
        }
        self.df_jogadores = pd.concat([self.df_jogadores, pd.DataFrame([novo])], ignore_index=True)    # cria um dateFrame temporario e ja usa ele para juntar no principal   
        print(f'✅ Jogador **{jogador.nome}** cadastrado com sucesso!')

    def mostrar_dados(self):
        print("\n=== JOGADORES CADASTRADOS ===")
        print(self.df_jogadores)

class CadastroAmbiente:
    # Cadastro de Ambiente, usa Pandas DataFrame
    def __init__(self):
        # Colunas específicas para o ambiente
        self.df_ambiente = pd.DataFrame(columns=["Local","Tipo de Terreno", "Clima", "Periculosidade"])

    def cadastrar(self, local: str, terreno: str, clima: str, perigo: str):
        novo_ambiente = {
            "Local" :           local,
            "Tipo de Terreno":  terreno,
            "Clima" :           clima,
            "Periculosidade" :  perigo
        }
        self.df_ambiente = pd.concat([self.df_ambiente, pd.DataFrame([novo_ambiente])], ignore_index=True)
        print(f'✅ Ambiente **{local}** cadastrado com sucesso!')

    def mostrar_dados(self):
        print("\n=== AMBIENTES CADASTRADOS ===")
        print(self.df_ambiente)


# --- FUNÇÕES POLIMÓRFICAS ---

def executar_cadastro(objeto_cadastro, dados_para_cadastro):
    """
    Cria uma função polimórfica que usa o método 'cadastrar' de diferentes classes.
    """
    print("---")
    # Usa 'isinstance' para checar o tipo da classe (Polimorfismo por tipo)
    if isinstance(objeto_cadastro, CadastroJogadores):
        # Chama cadastrar com um objeto Jogador
        objeto_cadastro.cadastrar(dados_para_cadastro)
    
    elif isinstance(objeto_cadastro, CadastroAmbiente):
        # Chama cadastrar com os dados do ambiente (espera uma tupla/lista)
        local, terreno, clima, perigo = dados_para_cadastro
        objeto_cadastro.cadastrar(local, terreno, clima, perigo)
    
    else:
        print(f'⚠️ Tipo de cadastro não reconhecido: {type(objeto_cadastro)}')

def iniciar_jogo(jogador1: Jogador, jogador2: Jogador):
    """
    Cria outra função polimórfica que faz os jogadores atacarem e para quando um morre.
    """
    print('\n' + '═'*30)
    print(f'🚨 INÍCIO DO COMBATE: {jogador1.nome} vs {jogador2.nome} 🚨')
    print('═'*30)
    
    # O loop continua enquanto ambos estiverem vivos
    while jogador1.vivo and jogador2.vivo:
        # Polimorfismo: ambos os objetos Jogador usam o mesmo método 'atacar'
        jogador1.atacar(jogador2)
        # Se o jogador2 morreu após o ataque, sai do loop
        if not jogador2.vivo: 
            break
        
        jogador2.atacar(jogador1)
        # Se o jogador1 morreu após o ataque, sai do loop
        if not jogador1.vivo:
            break
        
    print('\n' + '═'*30)
    print('🏆 FIM DO JOGO! 🏆')
    
    # Imprime o resultado final
    if jogador1.vivo:
        print(f'O vencedor é **{jogador1.nome}**! Vidas restantes: {jogador1.qnt_vidas}')
    elif jogador2.vivo:
        print(f'O vencedor é **{jogador2.nome}**! Vidas restantes: {jogador2.qnt_vidas}')
    else:
        print('Empate! Ambos caíram ao mesmo tempo.')
    print('═'*30)


# --- EXECUÇÃO  ---

# 1. Criação de Jogadores
j1 = Jogador('Felipe',"Casagrande",20,1.87,'Guerreiro','Espada', 3,'Corte Poderoso', 35)
j2 = Jogador('Igor',"Shaco",20,1.87,'Mago','Cajado', 2,'Bola de Fogo', 50) 

# 2. Criação dos Cadastros
cadastro_jogadores = CadastroJogadores()
cadastro_ambiente = CadastroAmbiente()

# 3. Cadastro Polimórfico
print("## 📝 TESTE DE CADASTRO POLIMÓRFICO ##")
executar_cadastro(cadastro_jogadores, j1)
executar_cadastro(cadastro_jogadores, j2)

dados_ambiente_1 = ('Caverna do Dragão', 'Subterrâneo', 'Frio/Úmido', 'Extremo')
executar_cadastro(cadastro_ambiente, dados_ambiente_1)


# 4. Mostrar DataFrames
cadastro_jogadores.mostrar_dados()
cadastro_ambiente.mostrar_dados()


# 5. Iniciar o Jogo Polimórfico
iniciar_jogo(j1, j2)