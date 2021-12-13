resultado = []
def dados(n):
    a=0
    b=1

    while a<n:
        resultado.append(a)
        a=b
        b=a+b
def main():
    dados(100)
    print (resultado)
main()