# ============================================================
# ESTADÍSTICAS
# ============================================================
def mostrar_estadisticas(historial, bicicletas):
    """Muestra estadísticas generales de utilización del sistema."""
    print("\n--- Estadísticas del sistema ---")

    if not historial:
        print("  Aún no se registraron alquileres finalizados.")
        print("---------------------------------\n")
        return

    total_alquileres = len(historial)
    total_recaudado = 0
    total_minutos = 0

    for registro in historial:
        total_recaudado += registro["importe"]
        total_minutos += registro["minutos"]

    promedio_minutos = total_minutos / total_alquileres

    bici_mas_usada = max(bicicletas, key=lambda b: b.veces_alquilada)

    print(f"  Total de alquileres finalizados: {total_alquileres}")
    print(f"  Recaudación total: ${total_recaudado}")
    print(f"  Tiempo promedio de uso: {promedio_minutos:.1f} minutos")
    print(f"  Bicicleta más utilizada: N°{bici_mas_usada.id:02d} "
          f"({bici_mas_usada.veces_alquilada} veces)")
    print("---------------------------------\n")
