#!/usr/bin/env python3
import argparse
import requests
from tqdm import tqdm

def run_fuzzing(url, diccionario):
    # Abrir y leer el archivo de diccionario
    with open(diccionario) as file:
        wordlist = file.read().splitlines()

    try:
        barra = tqdm(total=len(wordlist), desc="Progreso", unit="urls", dynamic_ncols=True)

        for linea in wordlist:
            url_completa = url + linea
            response = requests.get(url_completa)
            if response.status_code == 200:
                tqdm.write(f"↪ Directorio encontrado: {url_completa}")
            barra.update(1)

    except KeyboardInterrupt:
        print("\n✖ Fuzzing interrumpido por el usuario")

    finally:
        barra.close()
