from datetime import datetime
from .gestiones import *
from .validaciones import *

TARIFA_MINIMA_MINUTOS = 5  # se cobra un mínimo de 5 minutos aunque el uso sea menor
PRECIO_POR_MINUTO = 50

# ============================================================
# ALQUILERES
# ============================================================
def alquilar_bicicleta(bicicletas, clientes, alquileres_activos):
    """Gestiona el alquiler de una bicicleta a un cliente."""
    bici_disponible = buscar_bicicleta_disponible(bicicletas)

    if bici_disponible is None:
        print("  ✘ No hay bicicletas disponibles en este momento.\n")
        return

    dni = registrar_cliente(clientes)

    # Validación: un cliente no puede tener dos bicicletas alquiladas a la vez
    for alquiler in alquileres_activos.values():
        if alquiler["dni"] == dni:
            print("  ✘ Este cliente ya tiene una bicicleta alquilada.\n")
            return

    bici_disponible["disponible"] = False
    alquileres_activos[bici_disponible["id"]] = {
            "dni": dni,
            "hora_inicio": datetime.now()
            }
    print(f"  ✔ Bicicleta N°{bici_disponible['id']:02d} alquilada a {clientes[dni]} (DNI {dni}).\n")


def devolver_bicicleta(bicicletas, alquileres_activos, historial):
    """Gestiona la devolución de una bicicleta y calcula el importe."""
    if not alquileres_activos:
        print("  ✘ No hay bicicletas alquiladas actualmente.\n")
        return

    print("Bicicletas actualmente alquiladas:", list(alquileres_activos.keys()))
    id_bici = leer_entero("Ingrese el N° de bicicleta a devolver: ", minimo=1)

    if id_bici not in alquileres_activos:
        print("  ✘ Esa bicicleta no figura como alquilada.\n")
        return

    bici = buscar_bicicleta_por_id(bicicletas, id_bici)
    datos_alquiler = alquileres_activos.pop(id_bici)

    hora_inicio = datos_alquiler["hora_inicio"]
    hora_fin = datetime.now()
    minutos_uso = max(TARIFA_MINIMA_MINUTOS,
                      int((hora_fin - hora_inicio).total_seconds() // 60) + 1)
    importe = minutos_uso * PRECIO_POR_MINUTO

    bici["disponible"] = True
    bici["veces_alquilada"] += 1

    historial.append({
        "id_bici": id_bici,
        "dni": datos_alquiler["dni"],
        "minutos": minutos_uso,
        "importe": importe
        })

    print(f"  ✔ Bicicleta N°{id_bici:02d} devuelta correctamente.")
    print(f"    Tiempo de uso: {minutos_uso} minutos")
    print(f"    Importe a pagar: ${importe}\n")
