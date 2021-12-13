'''Faça um programa em Python que resolva o seguinte problema: 

Um concurso possui um prêmio no montante de R$ 780.000,00 para dividir entre três ganhadores da seguinte forma: 

- o primeiro ganhador receberá 46% do prêmio; 
- o segundo ganhador receberá 32% do prêmio; 
- o terceiro ganhador receberá o restante do prêmio. 

Calcule e mostre o valor do prêmio de cada ganhador. 

Observe que este programa não tem valor de entrada feita pelo usuário. '''

vTotal = 780000.00
pGan = (vTotal*46)/100
sGan = (vTotal*32)/100
tGan = vTotal-pGan-sGan

print(pGan)
print(sGan)
print(tGan)