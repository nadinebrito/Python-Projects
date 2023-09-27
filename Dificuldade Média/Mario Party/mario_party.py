# Mario Party Game 

# Importar Bibliotecas
import numpy as np
import matplotlib.pyplot as plt
import random

# Instructions
print ('Mario Party em Python')

# Personagens: Mario, Luigi, Bowser, Peach, Daisy
lista_de_personagens = ['Mario', 'Diddy Kong', 'Waluigi', 'Boom Boom' ]
print ('Personagens:', lista_de_personagens)


# Crie um caminho
x = [1,1,2,3,4,4,4,5,6,6,6]
y = [1,2,2,2,2,3,4,4,4,5,6]

plt.plot(x,y)

plt.xlim(0,7)
plt.ylim(0,7)
plt.title('Mario Party Game Board')

# Comece em uma base
plt.scatter(x[0], y[0], c='green',s=200, marker="^")

# Crie a linha de chegada
plt.scatter(x[-1], y[-1], c='yellow',s=200, marker="^")

# Plotar a lista de personagens
lista_de_cores  = ['red','blue','magenta','orange']

# Pintando os personagens
plt.scatter(x[0] - 0.1, y[0]  - 0.1 , c=lista_de_cores[0],s=50, marker="o")
plt.scatter(x[0] - 0.2 , y[0] - 0.1 , c=lista_de_cores[1],s=50, marker="o")
plt.scatter(x[0] - 0.3, y[0] - 0.1 , c=lista_de_cores[2],s=50, marker="o")
plt.scatter(x[0] - 0.4, y[0] - 0.1 , c=lista_de_cores[3],s=50, marker="o")

# Plotando o mapa
plt.savefig('CaminhoOriginal.png')

# Crie a o dado
tamanho_dado = 6

# Comece o jogo com o Mario
dado_mario = random.randint(1,tamanho_dado)
plt.scatter(x[dado_mario], y[dado_mario], c=lista_de_cores[0],s=50, marker="o")
plt.title('Primeira jogada do Mario, dado sorteou: ' + str(dado_mario))
plt.savefig('Primeira jogada do Mário')

# Continue o jogo com o Diddy Kong
dado_diddy = random.randint(1,tamanho_dado)
plt.scatter(x[dado_diddy], y[dado_diddy], c=lista_de_cores[1],s=50, marker="o")
plt.title('Primeira jogada do Diddy Kong, dado sorteou: ' + str(dado_diddy))
plt.savefig('Primeira jogada do Diddy Kong')

# Continue o jogo com o Waluigi
dado_waluigi = random.randint(1,tamanho_dado)
plt.scatter(x[dado_waluigi], y[dado_waluigi], c=lista_de_cores[2],s=50, marker="o")
plt.title('Primeira jogada do Waluigi, dado sorteou: ' + str(dado_waluigi))
plt.savefig('Primeira jogada do Waluigi')

# Continue o jogo com o Boom Boom
dado_boom = random.randint(1,tamanho_dado)
plt.scatter(x[dado_boom], y[dado_boom], c=lista_de_cores[3],s=50, marker="o")
plt.title('Primeira jogada do Boom Boom, dado sorteou: ' + str(dado_boom))
plt.savefig('Primeira jogada do Boom Boom')


# Determinar vencedores