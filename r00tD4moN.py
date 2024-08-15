#!/usr/bin/env python3
# ⬆ shebang de python
# Librerías ⬇
import pyfiglet                 # pyfiglet para crear el banner, se instala con "pip install pyfiglet"
from termcolor import colored   # termcolor para poner colores a los textos, se instala con "pip install termcolor"
import argparse                 # Crea el menú de ayuda 
import sys                      # Proporciona acceso a algunas variables y funciones que interactúan con el intérprete de Python y el entorno del sistema.
import __fuzzing__                  # Importa el módulo de fuzzing


def ejecutar_fuzzing(url, diccionario):
    # Llama a la función run_fuzzing del módulo fuzzing
    __fuzzing__.run_fuzzing(url, diccionario)


def crear_panel_de_ayuda_banner(texto, fuente, color):
    banner = pyfiglet.figlet_format(texto, font=fuente)
    colored_banner = colored(banner, color)
    return colored_banner


def __panel_deayuda__():
    texto  = 'HackPanel'
    fuente = 'bloody'
    color  = 'red'
    banner = crear_panel_de_ayuda_banner(texto, fuente, color)
    print(banner)

    parser = argparse.ArgumentParser(
        description='↪ HELP PANEL',
        formatter_class=argparse.RawTextHelpFormatter
    )

    parser.add_argument('--scan',                        help='[INFO] Opción para un escaneo silencioso de una dirección IP con nmap')
    parser.add_argument('--fuzzing',                     help='[INFO] Opción para hacer fuzzing web con la herramienta wfuzz')
    parser.add_argument('--scanWP',                      help='[INFO] Opción para escanear WordPress con wpscan (sin la API)')
    parser.add_argument('--sql',                         help='[INFO] Opción para ejecutar una SQL-injection con sqlmap')
    parser.add_argument('--smb',                         help='[INFO] Opción para listar archivos compartidos de SMB')
    parser.add_argument('--url',                         help='[INFO] Opción de URL')
    parser.add_argument('--rpc',                         help='[INFO] Opción para enumerar archivos con el protocolo RPC')
    parser.add_argument('-pb', '--password-brute-force', help='[INFO] Opción de fuerza bruta para atacar logins')
    parser.add_argument('-u', '--user',                  help='[INFO] Proporcionar credenciales de usuario compatible con diccionarios')
    parser.add_argument('-p', '--password',              help='[INFO] Proporcionar credenciales de contraseña compatible con diccionarios')
    parser.add_argument('-d', '--dictionary',            help='[INFO] Parámetro de diccionario')

    parser.add_argument('ip', type=str, help='[INFO] Parámetro para la IP o dirección')

    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(1)

    args = parser.parse_args()

    print(f'IP: {args.ip}')
    if args.scan:
        print(f'Scan: {args.scan}')
    if args.fuzzing:
        print(f'Fuzzing: {args.fuzzing}')

        if args.url and args.dictionary:
            ejecutar_fuzzing(args.url, args.dictionary)

        else:
            print("Error: Se requieren tanto --url como --dictionary para el fuzzing.")

    if args.scanWP:
        print(f'ScanWP: {args.scanWP}')
    if args.password_brute_force:
        print(f'Password Brute Force: {args.password_brute_force}')
    if args.sql:
        print(f'SQL Injection: {args.sql}')
    if args.smb:
        print(f'SMB: {args.smb}')
    if args.user:
        print(f'User: {args.user}')
    if args.password:
        print(f'Password: {args.password}')
    if args.url:
        print(f'URL: {args.url}')
    if args.rpc:
        print(f'RPC: {args.rpc}')
    if args.dictionary:
        print(f'Dictionary: {args.dictionary}')


if __name__ == '__main__':
    __panel_deayuda__()
