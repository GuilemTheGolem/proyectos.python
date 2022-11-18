import os
# Realizar el 3 en raya

TableroPrueba= [[0,1,1],[0,0,1],[5,5,0]]

'''Esta función inicializa un tablero'''
def inicializarTablero():
    tablero=[[0,0,0],[0,0,0],[0,0,0]]
    return tablero
    

# Esta función nos pinta un tablero dado un tablero

    



def pintarTablero(tablero):
    os.system("clear")
    print("Tablero: ")
    for i in range(0, len(tablero)):
        salida = ""
        for j in range(0, len(tablero[i])):
            valor = tablero[i][j]
            salida += "|"
            if(valor == 1):
                salida +=('O')
            elif(valor ==5):
                salida +=('X')
            else:
                salida +=(' ')
        salida += "|"
        print(salida)   


def esGanador(tablero):
    if(ganadorJug1(tablero)):
        return 1
    elif(ganadorJug2(tablero)):
        return 5
    elif(empate(tablero)):
        return 0
    else:
        return -1
        
    
def ganadorJug1(tablero):
    l1 = sum(tablero[0])
    l2 = sum(tablero[1])
    l3 = sum(tablero[2])
    c1 = sum(columna(0, tablero))
    c2 = sum(columna(1, tablero))
    c3 = sum(columna(2, tablero))
    d1 = sum([tablero[0][0], tablero[1][1], tablero[2][2]])
    d2 = sum([tablero[0][2], tablero[1][1], tablero[2][0]])

    return (l1 == 3) or (l2 == 3) or (l3 == 3) or (c1 == 3) or (c2 == 3) or (c3 == 3) or (d1 == 3) or (d2 == 3)
    
def ganadorJug2(tablero):
    l1 = sum(tablero[0])
    l2 = sum(tablero[1])
    l3 = sum(tablero[2])
    c1 = sum(columna(0, tablero))
    c2 = sum(columna(1, tablero))
    c3 = sum(columna(2, tablero))
    d1 = sum([tablero[0][0], tablero[1][1], tablero[2][2]])
    d2 = sum([tablero[0][2], tablero[1][1], tablero[2][0]])
    
    return (l1 == 15) or (l2 == 15) or (l3 == 15) or (c1 == 15) or (c2 == 15) or (c3 == 15) or (d1 == 15) or (d2 == 15)
 
''''
def empate(tablero):
    l1 = sum(tablero[0])
    l2 = sum(tablero[1])
    l3 = sum(tablero[2])
    c1 = sum(columna(0, tablero))
    c2 = sum(columna(1, tablero))
    c3 = sum(columna(2, tablero))


    if((l1 > 3) and (l2 > 3) and (l3 > 3)):
        res = "El juego ha terminado - Empate"
        devolver = True

    return devolver'''

def empate(tablero):
    if(not ganadorJug2(tablero) or not ganadorJug1(tablero)):
        if((0 in tablero[0]) or (0 in tablero[1]) or (0 in tablero[2])):
            return False
        else:
            return True
    else:
        return False
    
    
def columna(n, tablero):
  return [tablero[0][n], tablero[1][n], tablero[2][n]] 

def hayPieza(pos, tablero):
    if(pos == "a0"):
        return tablero[0][0] != 0
    elif(pos == "a1"):
        return tablero[0][1] != 0
    elif(pos == "a2"):
        return tablero[0][2] != 0
    elif(pos == "b0"):
        return tablero[1][0] != 0
    elif(pos == "b1"):
        return tablero[1][1] != 0
    elif(pos == "b2"):
        return tablero[1][2] != 0
    elif(pos == "c0"):
        return tablero[2][0] != 0
    elif(pos == "c1"):
        return tablero[2][1] != 0
    elif(pos == "c2"):
        return tablero[2][2] != 0
        
def jugar(jugador_actual, tablero):
    if(jugador_actual == 1):
        print("Juega el jugador 1 (X)")
    else:
        print("Juega el jugador 2 (O)")
        
    pos = input("Dime la coordenada: ")    
     
    if(not hayPieza(pos, tablero)):
        colocarPieza(jugador_actual, pos, tablero)
        
        if(jugador_actual == 1):
            return 5
        else:
            return 1
    else:
        print("Hay una pieza pruena otra coordenada")
        return jugador_actual

def colocarPieza(jugador_actual, pos, tablero):
    if(pos == "a0"):
        tablero[0][0] = jugador_actual
    elif(pos == "a1"):
        tablero[0][1] = jugador_actual
    elif(pos == "a2"):
        tablero[0][2] = jugador_actual
    elif(pos == "b0"):
        tablero[1][0] = jugador_actual
    elif(pos == "b1"):
        tablero[1][1] = jugador_actual
    elif(pos == "b2"):
        tablero[1][2] = jugador_actual
    elif(pos == "c0"):
        tablero[2][0] = jugador_actual
    elif(pos == "c1"):
        tablero[2][1] = jugador_actual
    elif(pos == "c2"):
        tablero[2][2] = jugador_actual

    
    

     
    












