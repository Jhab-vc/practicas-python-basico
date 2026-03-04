"""
UNA FUNCION QUE INVIERTE CADA PALABRA DE UNA FRASE.
hola mundo --> aloh odnum
"""

def invertido(frase):
    palabras = frase.split(" ")
    invertidas = []
    for palabra in palabras:
        invertidas.append(palabra [::-1])

    return " ".join(invertidas)

print(invertido("Hola MUNDO"))