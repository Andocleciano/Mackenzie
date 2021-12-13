nome = ['Ana', 'Marcos', 'Roberto', 'Joao']
print (nome[1])
print ('Antes: ', nome)
nome[2] = 'Carlos'
print ('Depois:' ,nome)
nome.insert(2, 'Aline')
print ('Depois de inserir: ', nome)
nome.append('Maria')
nome.append('Beatriz')
print ('Depois do append: ', nome)
del nome[3]
print('Depois de apagar item 3: ', nome)
nome.sort()
print('Lista dos nomes em ordem crescente: ', nome)
nome.reverse()
print('Lista dos nomes em ordem decrescente: ', nome)