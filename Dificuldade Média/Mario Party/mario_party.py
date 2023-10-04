# Mario Party Game 

# Importar Bibliotecas
import numpy as np
import matplotlib.pyplot as plt
import random

# Instructions
print ('Mario Party em Python')

# Personagens
lista_de_personagens = ['Mario', 'Diddy Kong', 'Waluigi', 'Boom Boom' ]

lista_de_pontos = [0, 0, 0, 0]

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

# Determinar vencedor
def fimDeJogo(pts):
    if (pts == 10):
        return True
    else:
        return False

# Crie a o dado
tamanho_dado = 6        

# Jogada Individual
def jogada(pers, cor,pontos, cont):

    dado = random.randint(1,tamanho_dado)

    
    if (pers=='Mario'):
        pts = pontos[0]
        pts = pts + dado
        pontos[0] = pts

    if (pers=='Diddy Kong'):
        pts = pontos[1]
        pts = pts + dado
        pontos[1] = pts

    if (pers=='Waluigi'):
        pts = pontos[2]
        pts = pts + dado
        pontos[2] = pts

    if (pers=='Boom Boom'):
        pts = pontos[3]
        pts = pts + dado
        pontos[3] = pts

    if(pts > 10):
        pts = 10
    
    
    plt.scatter(x[pts], y[pts], c=cor,s=50, marker="o")
    
    
    plt.title('{a}ª jogada: {b} jogou o dado e sorteou: {c}'.format(a=cont, b=pers, c=dado))
    plt.savefig('{a}ª jogada'.format(a=cont))

    chegada = fimDeJogo(pts)

    return chegada
    
# Ordem das Jogadas
def ordemDeJogada(personagem, cor,pts):
    cont = 1
    game = True
    while game:
        for a,b in zip(personagem, cor):
            chegada = jogada(a,b,pts,cont)
            if chegada == False:
                cont+=1
            else:
                print("Fim de Jogo") 
                game = False 
                return    

ordemDeJogada(lista_de_personagens, lista_de_cores,lista_de_pontos)