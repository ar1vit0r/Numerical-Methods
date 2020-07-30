import numpy as np
#ESCALONAMENTO

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
termos_ind = []
for x in range(alt):
    termos_ind.append(int(input("Insira o " + str(x+1) + " termo independente: ")))
print("\n")
print(termos_ind)

Det = 1
Info = 0

for j in range(ordem):
    #escolha do pivô
    pivo = j
    matriz_coef_max = abs(matriz_coef[j,j])
    for k in range(j+1,ordem):
        if abs(matriz_coef[k,j]) > matriz_coef_max:
            matriz_coef_max = abs(matriz_coef[k,j]) 
            pivo = k
    if pivo != j: #troca linhas
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
        r = 1/matriz_coef[j,j]
        for i in range(j+1,ordem):
            mult = matriz_coef[i,j]*r
            matriz_coef[i,j] = 0
            for k in range(j+1,ordem):
                matriz_coef[i,k] = matriz_coef[i,k] - (mult*matriz_coef[j,k])
            termos_ind[i] = termos_ind[i] - (mult*termos_ind[j])
    else:
        if Info == 0:
            Info = j
Det = Det * matriz_coef[ordem-1,ordem-1]
if Info == 0 and abs(matriz_coef[ordem-1,ordem-1]) == 0:
    Info = ordem

print("\nA matriz é: \n")
print(matriz_coef)
print("\nA Determinante é: " + str(Det))
print("\nO vetor transformado é: \n")
print(termos_ind)
print("\nA Info é: " + str(Info))