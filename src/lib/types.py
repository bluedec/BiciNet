from dataclasses import dataclass


@dataclass()
class Bicicleta:
    id: int
    disponible: bool
    veces_alquilada: int

@dataclass
class Registro:
    importe: int
    minutos: int
