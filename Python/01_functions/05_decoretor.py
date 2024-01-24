def mi_decorador(func):
    def wrapper(*args, **kwargs):
        print("Antes de la función")
        resultado = func(*args, **kwargs)
        print("Después de la función")
        return resultado
    return wrapper

@mi_decorador
def mi_funcion():
    print("¡Hola, mundo!")

mi_funcion()