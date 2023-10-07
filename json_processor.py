import json

def procesar_json():
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

if __name__ == "__main__":
    procesar_json()