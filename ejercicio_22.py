print("Ingrese la capacidad de cada balde en litros:\n")
balde1 = float(input("Balde 1: "))
balde2 = float(input("Balde 2: "))
balde3 = float(input("Balde 3: "))

tiempo_por_litro = 1.5

tiempo1 = balde1 * tiempo_por_litro
tiempo2 = balde2 * tiempo_por_litro
tiempo3 = balde3 * tiempo_por_litro

print("\nTiempos de llenado:")
print("Balde 1 (", balde1, "litros):", tiempo1, "horas")
print("Balde 2 (", balde2, "litros):", tiempo2, "horas")
print("Balde 3 (", balde3, "litros):", tiempo3, "horas")
