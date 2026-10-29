id_cajero = int(input("Ingrese su id: "))
denominaciones = [100, 50, 20, 10]
cantidades = {}
total = 0
for d in denominaciones:
    cantidades[d] = int(input(f"Introduce la cantidad de billetes de {d}: "))
    total = total + d * cantidades[d] 
monto_esperado = float(input("Ingrese el monto esperado del cierre de caja: "))
diferencia = total - monto_esperado

print(f"Arqueo de caja, cajero {id_cajero}")
print("======================================")
for d in denominaciones:
    print(f"Billetes de {d}: {cantidades[d]} -> subtotal S/.{d * cantidades[d]}")
print("======================================")
print(f"Total contado: S/.{total:.2f}")
print(f"({total} con 00/100 soles)")
if diferencia == 0:
    print("La caja cuadra")
elif diferencia > 0:
    print(f"Hay un sobrante de S/.{diferencia:.2f}")
else:
    print(f"Hay un faltante de S/.{abs(diferencia):.2f}")