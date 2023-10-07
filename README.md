# Ejemplos de Procesamiento de Datos en Python

Este repositorio contiene ejemplos de procesamiento de datos en Python utilizando los formatos CSV y JSON. Los ejemplos incluyen cómo leer y mostrar datos en consola.

## Procesamiento de Datos CSV

El archivo `csv_example.py` contiene un ejemplo de cómo leer datos de un archivo CSV y mostrarlos en la consola.

```python
import csv
from io import StringIO

# Tu cadena CSV
datos_csv = """nombre,edad,ciudad,profesion
Alice,30,New York,Ingeniera
Bob,25,Los Angeles,Doctor
Charlie,35,Chicago,Abogado
David,28,Miami,Arquitecto
Eva,40,Houston,Profesor
"""

# Crear un objeto StringIO (simula un archivo)
archivo_csv = StringIO(datos_csv)

# Leer la cadena CSV
lector_csv = csv.reader(archivo_csv)

# Iterar sobre las filas e imprimir los datos
for fila in lector_csv:
    print(fila)
Procesamiento de Datos JSON
El archivo json_example.py contiene un ejemplo de cómo cargar y mostrar datos desde un objeto JSON en Python.

python
Copy code
import json

# Tu objeto JSON
datos_json = '''
{
    "personas": [
        {
            "nombre": "Alice",
            "edad": 30,
            "ciudad": "New York",
            "profesion": "Ingeniera"
        },
        {
            "nombre": "Bob",
            "edad": 25,
            "ciudad": "Los Angeles",
            "profesion": "Doctor"
        },
        {
            "nombre": "Charlie",
            "edad": 35,
            "ciudad": "Chicago",
            "profesion": "Abogado"
        }
    ]
}
'''

# Cargar el JSON
datos = json.loads(datos_json)

# Imprimir el JSON cargado
print(json.dumps(datos, indent=4))


Cómo Ejecutar los Ejemplos
Para ejecutar estos ejemplos, asegúrate de tener Python instalado en tu sistema. Luego, puedes ejecutar cada uno de los archivos Python (csv_example.py y json_example.py) desde la línea de comandos de la siguiente manera:

python csv_example.py

python json_example.py

Estos comandos ejecutarán los ejemplos respectivos y mostrarán los resultados en la consola.

¡Diviértete explorando y procesando datos en Python!
