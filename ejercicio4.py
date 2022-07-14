def ordenar_tabla(tabla):
    for categoria in tabla:
        print('*' * 10 + categoria['categoria'] + '*' * 10)
        for juego in categoria['juegos']:
            print(f'Juego: {juego}')

if __name__ == '__main__':
    tabla = [
        {
            "categoria" : 'ACCIÓN',
            "juegos": ["GTA","CALL OF DUTY"]
        },
        {
            "categoria" : "AVENTURA",
            "juegos" : ["COD","CRASH","PRINCE OF PERCIA"]
        },
        {
            "categoria" : "DEPORTES",
            "juegos" : ['FIFA 21','PRO21','MOTO GP 21']
        }
    ]

    ordenar_tabla(tabla)