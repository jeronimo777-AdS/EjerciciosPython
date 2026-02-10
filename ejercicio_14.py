print("Ingrese los datos de los 4 artículos:\n")

print("Artículo 1:")
precio1 = float(input("  Precio: "))
cantidad1 = int(input("  Cantidad: "))

print("\nArtículo 2:")
precio2 = float(input("  Precio: "))
cantidad2 = int(input("  Cantidad: "))

print("\nArtículo 3:")
precio3 = float(input("  Precio: "))
cantidad3 = int(input("  Cantidad: "))

print("\nArtículo 4:")
precio4 = float(input("  Precio: "))
cantidad4 = int(input("  Cantidad: "))

subtotal1 = precio1 * cantidad1
subtotal2 = precio2 * cantidad2
subtotal3 = precio3 * cantidad3
subtotal4 = precio4 * cantidad4

subtotal_total = subtotal1 + subtotal2 + subtotal3 + subtotal4

iva = subtotal_total * 0.19

total = subtotal_total + iva

print("\n--- FACTURA ---")
print("Subtotal:", subtotal_total)
print("IVA (19%):", iva)
print("Total:", total)
