sueldo_base = float(input("Ingrese el sueldo base: "))

venta1 = float(input("Ingrese el monto de la venta 1: "))
venta2 = float(input("Ingrese el monto de la venta 2: "))
venta3 = float(input("Ingrese el monto de la venta 3: "))

total_ventas = venta1 + venta2 + venta3

comision = total_ventas * 0.10

total_a_recibir = sueldo_base + comision

print("\nSueldo base:", sueldo_base)
print("Total de ventas:", total_ventas)
print("Comisión (10%):", comision)
print("Total a recibir:", total_a_recibir)
