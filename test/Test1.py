import random

print("Рандомайзер")

connect = True

while connect == True:
    a = input('От:')
    b = input('До:')
    if a>= b:
        print("Ты дебил!(")
        break
    if b <= a:
        print("Idi v popu)")
        break

    finish = random.randint(int(a), int(b))

    print("Ответ: ", int(finish))
