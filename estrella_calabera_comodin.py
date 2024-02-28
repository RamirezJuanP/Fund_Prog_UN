print("""Calaberas, estrellas y comodines
""")

participantes = int(input("indique el numero de participantes: "))
if participantes == 2:
    participante_1 = str(input("Por favor indique el nombre del participante #1: "))
    participante_2 = str(input("Por favor indique el nombre del participante #2: "))
    print(f"""
PUNTAJES: {participante_1} = 0 {participante_2} = 0
""")
else:
    print("""para esta etapa es condicion necesaria y suficiente que participen 2 jugadores
Bye""")

print(f"""Ahora es el turno de {participante_1}
Obteniendo tres dados del cubo...
Lanzando los tres dados...
      
+-----------+   +-----------+   +-----------+
|     .     |   |    ___    |   |           | 
|    ,O,    |   |   /   \   |   |           |
| 'ooOOOoo' |   |  |() ()|  |   |     ?     |
|   ´OOO´   |   |   \ ^ /   |   |           | 
|   O' 'O   |   |    vvv    |   |           |
+-----------+   +-----------+   +-----------+
     ORO             ORO           BRONCE
Estrellas: 1     Calaveras:0      
""")

continuar_turno = input(f"{participante_1} quieres jugar de nuevo [S/N]?").upper()

print(f"""
PUNTAJES: {participante_1}= 1 {participante_2}=0
""")

if continuar_turno == "S":
    print(f"""{participante_1} sigue jugando...
Gano {participante_1}
¡Gracias por jugar!
""")
elif continuar_turno == "N":
    print(f"""Ahora es turno de {participante_2}
Obteniendo tres dados del cubo...
Lanzando los tres dados...
Gano {participante_1}
¡Gracias por jugar!
""")
else:
    print(f"""No se reconoce tu respuesta
Bye
Ganó {participante_1}
¡Gracias por jugar!
""")

