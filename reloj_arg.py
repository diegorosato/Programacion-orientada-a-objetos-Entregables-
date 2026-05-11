def convertir_tiempo(*args):
    if len(args) == 1:
        segundos_totales = int(args[0])
        horas = segundos_totales // 3600
        minutos = (segundos_totales % 3600) // 60
        segundos = segundos_totales % 60
        print(f"{segundos_totales} segundos = {horas}h {minutos}m {segundos}s")

    elif len(args) == 3:
        horas = int(args[0])
        minutos = int(args[1])
        segundos = int(args[2])
        total = (horas * 3600) + (minutos * 60) + segundos
        print(f"{horas}h {minutos}m {segundos}s = {total} segundos")

    else:
        print("Error: ingrese 1 o 3 valores.")


# Pedir datos al usuario
entrada = input("Ingrese 1 valor (segundos) o 3 valores separados por espacio (h m s): ")

# Separar los valores ingresados
argumentos = entrada.split()

if len(argumentos) in (1, 3):
    convertir_tiempo(*argumentos)
else:
    print("Error: ingrese 1 argumento (segundos) o 3 argumentos (horas minutos segundos).")