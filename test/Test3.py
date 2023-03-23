# -*- coding: utf-8 -*-

from time import sleep
import random

# replys = ["привет", "пока", "как тебя зовут?", "как дела?"]
# answers = [["Здраствуйте", "Привет", "И тебе не хворать", "Иди нахуй!!!"], ["До свидание!"], ["Робот"], ["Неплохо!"]]

with open("/home/pi/Documents/Project1/test/ans.txt", encoding="UTF-8") as ansfile:
    answers = []
    for st in ansfile:
        st = st.replace("\n", "")
        answers.append(st.split("/"))
    # print(answers)

with open("/home/pi/Documents/Project1/test/rep.txt", encoding="UTF-8") as repfile:
    replys = []
    for st in repfile:
        st = st.replace("\n", "")
        replys.append(st)
    # print(replys)

def exit_proc():
    global replys
    global answers

    with open("/home/pi/Documents/Project1/test/ans.txt", "w", encoding="UTF-8") as ansfile:
        for item in answers:
            it = str(item)[1:-1].replace("'","")
            ansfile.write(it)
            ansfile.write(item+"\n")

    with open("/home/pi/Documents/Project1/test/rep.txt", "w", encoding="UTF-8") as repfile:
        for item in replys:
            repfile.write(item)
            repfile.write(item+"\n")


def learn(an):
    global replys
    global answers
    replys.append(an)
    print("Придумайте ответ: ", end=" ")
    answers.append([input()])
    print("Запомнил!")

def password(x):
    if x == "123":
        return True

def reply(answer):
    game = True
    if answer in replys:
        index = replys.index(answer)
        print(random.choice(answers[index]))
        if answer == "пока":
            exit_proc()
            game = False  
    else:
        print("Не понимаю")
        if password(input("Введите пароль: ")):
            learn(answer)
        else:
            print("Невозможно обучитить")
        sleep(0.5)
    return game 

def main():
    gameLoop = True
    while gameLoop:
        print("Вы: (для выхода напишите 'пока')")
        rep = input().lower()
        gameLoop = reply(rep)

if __name__ == "__main__":
    main()

