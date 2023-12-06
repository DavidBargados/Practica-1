import random
import platform
import os

#NOM I COGNOMS: DAVID BARGADOS GÓMEZ


def clear_screen():                 #LIMPIA LA PANTALLA
    sistema = platform.system()
    if sistema == "Windows":
        os.system('cls')
    else:
        os.system('clear')

def genera_tauler():            #CREAR TABLERO
    tauler = [
        [0, 1, 2, 3, 4, 5, 6, 7],
        [25, 26, 27, 28, 29, 30, 31, 8],
        [24, 43, 44, 45, 46, 47, 32, 9],
        [23, 42, 53, 54 ,48, 33, 10],
        [22, 41, 52, 51, 50, 49, 34, 11],
        [21, 40, 39, 38, 37, 36, 35, 12], 
        [20, 19, 18, 17, 16, 15, 14, 13]
    ]
    return tauler

fitxes = {
    'vermell': "no assignat",
    'groc': "no assignat",
    'verd': "no assignat",
    'blau': "no assignat"
}
identificadores = ['V','B','D','G']

def tirar_daus():
    return random.randint(1, 6)

def mostrar_tauler(tauler, posicions_jugadors, identificadores):
    for fila in range(len(tauler)):
        for casella in tauler[fila]:
            if isinstance(casella, int):   #VERIFICA SI CASELLA ES UN NUMERO ENTERO
                jugadors_en_casella = [jugador for jugador, posicio in posicions_jugadors.items() if posicio == casella]
                cantidad_jugadores = len(jugadors_en_casella)
                
                if cantidad_jugadores > 1:
                    print(f"[{casella:<2}{cantidad_jugadores}P]", end="")
                elif cantidad_jugadores == 1:
                    color = jugadors_en_casella[0]  # Obtén el color del jugador
                    indice_color = list(posicions_jugadors.keys()).index(color)  # Obtiene el índice del color
                    identificador = identificadores[indice_color]  # Obtiene el identificador del color desde la lista
                    print(f"[{casella:<2}{identificador:^4}]", end="")
                else:
                    print(f"[{casella:^6}]", end="")
        print()

def regles_joc(jugadors, tauler):           #REGLAS DE JUEGO
    posicions_jugadors = {jugador: 0 for jugador in jugadors.values() if jugador != "no assignat"}
    turnos_espera = {jugador: 0 for jugador in fitxes.values() if jugador != "no assignat"}
    jugadors_index = 0
    jugadors_finalitzats = []
    while len(jugadors_finalitzats) < len(posicions_jugadors):  # Continuar hasta que todos los jugadores lleguen al final
        jugador = list(posicions_jugadors.keys())[jugadors_index]
        daus = tirar_daus()
        
       # Verificar si el jugador está en un turno de espera
        if turnos_espera[jugador] > 0:
            print(f"{jugador} está en espera por {turnos_espera[jugador]} turnos.")
            turnos_espera[jugador] -= 1
            jugadors_index = (jugadors_index + 1) % len(posicions_jugadors)
            continue
        
        opcio = input(f"Torn de {jugador},tirar dau? (si,trampa,sortir):")
        if opcio == "si":
            posicio_anterior = posicions_jugadors[jugador]
            posicions_jugadors[jugador] += daus
            print(f"Has tret {daus}, has caigut en: {posicions_jugadors[jugador]}")
        if posicions_jugadors[jugador] >= 53:
            print(f"{jugador} ha llegado al final!")
            jugadors_finalitzats.append(jugador)
        elif opcio == "trampa":
            posicio = int(input("A quina posició et vols moure?: "))
            if posicio > 53:
                print("Aquesta posició no és vàlida!!!")
            else:
                posicio_anterior = posicions_jugadors[jugador]
                posicions_jugadors[jugador] = posicio
                print(f"Has mogut a la posició {posicio}")
        elif opcio == "sortir":
            break
        else:
            
            # Lógica para casillas especiales (oca, puente, dados)
            if posicions_jugadors[jugador] in [5, 9, 16, 21, 25, 30, 34, 37, 41, 46]:
                print(f"Casella {posicions_jugadors[jugador]}, Oca, {jugador}")
                posicions_jugadors[jugador] += daus
                print(f"Va a la casella {posicions_jugadors[jugador]} i torna a jugar")
            elif posicions_jugadors[jugador] == 6:
                print(f"Has caigut en un pont: {posicions_jugadors[jugador]}")
                posicions_jugadors[jugador] = 19
                turnos_espera[jugador] = 1  # Esperar un turno después de pasar por el puente
            elif posicions_jugadors[jugador] == 10:
                print("Has caigut en un dau, tornes a jugar")
                posicions_jugadors[jugador] = 23
            elif posicions_jugadors[jugador] == 17:
                print(f"Has caigut al hotel, espera un torn")
                turnos_espera[jugador] = 1  # Esperar un turno después de estar en el hotel
                turnos_espera[jugador] -= 1
            elif posicions_jugadors[jugador] == 29:
                print(f"Has caigut al pou, espera tres torns")
                turnos_espera[jugador] = 3  # Esperar tres turnos después de caer en el pou
                turnos_espera[jugador] -= 1
            elif posicions_jugadors[jugador] == 38:
                print(f"Has caigut al laberint, espera tres torns")
                turnos_espera[jugador] = 3  # Esperar tres turnos después de estar en el laberinto
                turnos_espera[jugador] -= 1
            elif posicions_jugadors[jugador] == 52:
                posicions_jugadors[jugador] = 0
                print("Has caigut a la calavera, tornes al principi del tauler!!!")
                turnos_espera[jugador] = 0  # No esperar ningún turno después de caer en la calavera
            
            print(f"Posicio anterior: {posicio_anterior}, Posicio actual: {posicions_jugadors[jugador]}")
                
        mostrar_tauler(tauler, posicions_jugadors, identificadores)
        jugadors_index = (jugadors_index + 1) % len(posicions_jugadors)


        for jugador in posicions_jugadors.keys():
            if jugador not in jugadors_finalitzats and posicions_jugadors[jugador] >= 53:
                print(f"{jugador} ha arribat al final!")
                jugadors_finalitzats.append(jugador)
        ranking = sorted(jugadors_finalitzats, key=lambda jugador: posicions_jugadors[jugador])
        for i, jugador in enumerate(ranking, start=1):
            print(f"{i}.{jugador}")
def escull_jugador(color, fitxes):  #PIDE Y COMPRUEBA LOS NOMBRES DE USUARIOS,Y LOS ASIGNA A UNA FICHA
    while True:
        nom = input(f"Escriu un nom  per la fitxa {color}: ")
        if nom.replace(" ", "").isalpha():
            fitxes[color] = nom
            break
        print("Nom invàlid (tan sols lletres i espais)")

def menu():
    global fitxes
    while True:
        clear_screen()
        print(f'''LA OCA
---------
1) Assignar Jugador Vermell       {fitxes["vermell"]}
2) Assignar jugador Blau          {fitxes["blau"]}
3) Assignar jugador Verd          {fitxes["verd"]}
4) Assignar jugador Groc          {fitxes["groc"]}  
5) Començar partida''')
        opcio = int(input("Escull una opció (0 - 5): "))
        if opcio == 1:
            escull_jugador("vermell", fitxes)
        elif opcio == 2:
            escull_jugador("blau", fitxes)
        elif opcio == 3:
            escull_jugador("verd", fitxes)
        elif opcio == 4:
            escull_jugador("groc", fitxes)
        elif opcio == 5:
            # Comprobar si hay al menos 2 jugadores asignados
            if comprobar_jugadores(fitxes) >= 2:
                # Lógica para comenzar la partida
                tauler = genera_tauler()
                regles_joc(fitxes, tauler)
                break
            else:
                print("Es necessiten 2 o més jugadors per jugar!!!!.")
        elif opcio == 0:
            break

def comprobar_jugadores(fitxes):
    cnt = 0
    for clau, valor in fitxes.items():
        if valor != "no assignat":
            cnt = cnt + 1
    return cnt

menu()