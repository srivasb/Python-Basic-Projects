#Reed a .txt file

def run():

    strg = 'she'
    cont = 0
    i = 0

    with open('The_Story_of_an_Hour.txt') as f:
        for line in f.readlines():
            cont += line.count(strg)
            print(f'cont = {cont}, line number= {i}')
            i+=1

        print(f'\nNumero de {strg} en .txt = {cont}, y un total de {i} lineas.\n')



if __name__ == '__main__':
    run()
