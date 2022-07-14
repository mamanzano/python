def convert_mayus(variable):
    #
    variable = variable.upper()
    return variable

def prove_var(variable):
    if variable == '':
        variable = 'que paso padrino, eres tu'
        variable = convert_mayus(variable)
    else:
        variable = 'la variable tiene contenido'
    return variable

if __name__ == '__main__':
    text = 'll'

    text = prove_var(text)
    print(text)
    