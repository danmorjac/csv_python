def main():
    print("Seleccione una opción:")
    print("1. Procesar Datos CSV")
    print("2. Procesar Datos JSON")
    
    opcion = input("Ingrese el número de la opción que desea ejecutar: ")
    
    if opcion == "1":
        print("Procesando Datos CSV...\n")
        from csv_processor import procesar_csv
        procesar_csv()
    elif opcion == "2":
        print("Procesando Datos JSON...\n")
        from json_processor import procesar_json
        procesar_json()
    else:
        print("Opción no válida. Por favor, seleccione 1 o 2.")

if __name__ == "__main__":
    main()
    