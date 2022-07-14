pais = 'México'
continente = 'Americano'

contactos = [
    {
        "nombre" : "Mario",
        "email" : "m@.com"
    },
    {
        "nombre" :"Adriana",
        "email" : "a@.com"
    }
]

print(contactos[0]['nombre'])

print(pais + ' Tipo de dato ' + str(type(pais)))
print(continente + ' Tipo de dato ' + str(type(continente)))

for contacto in contactos:
    print("Nombre del contacto: " + contacto['nombre'])
    print('Email del contacto: ' + contacto['email'])