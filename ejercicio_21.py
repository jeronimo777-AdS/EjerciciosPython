nombre = input("Ingrese el nombre: ")
direccion = input("Ingrese la dirección: ")
ano_nacimiento = int(input("Ingrese el año de nacimiento: "))

ano_actual = 2026
edad = ano_actual - ano_nacimiento

print("\n--- INFORMACIÓN DEL APRENDIZ ---")
print("Nombre:", nombre)
print("Dirección:", direccion)
print("Año de nacimiento:", ano_nacimiento)
print("Edad:", edad, "años")
