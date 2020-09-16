# DECLARANDO FUNCIONES ARITMETICAS

def suma (a,b):
    '''

    Function to add

    Parameters: a,b

    return a+b
    '''
    y = a + b
    return y

def resta (a,b):
    '''

    Function to substract

    Parameters: a,b

    return a-b
    '''
    y = a - b
    return y

def multiplicacion (a,b):
    '''

    Function to multiply

    Parameters: a,b

    return a*b
    '''
    y = a * b
    return y

def division (a,b):

    '''
    Function to divide

    Parameters: a,b

    return a / b
    '''
    if b != 0:
        y = a / b
        return y
    raise ZeroDivisionError('ERROR: Division entre 0 on permitida, verifique su error')
        
def potencia (a,b):
    '''

    Function to pow

    Parameters: a,b

    return a ** b
    '''
    y = a ** b
    return y

def raiz_cuadrada(a):
    '''
    Function to sqrt

    Parameters: a

    return a ** 0.5

    '''
    y = a ** 0.5
    return y

