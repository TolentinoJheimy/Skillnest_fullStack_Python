for i in range(101):
    print(i)

for i in range(251):
    i *= 2
    print(i)

for point in range(5, 101):
    if point % 10 == 0:
        print(f"Felcidades llegaste a {str(point)} puntos! 😎")
    elif point % 5 == 0:
        print(f"Felcidades llegaste a {str(point)} puntos! 😁")

bonus = sum(range(0, 500001, 2))
print(f"Experciencia total acumulada: {bonus}")

for viaje in range(2024, -1, -3):
    print(viaje)


inicio = 3
fin = 10
salto = 2

for nivel in range(inicio + 1, fin + 1):
    if nivel % salto == 0:
        print(nivel)


