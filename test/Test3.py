replys = []

def reply(answer):
    game = True
    if answer == "привет":
        print("Здраствуйте")
    elif answer == "пока":
        print("До свидание!")
        game = False
    elif answer == "как тебя зовут?":
        print("Робот")
    elif answer == "как дела?":
        print("Неплохо!")    
    else:
        print("Не понимаю")
    return game 

def main():
    gameLoop = True
    while gameLoop:
        print("Вы")
        rep = input().lower()
        gameLoop = reply(rep)

if __name__ == "__main__":
    main()