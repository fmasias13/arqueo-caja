def pedir_cantidades(denominaciones):
    cantidades = {}
    for d in denominaciones:
        cantidades[d] = int(input(f"Ingrese la cantidad de los billetes de {d}: "))
    return cantidades

def calcular_total(denominaciones, cantidades):
    total = 0
    for d in denominaciones:
        total = total + d * cantidades[d]
    return total

def evaluar_diferencia(total, monto_esperado):
    diferencia = total - monto_esperado
    if diferencia == 0:
        return "La caja cuadra"
    elif diferencia > 0:
        return f"Hay un sobrante en caja de S/. {diferencia:.2f}"
    else:
        return f"Hay un faltante de S/.{abs(diferencia):.2f}"

def mostrar_reporte(id_cajero, denominaciones, cantidades, total, resultado):
    print(f"Mostrar el Arqueo de caja del cajero {id_cajero}")
    print("=================================================")
    for d in denominaciones:
        print(f"Billetes de {d}: {cantidades[d]} -> subtotal S/.{d * cantidades[d]}")
    print("=================================================")
    print(f"Total contado S/.{total:.2f}")
    print(resultado)

denominaciones = [100, 50, 20, 10]
id_cajero = int(input("Ingrese su id: "))
cantidades = pedir_cantidades(denominaciones)
monto_esperado = float(input("Ingrese el monto esperado del cierre de caja: "))
total = calcular_total(denominaciones, cantidades)
resultado = evaluar_diferencia(total, monto_esperado)
mostrar_reporte(id_cajero, denominaciones, cantidades, total, resultado)