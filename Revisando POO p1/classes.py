class Fruta:
    def __init__(self,tipo):
        self.tipo = tipo
        self.madura = False

    def amadurecer(self):
        if not self.madura:
            self.madura = True
            return "Fruta amadurecida com sucesso!"
        else:
            return "A fruta ja esta madura"



class Pessoa:
    def __init__(self,nome,idade,altura):
        self.nome = nome
        self.idade = idade
        self.altura = altura
        self.fruta = None

    def  __str__(self):
        return f'Meu nome é {self.nome}, tenho {self.idade} anos de idade e tenho {self.altura} de altura!'
    
    def apre_unidade(self,curso):
        return f''' Olá, me chamo {self.nome}, e faço o curso {curso} na Universidade de Vassouras! 

        '''
    
    def pegar_fruta(self,fruta:Fruta):
        if self.fruta == None:
            self.fruta = fruta
            self.fruta.amadurecer()
            return f''' A fruta {fruta.tipo} foi pega pelo {self.nome}. A {self.fruta.tipo} esta {'madura' if self.fruta.madura else "verde"}
            '''
        else:
            return f"{self.nome} ja esta com a fruta {self.fruta.tipo}, nao pode pegar {fruta.tipo}"



    



p1 = Pessoa('felipe',10,20)

f1 = Fruta('maça')
print(p1)
print(f1.tipo)
f1.amadurecer()
f1.amadurecer()
print(p1.pegar_fruta(f1))

f2 = Fruta("banana")
f2.amadurecer()
print(p1.pegar_fruta(f2))

print(p1.apre_unidade("engenharia de software"))