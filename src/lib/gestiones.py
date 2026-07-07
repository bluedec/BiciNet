
from .validaciones import *

# ============================================================
# GESTIÓN DE CLIENTES
# ============================================================
def registrar_cliente(clientes):
    """Registra un cliente nuevo o retorna uno existente por DNI."""
    dni = leer_dni("Ingrese DNI del cliente: ")
    if dni in clientes:
        print(f"  → Cliente ya registrado: {clientes[dni]}")
        return dni
    nombre = leer_texto_no_vacio("Ingrese nombre y apellido del cliente: ")
    clientes[dni] = nombre
    print(f"  ✔ Cliente {nombre} registrado con éxito.")
    return dni


# ============================================================
# GESTIÓN DE BICICLETAS
# ============================================================
def mostrar_bicicletas(bicicletas):
    """Muestra el estado (disponible/alquilada) de todas las bicicletas."""
    print("\n--- Estado de bicicletas ---")
    for bici in bicicletas:
        estado = "Disponible" if bici["disponible"] else "Alquilada"
        print(f"  Bicicleta N°{bici['id']:02d} - {estado}")
    print("----------------------------\n")


def buscar_bicicleta_disponible(bicicletas):
    """Busca y devuelve la primera bicicleta disponible, o None si no hay."""
    for bici in bicicletas:
        if bici["disponible"]:
            return bici
    return None


def buscar_bicicleta_por_id(bicicletas, id_bici):
    """Busca una bicicleta por su ID."""
    for bici in bicicletas:
        if bici["id"] == id_bici:
            return bici
    return None


