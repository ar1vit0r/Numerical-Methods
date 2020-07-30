import numpy as np
import copy
import math

def laplace(A): ### Adaptado das notas de aula do Prof. Daniel Cajueiro (curso de métodos computacionais, Universidade de Brasília, 2017/1)
    n=np.shape(A)[0]
    if(n==1):
        det=A
    elif(n==2):
        det=A[0,0]*A[1,1]-A[0,1]*A[1,0]
    else:
        det=0
    for i in range(n):
        newMatrix=A[1:,:]
        newMatrix=np.delete(newMatrix,i,axis=1)
        det=det+math.pow(-1,1+i+1)*A[0,i]*(laplace(newMatrix))
    return det

def LU(x):
    dim=np.shape(x) # dimensões da matriz (linhas/colunas)
    det=1 # elemento neutro da multiplicação
    lower=np.identity(dim[0])  # começa-se pela matriz identidade para a matriz L
    for j in range(0,dim[1]):
        for i in range(j,dim[0]):  # eliminação de Gauss
            if(i == j and x[i,j]==0 and i!=dim[1]-1):  # permutação de linhas para deixari pivô diferente de zero
                p=-2  # contador provisório
                k=i
                while p!=k and k<dim[1]-1: # trocar linha pivô por outra que tenha elemento não nulo na coluna pivô
                    if x[k,j]!=0:
                        p=k # identifica primeira linha com coluna pivô não nula
                    else:
                        k+=1
                if p==-2: # caso não tenha (ou seja, coluna inteira nula), a matriz é singular
                    return("Determinante = 0 (Matriz singular)")
                else:
                    x[i,],x[p,]=x[p,].copy(),x[i,].copy() # permutação de linhas
                    det=(-1)*det # trocar sinal do determinante (pela propriedade)
            elif(i!=j): # com o pivô não-nulo:
                xt0=x[j,j] 
                xt1=x[i,j]
                ft=xt1/xt0
                x[i,:]=x[i,:]-x[j,:]*ft # operação-linha número 3
                lower[i,j]=ft # o fator que multiplica a outra linha é atribuída à matriz L - não se troca o sinal pois a operação já é de substração
        det=det*x[j,j] # após zerar todos os elementos abaixo do elemento pivô na respectiva coluna, agrupar o elemento da diagonal principal ao determinante - ao final de todas as colunas, o número resultante será o produtório de todos os elementos dessa diagonal, e portanto o determinante da matriz original (por construção, a matriz identidade de L será sempre 1)
    print ("U=" + x)
    print ("L=" + lower)
    print ("LU = " + np.dot(lower,x) + "= X")
    print ("Determinante = " + det)