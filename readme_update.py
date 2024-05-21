"""Modulo para actualizar el README.md"""

from jinja2 import Environment, FileSystemLoader
from potools.po_analizer import po_analize


def actualizar_readme(table):
    """
    Obtiene información de los archivos .po y actualiza el archivo README.md
    """
    file_loader = FileSystemLoader('.')
    env = Environment(loader=file_loader)

    template = env.get_template('.github/README_template.md')

    output = template.render(table=table)

    with open('README.md', 'w', encoding='utf-8') as f:
        f.write(output)

actualizar_readme(po_analize())
