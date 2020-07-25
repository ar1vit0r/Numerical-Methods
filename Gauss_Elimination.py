import numpy as np
#ESCALONAMENTO

larg = int(input("Largura: "))
alt = int(input("Altura: "))
matriz_coef = np.zeros((larg, alt),dtype=np.float)
print(matriz_coef)
for x in range(larg):
    for y in range(alt):
        matriz_coef[x,y] = int(input())
print(matriz_coef)

ordem = int(input("Insira a Ordem: "))

termos_ind = []
for x in range(alt):
    termos_ind.append(int(input("Insira o " + str(x+1) + " termo: ")))
print(termos_ind)

Det = 1
Info = 0

for j in range(ordem-1):
    #escolha do pivô
    pivo = j
    matriz_coef_max = abs(matriz_coef[j,j])
    k = j+1 # talvez dê problema
    for k in range(ordem):
        if abs(matriz_coef[k,j]) > matriz_coef_max:
            matriz_coef_max = abs(matriz_coef[k,j])
            pivo = k
    if pivo != j:
        for k in range(ordem):
            temp = matriz_coef[j,k]
            matriz_coef[j,k] = matriz_coef[pivo,k]
            matriz_coef[pivo,k] = temp
        temp = termos_ind[j]
        termos_ind[j] = termos_ind[pivo]
        termos_ind[pivo] = temp
        Det = Det*-1
    Det = Det*matriz_coef[j,j]
    #eliminação de gauss
    if abs(matriz_coef[j,j]) != 0:



