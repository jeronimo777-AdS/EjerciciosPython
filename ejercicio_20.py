precio_unitario = float(input("Ingrese el precio unitario: "))
cantidad = int(input("Ingrese la cantidad: "))
descuento_porcentaje = float(input("Ingrese el descuento (%): "))

subtotal = precio_unitario * cantidad

descuento = subtotal * (descuento_porcentaje / 100)

subtotal_con_descuento = subtotal - descuento

iva = subtotal_con_descuento * 0.19

precio_neto = subtotal_con_descuento + iva

print("\nSubtotal:", subtotal)
print("Descuento:", descuento)
print("Monto del IVA:", iva)
print("Precio neto:", precio_neto)
