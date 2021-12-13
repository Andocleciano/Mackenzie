#Faça um programa modularizado em Python, para resolver um problema usando listas.  

#O programa deve ter as seguintes funções: 

# - entrada_carro(): faz a entrada do modelo de quatro carros via teclado (o usuário digitará o modelo de quatro carros); 
# - entrada_consumo(): faz a entrada de um número inteiro que é o consumo (em litros) de cada modelo de carro por quilometro (o usuário digita o consumo correspondente a cada carro); 
# - economico(): retorna o modelo do carro mais econômico. Observe que o modelo do carro e seu consumo estará na mesma posição na lista, porém em vetores diferentes (carro e consumo). 

#A entrada de dados deve ser feita da seguinte forma: 

# - O usuário digitará o modelo de cada um dos quatro carros, linha por linha, seguidas uma da outra. 
# - O usuário digitará o consumo de cada um dos quatro carros, linha por linha. 

#O programa apresentará, na tela, o modelo do carro que tiver o menor valor de consumo. 

carros = []
consumo = []
consumo_ordenado = []

def entrada_carro():
  i = 0
  while i  < (4):
    novoCarro = input()
    carros.append(novoCarro)
    i += + 1

def entrada_consumo():
  i = 0
  while i < (4):
    novoConsumo = int(input())
    consumo.append(novoConsumo)
    consumo_ordenado.append(novoConsumo)
    i +=  + 1

def economico():
  i = 0
  consumo_ordenado.sort()
  while i < (4):
    if (consumo_ordenado[0] == consumo[i]):
      maisEconomico = carros[i]
      break
    i +=  + 1
  return maisEconomico

def main():
  entrada_carro()
  entrada_consumo()
  print(economico())

main()