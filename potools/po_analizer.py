"""Analiza los achivos .po y obtiene información necesaria para actualizar el README.md"""

import os
import polib
from tabulate import tabulate

def contar_strings_faltantes(pofile):
    """
    Cuenta los archivos .po que faltan por traducir
    """
    po = polib.pofile(pofile)
    strings_faltantes = 0

    for entry in po:
        if not entry.translated() and not entry.obsolete:
            strings_faltantes += 1

    return strings_faltantes

def obtener_last_translator(pofile):
    """
    Obtiene al ultimo traductor del archivo .po dado
    """
    po = polib.pofile(pofile)
    last_translator = po.metadata.get("Last-Translator", "Desconocido")
    return last_translator

def po_analize():
    """
    Itera los archivos .po y obtiene la resectiva información
    """
    # Directorio donde se encuentran los archivos .po y sus subdirectorios
    directorio_base = "docs/locales/es/LC_MESSAGES"
    data = []
    total_faltantes = 0

    for root, _, archivos in os.walk(directorio_base):
        for archivo in archivos:
            if archivo.endswith(".po"):
                ruta_completa = os.path.join(root, archivo)
                # Obtener el directorio padre
                # directorio_padre = os.path.dirname(ruta_completa)
                # Eliminar el string contenido en directorio_base
                ruta_final = ruta_completa.replace(directorio_base, "")
                # Verificar si hay strings faltantes
                faltantes = contar_strings_faltantes(ruta_completa)
                # Obtener el Last-Translator
                last_translator = obtener_last_translator(ruta_completa)
                # Mostrar la ruta final, OK/NO y Last-Translator
                if faltantes == 0:
                    data.append([ruta_final, "SÍ", last_translator])
                else:
                    data.append([ruta_final, f"NO ({faltantes} restantes)", last_translator])
                total_faltantes += faltantes

    # Ordenar las filas por la ruta del archivo (primera columna)
    data.sort(key=lambda x: x[0])

    headers = ["Archivo", "Traducción completa", "Último traductor"]

    return tabulate(data, headers=headers, tablefmt="github")

if __name__ == "__main__":
    print(po_analize())
