connect = True

while connect == True:
    namber = input("Число: ")
    procent = input("Процeнт: ")
    while type(namber) != int:
        try:
            namber = int(namber)
            procent = int(procent)

        except ValueError:
            print("Вводи цулочисленые значения! ")
            namber = input('Число: ')
            procent = input("Процeнт: ")
        

    while type(procent) != int:
        try:
            procent = int(procent)
            namber = int(namber)

        except ValueError:
            print("Вводи цулочисленые значения! ")
            namber = input('Число: ')
            procent = input("Процeнт: ")
    
    finish = namber / 100 *procent

    print("Ваш ответ: ", int(finish))