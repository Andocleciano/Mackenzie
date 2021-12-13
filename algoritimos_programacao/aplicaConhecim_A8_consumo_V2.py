
carros = []
consumos = []
consumo_ordenado = []

def entrada_carro():
    i = 0
    for i in range (4):
        carro = input()
        carros.append(carro)
        i += + 1

def entrada_consumo():
    i = 0
    for i in range (4):
        consumo = int(input())
        consumos.append(consumo)
        consumo_ordenado.append(consumo)
        i +=  + 1

def economico():
  i = 0
  consumo_ordenado.sort()
  for i in range (4):
    if (consumo_ordenado[0] == consumos[i]):
        menor_consumo = carros[i]
    i +=  + 1
  return menor_consumo

def main():
  entrada_carro()
  entrada_consumo()
  print(economico())

main()