"""Módulo com operações matemáticas."""
import math
def fatorial(n):
    if n<0:
        raise ValueError("Número deve ser não-negativo")
    if n==0 or n==1:
        return 1
    resultado=1
    for i in range(2,n+1):
        resultado*=i
    return resultado

def fibonacci(n):
    if n<=0:
        return []
    elif n==1:
        return [0]
    seq=[0,1]
    for i in range(2,n):
        seq.append(seq[i-1]+seq[i-2])
    return seq

def eh_primo( numero ):
    if numero<2:
        return False
    for i in range(2,int(math.sqrt(numero))+1):
        if numero%i==0:
            return False
    return True

def potencia(base,expoente):
    return base**expoente
