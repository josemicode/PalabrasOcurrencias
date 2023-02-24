import collections
import os


def contar_ocurrencias(string, lista):
    dict = {}
    for i in lista:
        aux = string.count(i)
        dict.update({i: aux})
    return dict


def contar_ocurrencias_archivo(path, lista):
    existe = os.path.exists(path)
    if existe:
        file = open(path, 'r')
        lectura = file.read()
        res = contar_ocurrencias(lectura, lista)
        return res
    else:
        print("La ruta especificada no conduce a ningún archivo")


if __name__ == '__main__':
    lista1 = ["me", "a", "en"]
    dict = contar_ocurrencias("Yo me niego a participar en la revuelta del viernes en la plaza.", lista1)
    contador = collections.Counter(dict)
    print(contador)

    lista2 = ["corona", "e", "la"]
    resultado = contar_ocurrencias_archivo('//archivo1', lista2)
    print(resultado)

