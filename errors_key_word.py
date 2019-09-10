# -*- coding: utf-8 -*-

PAISES = {
    'colombia':49,
    'mexico':122,
    'chile': 18,
}

def run():

    while True:

        pais = str(input('Ingrese nombre de pais: ')).lower()

        try:
            print(f'El pais {pais} tiene {PAISES[pais]} millores de habitantes.')
        except KeyError:
            print(f'No hay informacion de {pais}.\n')
            num = int(input(f'ingrese numero en millores de habitantes de {pais}:  '))
            if pais not in PAISES.items():
                PAISES[pais] = num
            print(f'La nueva base de datos es: {PAISES}.')


        result = str(input('''
                [Y]es si desea salir
                [N]o si no desea salir

                opcion:  '''  )).upper()
        if result == 'Y':
            break
    print('')

if __name__ == '__main__':
    run()
