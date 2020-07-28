import numpy as np

ordem = int(input("Insira a ordem: "))
toler = int(input("Insira a tolerância: "))
iterMax = int(input("Insira o número máximo de iterações: "))
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
termos_ind = []
for x in range(alt):
    termos_ind.append(int(input("Insira o " + str(x+1) + " termo independente: ")))
print("\n")
print(termos_ind)

X = []

for i in range(ordem):
    X.append(termos_ind[i] / matriz_coef[i,i])
Iter = 0
#Iterações de Jacobi
loop = True
vetor = []
while loop:
    Iter+=1
    for i in range(ordem):
        soma = 0
        for j in range(ordem):
            if i != j:
                soma = soma + (matriz_coef[i,j] * X[j])
        vetor.insert(i, ((termos_ind[i] - soma) / matriz_coef[i,i]) ) 
    normaNum = 0
    normaDen = 0
    for i in range(ordem):
        temp = abs(vetor[i] - X[i])
        if temp > normaNum:
            normaNum = temp
        if abs(vetor[i]) > normaDen:
            normaDen = abs(vetor[i])
        X[i] = vetor[i]
    normaRel = normaNum / normaDen
    print("\nO vetor solução é: \n")
    print(X)
    print("\nO Iterador é: " + str(Iter))
    print("\nA NormaRel é: " + str(normaRel))
    #Teste de convergência
    if normaRel <= toler or Iter >= iterMax:
        loop = False
if normaRel <= toler:
    Info = 0
else:
    Info = 1
print("\nA Info é: " + str(Info) + "\n")