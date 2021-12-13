# Escreva uma função que receba dois números e retorne True se o primeiro número for múltiplo do segundo.

def multiplo (a, b):
    if a % b == 0:
        return True
    return False

def entrada ():
    n = int (input ('Digite um numero:'))
    return n

def main ():
    x = entrada ()
    y = entrada ()
    print (multiplo (x, y))

main()    