from modelos import coche



if __name__ == '__main__':
    
    auto = coche.Coche()

    auto.set_color('amarillo')
    auto.set_marca('WV')
    auto.set_modelo('Jetta')
    auto.set_puertas(5)

    print(auto.get_color())
    print(auto.get_marca())
    print(auto.get_modelo())

    auto.acelelar()
    auto.acelelar()

    print(auto.get_velocidad())

    print('*' * 50)
    auto.get_info()