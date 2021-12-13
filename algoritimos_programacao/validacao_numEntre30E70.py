num = float(input('Digite um número entre 30 e 70: '))
while num <=30 or num >=70:
    #if num <= 30 or num >=70: - essa linha ao meu entendimento não faz sentido.
    print('Valor invalido. Digite novamente: ')
    num = float(input('Digite um número entre 30 e 70: '))
print('número válido')    