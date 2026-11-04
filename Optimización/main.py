from src.geometry import Punto, Segmento
from src.trapezoidal_map import MapaTrapezoidal


def main():

    # Crear puntos
    p1 = Punto(2, 3)
    p2 = Punto(8, 5)

    p3 = Punto(2, 7)
    p4 = Punto(8, 9)

    # Crear segmentos
    s1 = Segmento(p1, p2)
    s2 = Segmento(p3, p4)

    segmentos = [s1, s2]

    # Construir mapa
    mapa = MapaTrapezoidal(segmentos)
    mapa.construir()

    print("Número de trapecios:", mapa.contar_trapecios())


if __name__ == "__main__":
    main()