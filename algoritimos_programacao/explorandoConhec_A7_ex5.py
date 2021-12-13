# Programa que conta a quantidade de divisores de um numero inteiro e positivo

# Sem modularização
#Validando a dado se entra:
#n = -1
#while n<=0:
   # n = int(input('Digite um número inteiro e positivo'))

# Contando os dividores do número lido
#ndiv = 0
#for cont in range (1, n+1):
    #resto = n%cont
    #if resto == 0:
        #ndiv += +1

    #Modularizado com funções:
    
def  entrada ():
    n = -1
    while n<0:
        n = int(input("Digite um numero inteiro e positivo:"))
    return n

def conta_divisor (n):
    ndiv = 0
    for cont in range (1, n+1):
        resto = n%cont
        if resto == 0:
            ndiv =+ 1
    return ndiv

def main():
    n = entrada()
    print (conta_divisor(n))

main()        
        
