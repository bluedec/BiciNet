# ============================================================
# VALIDACIONES
# ============================================================
def leer_entero(mensaje, minimo=None, maximo=None):
    """Solicita un número entero al usuario, validando el ingreso."""
    while True:
        try:
            valor = int(input(mensaje))
            if minimo is not None and valor < minimo:
                print(f"  ⚠ El valor debe ser mayor o igual a {minimo}.")
                continue
            if maximo is not None and valor > maximo:
                print(f"  ⚠ El valor debe ser menor o igual a {maximo}.")
                continue
            return valor
        except ValueError:
            print("  ⚠ Debe ingresar un número entero válido.")


def leer_texto_no_vacio(mensaje):
    """Solicita un texto al usuario validando que no esté vacío."""
    while True:
        texto = input(mensaje).strip()
        if texto == "":
            print("  ⚠ El dato no puede estar vacío.")
            continue
        return texto


def leer_dni(mensaje):
    """Solicita un DNI validando que sea numérico."""
    while True:
        dni = input(mensaje).strip()
        if not dni.isdigit():
            print("  ⚠ El DNI debe contener solo números.")
            continue
        return dni




