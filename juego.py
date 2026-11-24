# DF1 - RF-14: Menu principal
opcion = ""

while opcion != "2":
    print("\n===== BATALLA NAVAL =====")
    print("1. Jugar")
    print("2. Salir")

    opcion = input("Seleccione una opcion: ")

    if opcion == "1":
        print("La partida completa se implementara en la Fase 4.")

    elif opcion == "2":
        print("Saliendo del juego...")

    else:
        print("Opcion invalida")