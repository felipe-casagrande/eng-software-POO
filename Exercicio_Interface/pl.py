from abc import ABC, abstractmethod

# Classe base Pessoa
class Pessoa(ABC):
    def _init_(self, nome, sobrenome, idade, altura, vida=100, vivo=True):
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade
        self.altura = altura
        self.vida = vida
        self.vivo = vivo

    @abstractmethod
    def falar(self):
        pass

    @abstractmethod
    def andar(self):
        pass

    @abstractmethod
    def parar(self):
        pass


# Classe Jogador herdando de Pessoa
class Jogador(Pessoa):
    def _init_(self, nome, sobrenome, idade, altura, tipo, arma, ataque_nome, ataque_dano):
        super()._init_(nome, sobrenome, idade, altura)
        self.tipo = tipo
        self.arma = arma
        self.ataque_nome = ataque_nome
        self.ataque_dano = ataque_dano

    # Implementando métodos abstratos
    def falar(self):
        print(f"{self.nome} diz: Estou pronto para a batalha!")

    def andar(self):
        print(f"{self.nome} está andando.")

    def parar(self):
        print(f"{self.nome} parou de andar.")

    # Método atacar
    def atacar(self, outro):
        if self.vivo and outro.vivo:
            print(f"{self.nome} usa {self.ataque_nome} em {outro.nome} causando {self.ataque_dano} de dano.")
            outro.vida -= self.ataque_dano
            if outro.vida <= 0:
                outro.vivo = False
                print(f"{outro.nome} morreu!")
        else:
            print("Ataque inválido, alguém está morto.")


# Classe para cadastro de jogadores
class CadastroJogadores:
    def _init_(self):
        self.jogadores = []

    def cadastrar(self, jogador):
        self.jogadores.append(jogador)
        print(f"Jogador {jogador.nome} cadastrado.")

    def listar(self):
        for j in self.jogadores:
            status = "Vivo" if j.vivo else "Morto"
            print(f"{j.nome} ({j.tipo}) - Vida: {j.vida} - {status}")


# Classe para o ambiente do jogo
class CadastroAmbiente:
    def _init_(self, nome):
        self.nome = nome
        self.jogadores = []

    def adicionar_jogador(self, jogador):
        self.jogadores.append(jogador)
        print(f"{jogador.nome} entrou no ambiente {self.nome}.")


# Funções polimórficas
def cadastrar_jogadores(objeto_cadastro, lista_jogadores):
    for jogador in lista_jogadores:
        objeto_cadastro.cadastrar(jogador)


def iniciar_jogo(ambiente):
    print("\n--- Iniciando o jogo ---")
    vivos = [j for j in ambiente.jogadores if j.vivo]
    while len(vivos) > 1:
        atacante = vivos[0]
        alvo = vivos[1]
        atacante.atacar(alvo)
        vivos = [j for j in ambiente.jogadores if j.vivo]

    if vivos:
        print(f"\nFim do jogo! O vencedor é {vivos[0].nome}.")
    else:
        print("Todos os jogadores morreram!")


# ======= Exemplo de uso =======
if _name_ == "_main_":
    j1 = Jogador("Arthur", "Silva", 22, 1.80, "Guerreiro", "Espada", "Golpe Forte", 30)
    j2 = Jogador("Bruna", "Souza", 25, 1.65, "Arqueira", "Arco", "Flecha Rápida", 25)

    cadastro = CadastroJogadores()
    cadastrar_jogadores(cadastro, [j1, j2])

    ambiente = CadastroAmbiente("Campo de Batalha")
    ambiente.adicionar_jogador(j1)
    ambiente.adicionar_jogador(j2)

    j1.falar()
    j2.falar()

    iniciar_jogo(ambiente)