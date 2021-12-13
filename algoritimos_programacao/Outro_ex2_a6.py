num=0
soma=0

num=int(input())

while num <=0:
    print('VALOR INVÁLIDO')
    num=int(input())

for cont in range(1,num+1):
   if num % cont ==0:
    soma += cont
    print(cont, end=" ")




