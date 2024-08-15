#!/usr/bin/env python3
import argparse
import requests
from tqdm import tqdm

# Configurar el parser de argumentos
parser = argparse.ArgumentParser(description="↪ Fuzzing web")
parser.add_argument('url', type=str, help='URL objetivo para el fuzzing')
parser.add_argument('dic', type=str, help='Archivo de diccionario con entradas de prueba')
args = parser.parse_args()

# Abrir y leer el archivo de diccionario
with open(args.dic) as file:  # Usar args.dic para acceder al argumento
    wordlist = file.read().splitlines()

try:
    barra = tqdm(total=len(wordlist), desc="Progreso", unit="urls", dynamic_ncols=True)

    for linea in wordlist:
        url_completa = args.url + linea
        response = requests.get(url_completa)
        if response.status_code == 200:
            tqdm.write(f"↪ Directorio encontrado: {url_completa}")
        barra.update(1)

except KeyboardInterrupt:
    print("\n✖ Fuzzing interrumpido por el usuario")

finally:
    barra.close()
