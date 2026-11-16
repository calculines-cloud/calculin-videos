# 021 · Pobre con nómina — cálculos (fuentes oficiales INE)
moda = 16520.18          # EAES 2024 (INE, 28-may-2026): salario más frecuente, bruto anual
umbral1 = 12220.4        # ECV 2025 (ingresos 2024), umbral riesgo de pobreza hogar 1 persona (INE)
# Escala OCDE modificada (INE): 1 primer adulto, 0,5 resto >=14 años, 0,3 menores de 14
uc_fam = 1 + 0.5 + 0.3 + 0.3
umbral_fam = umbral1 * uc_fam
falta = umbral_fam - moda
print(f"UC familia 2+2: {uc_fam:.1f}")
print(f"Umbral familia 2 adultos + 2 niños: {umbral_fam:,.2f} €")
print(f"Falta al año: {falta:,.2f} € · al mes (12): {falta/12:,.2f} €")
print(f"Ratio umbral/sueldo: {umbral_fam/moda:.3f}")
print(f"Dos sueldos modales: {2*moda:,.2f} € (> umbral: {2*moda>umbral_fam})")
print(f"Persona sola: sueldo bruto {moda:,.0f} vs umbral {umbral1:,.0f} -> por encima: {moda>umbral1}")
# ocupados en riesgo de pobreza 2025 (INE, Mujeres y hombres en España): H 12,1 %, M 10,2 % -> ambos > 10 %
print("Ocupados en riesgo de pobreza >10 % en ambos sexos:", 12.1>10 and 10.2>10)
# ECV 2025: 36,4 % no puede afrontar gastos imprevistos -> 'más de un tercio'
print("36,4 % > 33,3 %:", 36.4>100/3)
