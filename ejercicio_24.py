monto_prestamo = float(input("Ingrese el monto del préstamo: "))

tasa_interes = 0.05 
anos = 5

interes_anual = monto_prestamo * tasa_interes

interes_trimestre = interes_anual / 4

interes_mes = interes_anual / 12

interes_total = interes_anual * anos

total_a_pagar = monto_prestamo + interes_total

print("\n--- CÁLCULO DEL PRÉSTAMO ---")
print("Monto del préstamo:", monto_prestamo)
print("\nIntereses:")
print("En un año:", interes_anual)
print("En el tercer trimestre:", interes_trimestre)
print("En el primer mes:", interes_mes)
print("\nTotal de intereses (5 años):", interes_total)
print("Total a pagar:", total_a_pagar)
