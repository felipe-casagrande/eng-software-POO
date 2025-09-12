from Exercicio_agregação import Chave
from Exercicio_agregação import Car

ch = Chave('Fiat')
ch1 = Chave('Ferrari')

car1 = Car("Uno",1998,'verde',1.0,'SQ007',ch1)
car1.AbrirCarro(ch1)
print(f"Chave ativa: {car1.ativa}")


#vai dar certo
car1.LigarCarro()

#acelera o carro
for i in range(5):
    car1.AcelerarCarro()

#mostrando que nao da pra desligar o carro sem a velocidade ser 0
car1.desligarCarro()

#freiando o carro
for i in range(5):
    car1.FrearCarro()

#desligando o carro
car1.desligarCarro()



