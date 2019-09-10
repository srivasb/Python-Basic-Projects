'''
Decoradores:
Funcion que recibe una funcion y retorna una funcion

Ejemplo:
funcion protegida por una contrasena
'''

#funcion decorada: protege la funcion a decorar
def protected(func):

    def wrapper(password):
        if password == 'rivas':
            return func()
        else:
            print('invalid password')

    #Regresa la funcion que tiene el trabajo de ejecutar lo que queremos: func()
    return wrapper


#funcion a decorar (se protege por medio de otra funcion @....)
@protected
def protected_function():
    print('password is correct')


if __name__ == '__main__':

    password = str(input('Write password: '))
    protected_function(password)
