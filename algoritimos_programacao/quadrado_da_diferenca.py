''' Faça um programa em Python que leia dois números inteiros e exiba o quadrado da diferença do primeiro valor pelo segundo. '''

'''n1 = int(input(''))
n2 = int(input(''))
resp = (n1-n2)*(n1-n2)
print('%.1f' % resp)'''

#Resposta do autor:
import math
a= int(input())
b= int(input())
res = math.pow(a-b,2)
print(res)