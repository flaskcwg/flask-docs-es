"""Ese archivo elimina los strings obsoletos de todos los archivos .po"""

import os
import polib


def eliminar_strings_obsoletos(pofile):
    """
    Elimina los strings obsoletos del archivo .po dado
    """
    po = polib.pofile(pofile)
    strings_a_eliminar = []

    for entry in po:
        if entry.obsolete:
            strings_a_eliminar.append(entry)

    for entry in strings_a_eliminar:
        po.remove(entry)

    # Guardar los cambios en el archivo .po
    po.save()

def po_clean():
    """
    Itera sobre los archivos .po y aplica la limpieza a cada uno
    """
    # Directorio donde se encuentran los archivos .po y sus subdirectorios
    directorio_base = "docs/locales/es/LC_MESSAGES"

    for root, _, archivos in os.walk(directorio_base):
        for archivo in archivos:
            if archivo.endswith(".po"):
                ruta_completa = os.path.join(root, archivo)
                eliminar_strings_obsoletos(ruta_completa)
                print(f"Se han eliminado los strings obsoletos en {ruta_completa}")

    print("Proceso completado. Los strings obsoletos han sido eliminados de los archivos .po.")

if __name__ == "__main__":
    po_clean()
