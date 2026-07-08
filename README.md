# 🚲 BiciNet

Sistema de gestión de alquiler de bicicletas desarrollado en Python como trabajo práctico para la cátedra.

## Integrantes del grupo

- Nombre — DNI/Legajo
- Saez Jesus — 42190494/31210
- Veron Victor Antonio — DNI/Legajo
- Benitez Byn — 46243104/31209
- Nombre y Apellido 4 — DNI/Legajo
- Nombre y Apellido 5 — DNI/Legajo

## Comisión **K1.1**

## Descripción general del sistema

**BiciNet** es un sistema de consola que simula la gestión de una red de alquiler de bicicletas urbanas. Permite administrar una flota fija de bicicletas, registrar clientes, gestionar el ciclo completo de alquiler y devolución, y calcular estadísticas de uso del sistema.

### Funcionalidades principales

1. **Ver bicicletas disponibles**: muestra el estado (disponible/alquilada) de cada una de las bicicletas del sistema.
2. **Alquilar bicicleta**: asigna automáticamente la primera bicicleta disponible a un cliente. Si el cliente ya existe (identificado por DNI) se reutilizan sus datos; caso contrario, se registra uno nuevo. Un mismo cliente no puede tener más de una bicicleta alquilada simultáneamente.
3. **Devolver bicicleta**: calcula el tiempo de uso en base a la hora de inicio y fin del alquiler, aplicando una tarifa mínima de 5 minutos aunque el uso real sea menor, y determina el importe a pagar según el precio por minuto configurado.
4. **Ver estadísticas**: informa la cantidad total de alquileres finalizados, la recaudación total, el tiempo promedio de uso y la bicicleta más utilizada del sistema.
5. **Salir**: finaliza la ejecución del programa.

### Detalles de diseño

- La flota se inicializa con una cantidad fija de bicicletas (`CANTIDAD_BICICLETAS`), cada una representada como un diccionario con `id`, `disponible` y `veces_alquilada`.
- Los clientes se almacenan en un diccionario indexado por DNI para evitar duplicados y permitir búsquedas rápidas.
- Los alquileres activos se guardan en un diccionario indexado por el ID de bicicleta, con el DNI del cliente y la hora de inicio.
- El historial de alquileres finalizados se guarda en una lista, utilizada luego para calcular las estadísticas.
- Se incluyen funciones de validación de entrada (enteros dentro de un rango, texto no vacío, DNI numérico) para evitar errores de ingreso de datos.
- Las constantes del sistema (`PRECIO_POR_MINUTO`, `TARIFA_MINIMA_MINUTOS`, `CANTIDAD_BICICLETAS`) están centralizadas al inicio del archivo para facilitar su configuración.

## Instrucciones de ejecución

### Requisitos

- Python 3.10 o superior (se utiliza `match-case`, disponible desde Python 3.10).

### Pasos

1. Clonar el repositorio:
   ```bash
   git clone https://github.com/bluedec/BiciNet
   cd BiciNet
   ```
2. Ejecutar el programa:
   ```bash
   python main.py
   ```
   (o `python3 main.py`, según la configuración del entorno).
3. Navegar el menú principal ingresando el número de opción deseada (1 a 5).

No se requieren dependencias externas: el proyecto utiliza únicamente la librería estándar de Python (`datetime`, `enum`).

## Uso de Inteligencia Artificial

Durante el desarrollo de este proyecto se utilizó **Claude (Anthropic)** como herramienta de apoyo, principalmente para:

- Resolver dudas puntuales sobre estructuras de datos y buenas prácticas en Python.
- Analizar y depurar errores durante la implementación.
- Proponer mejoras de organización del código (por ejemplo, separación en funciones y validaciones de entrada).

## Estado del proyecto

Actualmente implementado:
- [x] Inicialización de bicicletas
- [x] Menú principal y visualización de bicicletas disponibles
- [x] Alquiler de bicicletas 
- [x] Devolución de bicicletas
- [x] Visualización de estadísticas
