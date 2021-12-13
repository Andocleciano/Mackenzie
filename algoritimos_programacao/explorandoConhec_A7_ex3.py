def area_quadrado (lado):
    return lado ** 2

def entrada ():
    lado =float(input('Lado:'))
    return lado

def main ():
    l = entrada ()
    a = area_quadrado (l)
    print ('Área = ', a)

main()