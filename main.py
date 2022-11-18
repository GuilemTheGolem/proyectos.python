import tres_en_raya

def main():
    jugador_actual= 1
    tablero= tres_en_raya.inicializarTablero()

    while(True):
        if (tres_en_raya.esGanador(tablero) == 1):
            print("GANA EL JUGADOR 1 (X)")
        elif (tres_en_raya.esGanador(tablero) == 5):
            print("GANA EL JUGADOR 2 (O)")
        elif (tres_en_raya.esGanador(tablero) == 0):
            print("HA SIDO EMPATE ")
        else:
            tres_en_raya.pintarTablero(tablero)
            jugador_actual = tres_en_raya.jugar(jugador_actual, tablero)
main()