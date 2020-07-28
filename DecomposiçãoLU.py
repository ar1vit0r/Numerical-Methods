import numpy as np

larg = int(input("Largura: "))
alt = int(input("Altura: "))
matriz_coef = np.zeros((alt,larg),dtype=np.float)
print(matriz_coef)
for x in range(larg):
    for y in range(alt):
        matriz_coef[x,y] = int(input("Insira o elemento da \n Linha: " + str(x+1) + " Coluna: " + str(y+1) + ".\n"))
print("\n")
print(matriz_coef)
print("\n")
Pivot = []
for i in range(1,alt):
    Pivot.append(i)
print(Pivot)
Pdu = 1
Info = 1
for j in range(min(alt-1,larg-1)):
    #Escolhe pivô
    pivo = j
    matriz_coef_max = abs(matriz_coef[j,j])
    for k in range(j+1,alt-1):
        if abs(matriz_coef[k,j]) > matriz_coef_max:
            matriz_coef_max = abs(matriz_coef[k,j])
            pivo = k
    if pivo != j:
        #troca de linhas
        for k in range(larg-1):
            temp = matriz_coef[j,k]
            matriz_coef[j,k] = matriz_coef[pivo,k]
            matriz_coef[pivo,k] = temp
        temp = Pivot[j]
        Pivot[j] = Pivot[pivo]
        Pivot[pivo] = temp
        Pdu = Pdu * -1
    Pdu = Pdu * matriz_coef[j,j]
    #eliminação de gauss
    if abs(matriz_coef[j,j]) != 0:
        r = 1/matriz_coef[j,j]
        for i in range(j+1,alt-1):
            mult = matriz_coef[i,j] * r
            matriz_coef[i,j] = mult
            for k in range(j+1,larg-1):
                matriz_coef[i,k] = matriz_coef[i,k] - (mult * matriz_coef[j,k])
    else:
        if Info == 0:
            Info = j

print("\nA matriz é: \n")
print(matriz_coef)
print("\nO vetor pivot é: \n")
print(Pivot)
print("\nA Pdu é: " + str(Pdu))
print("\nA Info é: " + str(Info))