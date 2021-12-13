# escreva uma função que retorno o maior de dois números.

def maximo (n1, n2):
    if n1 > n2:
        return n1
    return n2

def entrada ():
    n = int (input ('Digite um número: '))
    return n

def main ():
    x = entrada ()
    y = entrada ()
    print ('O maior número é:', maximo (x, y))

main()
