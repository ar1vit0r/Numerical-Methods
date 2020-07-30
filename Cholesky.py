import numpy as np
import math

larg = int(input("Largura: "))
alt = int(input("Altura: "))
matriz_coef = np.zeros((alt,larg),dtype=np.float)
ordem = len(matriz_coef)
print(matriz_coef)
for x in range(alt):
    for y in range(larg):
        matriz_coef[x,y] = int(input("Insira o elemento da \n Linha: " + str(x+1) + " Coluna: " + str(y+1) + ".\n"))
print("\n")
print(matriz_coef)
print("\n")
Det = 1
Info = 0

for j in range(ordem):
    soma = 0
    for k in range(1,j-1):
        soma = soma + (matriz_coef[j,k] * matriz_coef[j,k])
    temp = matriz_coef[j,j] - soma
    if temp > 0:
        matriz_coef[j,j] = math.sqrt(temp)
        r = 1/matriz_coef[j,j]
        Det = Det * temp
    else:
        Info = j
        print("\nA Info é: " + str(Info))
        print("\nMatriz não é definida positiva.\n")
        raise SystemExit
    for i in range(j+1,ordem):
        soma = 0
        for k in range(1,j-1):
            soma = soma + (matriz_coef[i,k] * matriz_coef[j,k])
        matriz_coef[i,j] = (matriz_coef[i,j] - soma) * r

print("\nA matriz é: \n")
print(matriz_coef)
print("\nA matriz transposta é: \n")
print(np.transpose(matriz_coef))
print("\nA Det é: " + str(Det))
print("\nA Info é: " + str(Info))