def año_bisiesto(año):
    if not str(año).isdigit():
        print("Por favor, ingrese un número.")
        return

    año = int(año)

    if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
        print(f"El año {año} es bisiesto")
    else:
        print(f"El año {año} no es bisiesto")

# Set de pruebas
año_bisiesto(2012)
año_bisiesto(2010)
año_bisiesto(2000)
año_bisiesto(1900)
