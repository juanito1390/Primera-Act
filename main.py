palabras = {
    "LOL" : "una respuesta a algo gracioso",
    "CRINGE" : "algo raro o embarazoso",
    "ROFL" : "una respuesta a una broma",
    "SHEESH" : "ligera desaprobación",
    "CREEPY" : "aterrador, siniestro",
    "AGGRO" : "ponerse agresivo/enojado"
            }
palabra = input("Escribe una palabra que no entiendas (¡con mayúsculas!) ")
if palabra in palabras.keys():
    print(palabras[palabra])
else:
    print("No se encuentra la pabalra en el diccionario")
