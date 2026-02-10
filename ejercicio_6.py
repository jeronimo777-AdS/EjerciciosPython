valor_compra = float(input("Ingrese el valor de la compra: "))

descuento = valor_compra * 0.10

subtotal = valor_compra - descuento

iva = subtotal * 0.19

total = subtotal + iva

print("\nValor de compra:", valor_compra)
print("Descuento (10%):", descuento)
print("Subtotal:", subtotal)
print("IVA (19%):", iva)
print("Total a pagar:", total)
