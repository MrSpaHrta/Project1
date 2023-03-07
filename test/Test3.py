from time import sleep

replys = ["привет", "пока", "как тебя зовут?", "как дела?"]
answers = ["Здраствуйте", "До свидание!", "Робот", "Неплохо!"]

def reply(answer):
    game = True
    if answer in replys:
        index = replys.index(answers)
        print(answers[index])
    elif answer == replys[-1]:
        game = False  
    else:
        print("Не понимаю")
        sleep(0.5)
    return game 

def main():
    gameLoop = True
    while gameLoop:
        print("Вы")
        rep = input().lower()
        gameLoop = reply(rep)

if __name__ == "__main__":
    main()

    #==========================================================
    # чё за херня? Где ты шарахаешься?
    #==========================================================