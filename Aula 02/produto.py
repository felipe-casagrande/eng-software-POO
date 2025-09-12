# Classe --> Rica
class Produto:
    # Método contrutor
    def __init__(self, nome, preco, quantidade):
        # Atributos
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade
    
    # Método de apresentação
    def apresentacao(self):
        print(
    f"""
Produto  armazenados:
Produto {self.nome} esta R${self.preco} e temos 
{self.quantidade} quantidade
    """
    )

# criando objetos
leite = Produto("Leite", 7.99, 10)
maca = Produto("Maça", 0.99, 15)
agua = Produto("Água", 1.99, 20)

# Se eu quiser realizar a apresentação dos itens dessa classe
# Apresentando objetos
print(
    f"""
Esses são os produtos  armazenados até o momento:
Produto 1 {leite.nome} esta R${leite.preco} e temos 
{leite.quantidade} quantidade

Produto 2 {maca.nome} esta R${maca.preco} e temos 
{maca.quantidade} quantidade

Produto 3 {agua.nome} esta R${agua.preco} e temos
{agua.quantidade} quantidade
    """
)