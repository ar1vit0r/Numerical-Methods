import numpy as np
import math

larg = int(input("Largura: "))
alt = int(input("Altura: "))
ordem = int(input("Insira a Ordem: "))
matriz_coef = np.zeros((alt,larg),dtype=np.float)
print(matriz_coef)
for x in range(larg):
    for y in range(alt):
        matriz_coef[x,y] = int(input("Insira o elemento da \n Linha: " + str(x+1) + " Coluna: " + str(y+1) + ".\n"))
print(matriz_coef)

Det = 1
Info = 0

for j in range(ordem-1):
    soma = 0
    for k in range(j-1):
        soma = soma + (matriz_coef[j,k] * matriz_coef[j,k])
    temp = matriz_coef[j,j] - soma
    if temp > 0:
        matriz_coef[j,j] = math.sqrt(temp)
        r = 1/matriz_coef[j,j]
        Det = Det * temp
    else:
        Info = j
        print("\nMatriz não é definida positiva.\n")
        raise SystemExit
    for i in range(j+1,ordem-1):
        soma = 0
        for k in range(j-1):
            soma = soma + (matriz_coef[i,k] * matriz_coef[j,k])
        matriz_coef[i,j] = (matriz_coef[i,j] - soma) * r

print("\nA matriz é: \n")
print(matriz_coef)
print("\nA Det é: " + str(Det))
print("\nA Info é: " + str(Info))
