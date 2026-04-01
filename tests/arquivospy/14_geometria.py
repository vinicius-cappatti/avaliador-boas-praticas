"""Módulo de geometria."""
import math
class Circulo:
    def __init__(self,raio):
        self.raio=raio
    def area(self):
        return math.pi*self.raio**2
    def perimetro(self):
        return 2*math.pi*self.raio

class Retangulo:
    def __init__(self,largura,altura):
        self.largura=largura
        self.altura=altura
    def area(self):
        return self.largura*self.altura
    def perimetro(self):
        return 2*(self.largura+self.altura)

class Triangulo:
    def __init__(self,base,altura,lado_a,lado_b,lado_c):
        self.base=base
        self.altura=altura
        self.lado_a=lado_a
        self.lado_b=lado_b
        self.lado_c=lado_c
    def area(self):
        return (self.base*self.altura)/2
    def perimetro(self):
        return self.lado_a+self.lado_b+self.lado_c
