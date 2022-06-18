opc = 1
cont = 1
numeros = []

print('MENÚ DEL PROGRAMA')
print('1. 5 numeros enteros')
print('2. Suma de numeros ')
print('3. Agregar numero')
print('4. Salir')

while (opc != 4):
    opcion = int(input('Digite una opción: '))
    if (opc == 1):
        while (cont <= 5):
            numero = int(input('Digite un numero: '))
            numeros.append(numero)
            print(numeros)
            cont += 1
    elif (opc == 2):
        suma = sum(numeros)
        print(f'La suma es: {suma}')
    elif (opc == 3):
        numero = int(input('Digite un nuevo nuevo: '))
        numeros.append(numero)
        print(numeros)
    elif (opc == 4):
        print(' digite 4 para salir')
    else:
        print(' Opcion incorrecta')
else:
    print('---------------------------------------')
    print('Saliste del programa.')