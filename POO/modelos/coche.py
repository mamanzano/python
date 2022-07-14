class Coche:
    __color = ''
    __marca = ''
    __modelo = ''
    __puertas = ''
    __velocidad = 0

    def __init__(self) -> None:
        self.__velocidad = 120

    def set_color(self, color):
        self.__color = color
    
    def get_color(self):
        return self.__color

    def set_marca(self, marca):
        self.__marca = marca
    
    def get_marca(self):
        return self.__marca

    def set_modelo(self, modelo):
        self.__modelo = modelo

    def get_modelo(self):
        return self.__modelo

    def set_puertas(self, puertas):
        self.__puertas = puertas

    def get_puertas(self):
        return self.__puertas

    def set_velocidad(self, velocidad):
        self.__velocidad = velocidad

    def get_velocidad(self):
        return self.__velocidad

    def acelelar(self):
        self.__velocidad += 1
    
    def frenar(self):
        self.__velocidad -= 1

    def get_info(self):
        
        info = ' marca: ' + self.__marca
        info += '\n modelo: ' + self.__modelo
        info += '\n color: ' + self.__color
        info += '\n velocidad: ' + str(self.__velocidad)

        print(info)