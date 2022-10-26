from math import sin, asin
import math

def angRef(n1:float, n2:float, ang:float):
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

    r = n1 * sinAng
    print(f"{n1} x {sinAng} = {r}")
    r1 = round(((r) / n2), 4)
    print(f"{r} / {n2} = {r1}")
    aSin = round(asin(r1), 4)
    print(f"Arco seno de {r1} = {aSin} rad")
    aSinDeg = round(aSin * (180/math.pi), 4)
    print(f"{aSin} en grados = {aSinDeg}")


n1 = float(input('Ingrese el indice de refracción del primer medio: '))
n2 = float(input('Ingrese el indice de refracción del segundo medio: '))
angInc = float(input('Ingrese el ángulo de incidencia: '))
print('\n')

angRef(n1, n2, angInc)