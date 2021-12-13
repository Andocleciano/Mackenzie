tabuada = int(input('Montar a tabuada de: '))

while True:
  inicio = int(input('Começar por: '))
  termino = int(input('Terminar em: '))
  if(inicio > termino):
    print('Você digitou o valor final menor que o inicial! Digite novamente.')
  else:
    break
  

for fator in range(inicio, termino + 1):
  print(f'{tabuada} x {fator} = {tabuada*fator}')