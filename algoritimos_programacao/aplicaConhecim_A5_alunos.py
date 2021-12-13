total_alunos = int(input())
if total_alunos != 0:
    cont = 0
    nota_total = 0
    while cont < total_alunos:
        media_aluno = float(input())
        if media_aluno >= 6.0:
            print('PARABÉNS VOCÊ ESTÁ APROVADO')
        cont += 1
        nota_total += media_aluno
    media_total = nota_total/total_alunos
    print (media_total)
else:
    print('NÃO HOUVE PROCESSAMENTO')
