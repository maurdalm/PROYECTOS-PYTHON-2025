# Valores de hora extra de referencia en COP (mínimos) – ajustar según cada caso
VAL_HORA_EXTRA_DIURNA       = 8088.0     # +25%
VAL_HORA_EXTRA_NOCTURNA     = 11323.0    # +75%
VAL_HORA_EXTRA_DOM_FEST_DIURNA  = 13264.0 # +105%
VAL_HORA_EXTRA_DOM_FEST_NOCTURNA= 16500.0 # +155%

# Inicializar totales por sucursal
totales_sucursal = {1:0.0, 2:0.0, 3:0.0}

# Supongamos que los datos los leemos de un archivo, aquí un ejemplo de lista:
registros = [
    # (codigo_empleado, codigo_sucursal, nombre, sueldo_mensual,
    #  horas_extra_diurnas, horas_extra_nocturnas,
    #  horas_extra_dom_fest_diurnas, horas_extra_dom_fest_nocturnas)
    (1001, 1, 'Ana Pérez',   2500000.0,   2, 1, 0, 0),
    (1002, 2, 'Luis Gómez',   1800000.0,   0, 0, 1, 0),
    (1003, 3, 'María Díaz',   2200000.0,   3, 2, 0, 1),
    # … más registros …
]

print("Código\tSucursal\tNombre\tSueldo Mensual\tPago Horas Extra\tSueldo Total")
for rec in registros:
    cod_emp, cod_suc, nombre, sueldo_mensual, h_ed, h_en, h_df_d, h_df_n = rec

    pago_he = (
        h_ed   * VAL_HORA_EXTRA_DIURNA +
        h_en   * VAL_HORA_EXTRA_NOCTURNA +
        h_df_d * VAL_HORA_EXTRA_DOM_FEST_DIURNA +
        h_df_n * VAL_HORA_EXTRA_DOM_FEST_NOCTURNA
    )

    sueldo_total = sueldo_mensual + pago_he
    print(f"{cod_emp}\t{cod_suc}\t{nombre}\t{sueldo_mensual:.2f}\t{pago_he:.2f}\t{sueldo_total:.2f}")

    totales_sucursal[cod_suc] += sueldo_total

print("\nTotales por sucursal:")
for suc in [1,2,3]:
    print(f"Sucursal {suc}: {totales_sucursal[suc]:.2f}")

