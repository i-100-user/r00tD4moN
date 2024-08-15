#!/usr/bin/env python3
# ⬆ shebang de python
# Librerías ⬇
import pyfiglet                 # pyfiglet para crear el banner, se instala con "pip install pyfiglet"
from termcolor import colored   # termcolor para poner colores a los textos, se instala con "pip install termcolor"
import argparse                 # Crea el menú de ayuda 
import sys                      # Proporciona acceso a algunas variables y funciones que interactúan con el intérprete de Python y el entorno del sistema.
import __fuzzing__              # Importa el módulo __fuzzing__

def ejecutar_fuzzing(url, diccionario):
    # Llama a la función run_fuzzing del módulo __fuzzing__
    __fuzzing__.run_fuzzing(url, diccionario)

def crear_panel_de_ayuda_banner(texto, fuente, color):
    try:
        banner = pyfiglet.figlet_format(texto, font=fuente)
    except pyfiglet.FontNotFound:
        print(f"Font '{fuente}' no encontrado. Usando font 'standard' por defecto.")
        banner = pyfiglet.figlet_format(texto, font='standard')
    colored_banner = colored(banner, color)
    return colored_banner

def __panel_deayuda__():
    texto  = 'HackPanel'
    fuente = 'standard'  # Usa un font simple y predeterminado
    color  = 'red'
    
    # Mostrar el banner
    print(crear_panel_de_ayuda_banner(texto, fuente, color))

    parser = argparse.ArgumentParser(
        description='↪ HELP PANEL',
        formatter_class=argparse.RawTextHelpFormatter
    )

    parser.add_argument('--scan',                        help='[INFO] Opción para un escaneo silencioso de una dirección IP con nmap')
    parser.add_argument('--fuzzing',                     nargs=2, help='[INFO] Opción para hacer fuzzing web con la herramienta wfuzz. Requiere URL y archivo de diccionario')
    parser.add_argument('--scanWP',                      help='[INFO] Opción para escanear WordPress con wpscan (sin la API)')
    parser.add_argument('--sql',                         help='[INFO] Opción para ejecutar una SQL-injection con sqlmap')
    parser.add_argument('--smb',                         help='[INFO] Opción para listar archivos compartidos de SMB')
    parser.add_argument('--rpc',                         help='[INFO] Opción para enumerar archivos con el protocolo RPC')
    parser.add_argument('-pb', '--password-brute-force', help='[INFO] Opción de fuerza bruta para atacar logins')
    parser.add_argument('-u', '--user',                  help='[INFO] Proporcionar credenciales de usuario compatible con diccionarios')
    parser.add_argument('-p', '--password',              help='[INFO] Proporcionar credenciales de contraseña compatible con diccionarios')
    parser.add_argument('-d', '--dictionary',            help='[INFO] Parámetro de diccionario')

    parser.add_argument('ip', type=str, nargs='?', help='[INFO] Parámetro para la IP o dirección (opcional)')

    args = parser.parse_args()

    # Procesar los argumentos
    if args.scan:
        print(f'Scan: {args.scan}')
    if args.fuzzing:
        print(f'Fuzzing: URL={args.fuzzing[0]}, Diccionario={args.fuzzing[1]}')
        if args.fuzzing[0] and args.fuzzing[1]:
            try:
                ejecutar_fuzzing(args.fuzzing[0], args.fuzzing[1])
            except FileNotFoundError as e:
                print(f"Error: {e}")
            except Exception as e:
                print(f"Error: {e}")
        else:
            print("Error: Se requieren tanto URL como diccionario para el fuzzing.")
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
    if args.dictionary:
        print(f'Dictionary: {args.dictionary}')
    if args.ip:
        print(f'IP: {args.ip}')

if __name__ == '__main__':
    __panel_deayuda__()
