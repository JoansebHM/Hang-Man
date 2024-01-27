import random as rd

word_list = [
    "computadora",
    "telefono",
    "gato",
    "perro",
    "jirafa",
    "elefante",
    "playa",
    "montaña",
    "avion",
    "bicicleta",
    "pelota",
    "libro",
    "pintura",
    "musica",
    "familia",
    "amigo",
    "ciudad",
    "bosque",
    "pizza",
    "helado",
    "rana",
    "mariposa",
    "arcoiris",
    "sol",
    "luna",
    "estrella",
    "lluvia",
    "nieve",
    "rojo",
    "azul",
    "verde",
    "amarillo",
    "rosa",
    "naranja",
    "morado",
    "chocolate",
    "cafe",
    "escuela",
    "trabajo",
    "fiesta",
    "arte",
    "risa",
    "cancion",
    "juego",
    "deporte",
    "viaje",
    "aventura",
    "historia",
    "futuro",
    "pasado"
]

stages = [
    "",
    """
       |
       |
       |
       |
       |
    """,
    """
        ___________
       | /        
       |/        
       |          
       |          
       |
    """,
    """
        ___________
       | /        | 
       |/        
       |          
       |          
       |
    """,
    """
        ___________
       | /        | 
       |/        ( )
       |          
       |          
       |
    """,
    """
        ___________
       | /        | 
       |/        ( )
       |          |
       |         / 
       |
    """,
    """
        ___________
       | /        | 
       |/       (x x) YOU LOSE!
       |          |
       |         / \\
       |
    """,
]

def putChar(char, rw, emptyList):
    for i in range(len(rw)):
        if char == rw[i]:
            if char != emptyList[i]:
                emptyList[i] = char
                break
    return emptyList
        
def showGuessing(word):
    return "".join(word)

def generateRandomWord():
    return word_list[rd.randint(0, len(word_list) - 1)]

def createEmptyList(char):
    emptyList = []
    for _ in range(char):
        emptyList.append("_")
    return emptyList

def main():
    randomWord = generateRandomWord()
    emptyList = createEmptyList(len(randomWord))
    end = len(stages) - 1
    tmp = 0

    while tmp != end:
        print(stages[tmp])
        print(f"Type a letter: {showGuessing(emptyList)}")
        print("")
        guessing = input()

        emptyList_ = emptyList.copy()
        emptyList = putChar(guessing, randomWord, emptyList)
        if (emptyList_ == emptyList):
            tmp += 1
        
        if (guessing == randomWord or showGuessing(emptyList) == randomWord):
            print(f"""
                  CONGRATS, YOU WIN!! The word was {randomWord.upper()}
                         O
                        /|\\
                        / \\

                  """)
            break

    if (tmp == end):      
        print(f"{stages[tmp]}\n The word was {randomWord.upper()}")

if __name__ == "__main__":
    main()
    