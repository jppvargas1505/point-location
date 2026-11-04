class Trapecio:
    def __init__(self, superior, inferior, izquierda, derecha):
        self.superior = superior
        self.inferior = inferior
        self.izquierda = izquierda
        self.derecha = derecha

        self.vecino_sup_izq = None
        self.vecino_inf_izq = None
        self.vecino_sup_der = None
        self.vecino_inf_der = None