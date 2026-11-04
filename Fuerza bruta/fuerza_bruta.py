class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __repr__(self):
        return f"({self.x}, {self.y})"

class Segmento:
    def __init__(self, p, q, nombre):
        # Guardar los extremos ordenados: izq siempre es el de menor x
        if p.x < q.x:
            self.izq = p
            self.der = q
        else:
            self.izq = q
            self.der = p
        self.nombre = nombre

    def __repr__(self):
        return self.nombre

    def y_en(self, x):
        # Que fracción del camino llevamos en x (0 = izquierda, 1 = derecha)
        t = (x - self.izq.x) / (self.der.x - self.izq.x)
        # Avanzar esa misma fracción en y
        return self.izq.y + t * (self.der.y - self.izq.y)
    
    def cruza_vertical(self, x):
        #True si la vertical en x toca el segmento
        return self.izq.x <= x <= self.der.x

def revisar(s, q):
    if not s.cruza_vertical(q.x):
        return "no cruza"

    y = s.y_en(q.x)        # altura del segmento en la x de q

    if y > q.y:
        return "arriba"
    elif y < q.y:
        return "abajo"
    else:
        return "sobre"

def fuerza_bruta(segmentos, q):
    superior = None            # record de arriba (todavía no hay)
    inferior = None            # record de abajo (todavía no hay)
    y_sup = float("inf")       # altura del récord de arriba (empieza en infinito)
    y_inf = float("-inf")      # altura del récord de abajo (empieza en menos infinito)

    for s in segmentos:
        resultado = revisar(s, q)

        if resultado == "no cruza":
            continue           # lo ignoramos y pasamos al siguiente

        y = s.y_en(q.x)

        if resultado == "arriba" and y < y_sup:
            superior = s       # nuevo record: está arriba y más cerca
            y_sup = y
        elif resultado == "abajo" and y > y_inf:
            inferior = s       # nuevo record: está abajo y más cerca
            y_inf = y

    return inferior, superior


# Probemos
s1 = Segmento(Punto(1, 2), Punto(9, 3), "s1")
s2 = Segmento(Punto(2, 7), Punto(8, 6), "s2")
s3 = Segmento(Punto(3, 9), Punto(7, 8.5), "s3")
s4 = Segmento(Punto(2, 1), Punto(6, 0.5), "s4")
segmentos = [s1, s2, s3, s4]

for q in [Punto(5, 4), Punto(5, 7.5), Punto(5, 0.2)]:
    inferior, superior = fuerza_bruta(segmentos, q)
    print("q =", q, "-> entre", inferior, "(abajo) y", superior, "(arriba)")
