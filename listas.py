def ordenar_lista(lista):
    lista.sort()
    return lista

def recorrer_lista(lista):
    suma = 0
    for element in lista:
        suma = suma + element

    print('La suma de los números de la lista es: ' + str(suma))

def encontrar_num(num):
    numeros = [89,52,2,45,32,20,45,12,65]
    encontrado = False
    for numero in numeros:
        if(numero == int(num)):
            encontrado = True
            break
    if encontrado == True:
        print('El número: ' + num + ' se encuentra en la lista')
    else:
        print('No se escontro el número: ' + num + ' en la lista')

if __name__ == '__main__':
    numeros = [89,52,2,45,32,20,45,12]

    lista_ordenada = ordenar_lista(numeros)

    for numero in lista_ordenada:
        print('Numero: ' + str(numero))  
    
    print('Longitud de la lista: ' + str(len(lista_ordenada)))

    recorrer_lista(numeros)

    encontrar = input(print('Escribe un número para buscar'))

    encontrar_num(encontrar)