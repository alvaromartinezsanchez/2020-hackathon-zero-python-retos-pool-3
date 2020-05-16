from random import randint

options = ["Piedra", "Papel", "Tijeras"]

# El resultado de salida son las siguientes String
#'Empate!'
#'Ganaste!'
#'Perdiste!'
def quienGana(player, ai):
    Player=player.upper()
    Ai=ai.upper()
    result=""
    
    if Player==Ai:
        result='Empate!'
    
    else:
       
        if Player=='PIEDRA' and Ai=='TIJERAS':
            result='Ganaste!'
        
        elif Player=='TIJERAS' and Ai=='PIEDRA':
            result='Perdiste!'

        elif Player=='PIEDRA' and Ai=='PAPEL':
            result='Perdiste!'
        
        elif Player=='PAPEL' and Ai=='PIEDRA':
            result='Ganaste!'

        elif Player=='TIJERAS' and Ai=='PAPEL':
            result='Ganaste!'
        
        elif Player=='PAPEL' and Ai=='TIJERAS':
            result='Perdiste!'
        

    return result

# Entry Point
def Game():
    #
    #
    
    #
    #
    
    winner = quienGana(player, ai)

    print(winner)

