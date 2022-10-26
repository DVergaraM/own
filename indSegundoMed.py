from math import sin, asin
import math

def angInc(n2:float, angInd:float, angRef:float):
    """
    rad to degree 
        - rad * (180/math.pi)
    degree to rad 
        - degree * (math.pi / 180)

    n2 = n1 * angInd / angRef
    n1 = n2 * angRef / angInd
    
    angIndR = round(angInd * (math.pi / 180), 4)
    sinAngIndR = round(sin(angIndR), 4)

    angRefR = round(angRef * (math.pi / 180), 4)
    asinAngRefR = round(sin(angRefR), 4)

    n2 = (n1 * sinAngIndR) /  asinAngRefR
    """
    angIndR = round(angInd * (math.pi / 180), 4)
    sinAngIndR = round(sin(angIndR), 4)
    print(f"El seno de {angInd} = {sinAngIndR}")

    angRefR = round(angRef * (math.pi / 180), 4)
    asinAngRefR = round(sin(angRefR), 4)
    print(f"El arcoseno de {angRef} = {asinAngRefR}")

    r = round(n2 * asinAngRefR, 4)
    print(f"{n2} x {asinAngRefR} = {r}")
    r1 = round(r /  sinAngIndR, 4)
    print(f"{r} / {sinAngIndR} = {r1}")


n1 = float(input('Ingrese el indice de refracción del segundo medio: '))
angInd = float(input('Ingrese el ángulo de incidencia: '))
angRef = float(input('Ingrese el ángulo de refracción: '))
print('\n')

angInc(n1, angInd, angRef)