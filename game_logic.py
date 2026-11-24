# DF2 - Validacion de la jugada
# RF-04, RF-07 y RF-08

lista_disparos = "A2D1"
valida = 0

print("===== VALIDACION DE LA JUGADA =====")
print("Disparos realizados:", lista_disparos)

while valida == 0:

    coord = input("Ingrese una coordenada (A1-D4): ")

    if len(coord) != 2:
        print("Coordenada invalida")

    elif not ("A" <= coord[0] <= "D" and
              "1" <= coord[1] <= "4"):
        print("Coordenada invalida")

    else:
        i = 0
        encontrado = 0

        while i < len(lista_disparos) and encontrado == 0:

            if (lista_disparos[i] == coord[0] and
                lista_disparos[i + 1] == coord[1]):

                encontrado = 1

            else:
                i = i + 2

        if encontrado == 1:
            print("Casilla repetida")

        else:
            valida = 1
            print("Coordenada valida y disponible")


# DF3 Fin de la partida
# Comprobacion del ganador o empate

print("\n===== FIN DE LA PARTIDA =====")

hundidos_j1 = 0
hundidos_j2 = 0
fin = 0

hundidos_j1 = int(input("Barcos hundidos por el Jugador 1 (0-3): "))
hundidos_j2 = int(input("Barcos hundidos por el Jugador 2 (0-3): "))

if hundidos_j1 == 3 and hundidos_j2 == 3:
    print("Empate")
    fin = 1

elif hundidos_j1 == 3:
    print("Ganador: Jugador 1")
    fin = 1

elif hundidos_j2 == 3:
    print("Ganador: Jugador 2")
    fin = 1

else:
    print("La partida continua")