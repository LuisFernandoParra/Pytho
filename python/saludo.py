import sys
print(sys.argv)

if (len(sys.argv) < 3) or (len(sys.argv) > 3):
    print("no alcanzan los argumentos")
    exit()
elif len(sys.argv) == 3:
    numero_1 = int(sys.argv[1])
    numero_2 = int(sys.argv[2])
    if (numero_1 < 0 or numero_1 > 10) or (numero_2 < 0 or numero_2 > 10):
        print("error")
    elif (numero_1 >= 7) and (numero_2 >= 7):
        print("promocionado")
    elif (numero_1 >= 4) and (numero_2 >= 4):
        print("Aprobado, debe rendir final")
    elif (numero_1 < 4) or (numero_2 < 4): 
        if numero_1 ==3:
            print("Debe recuperar el primer parcial")
        else:
            print("Debe recuperar el segundo parcial")
    elif (numero_1 < 4) and (numero_2 < 4):
        print("Desaprobo ambos parciales, debe recursar")