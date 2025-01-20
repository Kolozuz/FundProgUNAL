from math import sqrt

a = float(input())
b = float(input())
c = float(input())

ecu = b**2-4*a*c

if ecu < 0:
    print("La ecuacion no tiene solucion en los reales")
else:
    sol1 = (b*-1 + sqrt(ecu)) / (2*a)
    sol2 = (b*-1 - sqrt(ecu)) / (2*a)

    if ecu == 0:
        print(f"La ecuacion tiene una solucion real, ella es X = {round(sol1,1)}")
    else:
        print(f"La ecuacion tiene dos soluciones reales, ellas son X1 = {round(sol1,1)} y X2 = {round(sol2,1)}")
