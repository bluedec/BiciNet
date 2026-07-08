from enum import Enum
from typing import List
from src.lib.gestiones import *
from src.lib.validaciones import *
from src.lib.alquileres import *
from src.lib.estadistica import *

# ============================================================
# CONSTANTES
# ============================================================
CANTIDAD_BICICLETAS = 10
PRECIO_POR_MINUTO = 50

# ============================================================
# INICIALIZACIÓN DE DATOS
# ============================================================
def inicializar_bicicletas(cantidad):
    """Crea la lista de bicicletas disponibles en el sistema."""
    bicicletas = []
    for i in range(1, cantidad + 1):
        bicicletas.append(Bicicleta(i, True, 0))
    return bicicletas


class DividerType(Enum):
    SINGLE = 1
    DOUBLE = 2

def divider(type: DividerType = DividerType.SINGLE, length = 40):
    """Print a divider line made of 'equal to' signs."""
    match type:
        case DividerType.SINGLE:
            print("-" * length);
        case DividerType.DOUBLE:
            print("=" * length);

# ============================================================
# MENÚ PRINCIPAL
# ============================================================
def mostrar_menu():
    divider(DividerType.DOUBLE)
    print(" Que le gustaria hacer?")
    divider(DividerType.DOUBLE)
    print("1. Ver bicicletas disponibles")
    print("2. Alquilar bicicleta")
    print("3. Devolver bicicleta")
    print("4. Ver estadísticas")
    print("5. Salir")
    divider(DividerType.DOUBLE)


def main():
    bicicletas: List[Bicicleta] = inicializar_bicicletas(CANTIDAD_BICICLETAS)
    clientes = {}
    alquileres_activos = {}
    historial: List[Registro] = []

    while True:
        mostrar_menu()
        opcion = leer_entero("Seleccione una opción: ", minimo=1, maximo=5)

        if opcion == 1:
            mostrar_bicicletas(bicicletas)
        elif opcion == 2:
             alquilar_bicicleta(bicicletas, clientes, alquileres_activos)
        elif opcion == 3:
             devolver_bicicleta(bicicletas, alquileres_activos, historial)
        elif opcion == 4:
            mostrar_estadisticas(historial, bicicletas)
        elif opcion == 5:
            print("\n¡Gracias por usar el sistema! Hasta pronto.")
            break


if __name__ == "__main__":
    main()

