class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

class Segmento:
    def __init__(self, v1, v2):
        if v1.x < v2.x:
            self.v1, self.v2 = v1, v2
        else:
            self.v1, self.v2 = v2, v1


Punto1 = Punto(8, 9)
Punto2 = Punto(2, 3)
Segmento1 = Segmento(Punto1, Punto2)
print(f"Segmento1: {Segmento1.v1} de {Segmento1.v2}")