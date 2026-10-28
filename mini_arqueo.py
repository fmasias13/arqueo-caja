id_cajero = int(input("Ingrese su codigo: "))
billete100 = int(input("Ingrese la cantidad de billetes de 100: "))
billete50 = int(input("Ingrese la cantidad de billetes de 50: "))
billete20 = int(input("Ingrese la cantidad de billetes de 20: "))
billete10 = int(input("Ingrese la cantidad de billetes de 10: "))

monto100 = billete100*100
monto50 = billete50*50
monto20 = billete20*20
monto10 = billete10*10

arqueo = monto100+monto50+monto20+monto10
monto_esperado = float(input("Ingrese el monto esperado: "))
diferencia = arqueo - monto_esperado

print(f"Arqueo de cajas cajero {id_cajero}")
print(f"Cantidad de billetes de 100: {billete100}")
print(f"Cantidad de billetes de 50: {billete50}")
print(f"Cantidad de billetes de 20: {billete20}")
print(f"Cantidad de billetes de 10: {billete10}")
print("==========================")
print(f"Subtotal de billetes de 100= {monto100}")
print(f"Subtotal de billetes de 50= {monto50}")
print(f"Subtotal de billetes de 20= {monto20}")
print(f"Subtotal de billetes de 10= {monto10}")
print("==========================")
print("Total del monto en gabeta:")
print(f"S/.{arqueo} con 00/100 soles")
if diferencia == 0:
    print("La caja cuadra")
elif diferencia > 0:
    print(f"Hay un sobrante de S/.{diferencia}")
else:
    print(f"Hay un faltante de S/.{abs(diferencia):.2f}")