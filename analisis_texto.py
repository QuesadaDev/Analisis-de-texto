import re
cadena = input("Introduce el texto que quieras: ")

mayor, oraciones, palabras_totales = 0, 0, 0
larga = ""


for palabra in cadena:
    separa_cadena_palabras = re.findall(r'\b\w+\b', cadena)
    palabras_totales = len(separa_cadena_palabras)

    mayor += len(palabra)
    if palabras_totales > 0:
        larga = max(separa_cadena_palabras, key=len)
    if "." in palabra:
        oraciones += 1

print(f"Las palabras que hay en la cadena son: {palabras_totales},\n"
      f"hay {oraciones} puntos en toda la cadena.\n"
      f"La palabra más larga es: '{larga}'\n"
      f"y la media de longitud de todas las palabras es de: {mayor/palabras_totales:.2f}")



