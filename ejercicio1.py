import os
import re


def contar_palabras(cadena):
    res = re.sub(r'[^\w\s]', '', cadena)
    res = len(res.split())
    return res


def contar_palabras_archivo(path):
    existe = os.path.exists(path)
    if existe:
        file = open(path, 'r')
        lectura = file.read()
        res = contar_palabras(lectura)
        return res
    else:
        print("La ruta especificada no conduce a ningún archivo")


if __name__ == '__main__':
    resultado = contar_palabras_archivo('//archivo1')
    print(resultado)
