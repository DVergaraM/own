from math import sin, asin
import math

def angInc(n1:float, n2:float, ang:float):
    """
    rad to degree 
        - rad * (180/math.pi)
    degree to rad 
        - degree * (math.pi / 180)
    """
    angR = round(ang * (math.pi / 180), 4)
    print(f"{ang} en radianes = {angR}")
    sinAng = round(sin(angR), 4)
    print(f"Seno de {ang} = {sinAng}")

    r = round(n2 * sinAng, 4)
    print(f"{n2} x {sinAng} = {r}")
    r1 = round(((r) / n1), 4)
    print(f"{r} / {n1} = {r1}")
    aSin = round(asin(r1), 4)
    print(f"Arco seno de {r1} = {aSin} rad")
    aSinDeg = round(aSin * (180/math.pi), 4)
    print(f"{aSin} en grados = {aSinDeg}")


n1 = float(input('Ingrese el indice de refracción del primer medio: '))
n2 = float(input('Ingrese el indice de refracción del segundo medio: '))
angRef = float(input('Ingrese el ángulo de refracción: '))
print('\n')

angInc(n1, n2, angRef)