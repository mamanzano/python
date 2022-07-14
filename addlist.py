from audioop import add
from itertools import count


def for_add_elements_list(lista):
    for i in range(0,120):
        lista.append(i)
    
    print('Lsita for: ' + '=' * 50)
    print(lista)

def while_add_elements_list(lista):
    count = 0
    while count < 120:
        lista.append(count)
        count = count + 1
    print('\n Lsita while: ' + '=' * 50)
    print(lista)


if __name__ == '__main__':
    lista=[]

    for_add_elements_list(lista)
    while_add_elements_list(lista)