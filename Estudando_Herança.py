class Animal:
    def __init__(self,nome):
        self.nome = nome

    def fazer_som_animal(self):
        raise NotImplementedError("Crie um som pra o animal")

class cachorro(Animal):
    def __init__(self,nome,idade):
        super().__init__(nome)
        self.idade = idade

    def fazer_som_animal(self):
        return 'auau'
class gato(Animal):
    def __init__(self, nome,cor):
        super().__init__(nome)
        self.cor = cor
    def fazer_som_animal(self):
        return "miau"




cachorro1 = cachorro('Tommy',10)
cachorro2 = cachorro("felipe",20)
print(f"O cachorro  {cachorro1.nome} tem {cachorro1.idade} anos! Ele faz {cachorro1.fazer_som_animal()}, que cachorro velho!")
gato1 = gato('Akali',"ruiva")
print(f"A gata {gato1.nome} é {gato1.cor}! Ela faz {gato1.fazer_som_animal()}, que gata linda!")
