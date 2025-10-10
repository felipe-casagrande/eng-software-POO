class Fruta:
    def __init__(self,tipo):
        self.tipo = tipo
        self.madura = False

    def amadurecer(self):
        if not self.madura:
            self.madura = True
            return "Fruta Amadurecida com sucesso!"
        else:
            return "A fruta ja esta madura!"
        

class Pessoa:
    def __init__(self,nome,idade,altura):
        self.nome = nome
        self.idade = idade
        self.altura = altura
        self.fruta = None

    def __str__(self):
        return f"Nome: {self.nome}\nIdade: {self.idade}\nAltura: {self.altura}"    
    
    def apres_unidade(self,curso):
        return f'''Olá, me chama {self.nome} e faço o curso de {curso} na Universidade de Vassouras!'''

    def pegar_fruta(self,fruta:Fruta):
        if self.fruta == None:
            self.fruta = fruta
            self.fruta.amadurecer()
            return f'''A fruta {self.fruta.tipo} foi pega pelo {self.nome} e ela esta {'madura' if self.fruta.madura else 'verde'}
            '''    
        else:
            return f"{self.nome} já tem a fruta {self.fruta.tipo}, nao pode pegar a {fruta.tipo}"
           

p1 = Pessoa('felipe',20,1.87)
print(p1)
print(p1.apres_unidade('Engenharia de software'))

f1 = Fruta('maça')
f2 = Fruta('Banana')
print(p1.pegar_fruta(f1))        
print(p1.pegar_fruta(f2))        