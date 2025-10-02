"""
porque pessoa tem velocidade? r = Ainda nao sei
nao entendi pq acelerar e frear tem o parametro pessoa, oq colocar pra elas fazerem? R = Coloquei pra verificar se tem alguem dentro do carro
calcular aceleração? R = Nao entendi
troca de marcha irei colocar até 6 marchas e que o freio é de 5 em 5km e o freio motor tambem de 5 em 5km
bloqueei a troca de marcha para numeros maiores que 6 ou menor que 0, pois 0 seria o neutro.
usei type hynts para ajudar.
inicialmente nao usei a chave em todos os metodos, mas fiquei confuso no todas as operações validam chave correta, entao irei colocar pra verificar a chave em todos os metodos do carro.

"""
from classes import Carro,Chave,Pessoa
ch1 = Chave('aa')
p1 = Pessoa('Felipe','Casagrande',20,1.87,ch1)
carro1 = Carro('aa')

#teste para abrir a porta 
#carro1.porta_aberta = True
#carro1.abrir(ch1.id_chave)
#carro1.abrir(ch1.id_chave)
#p1.abrir_carro(carro1)

#fechar carro
#carro1.fechar(ch1.id_chave)
#1.fechar_carro(carro1)

#ligando carro

#carro1.ligar(p1)
#carro1.desligar(p1)

#entrando no carro
#p1.entrar_carro(carro1)
#p1.entrar_carro(carro1)
#-----------------------------------------------------------------COMANDOS-----------------------------------------------------------------------------
p1.abrir_carro(carro1)
p1.entrar_carro(carro1)
p1.fechar_carro(carro1)
carro1.ligar(p1)
carro1.acelerar(p1)
carro1.trocar_marcha(0)
carro1.acelerar(p1)
carro1.trocar_marcha(1)
carro1.acelerar(p1)
carro1.trocar_marcha(2)
carro1.porta_aberta = False
carro1.acelerar(p1)
carro1.trocar_marcha(1)
carro1.frear(p1)
carro1.frear(p1)
carro1.frear(p1)
p1.sair_carro(carro1)
carro1.desligar(p1)
p1.abrir_carro(carro1)
p1.sair_carro(carro1)
p1.fechar_carro(carro1)
carro1.ver_historico(carro1)
