lang = "EN"
lang_opt = input("Enter L to change language or other key to continue: ")
while lang_opt == "l":
    if lang == "RU":
        lang = "EN"
        lang_opt = input("Enter L to change language or other key to continue: ")
    else:
        lang = "RU"
        lang_opt = input("Ввидите L, чтобы сменить язык, или любую клавишу, чтобы продолжить: ")
if lang == "EN":
    f = "Enter first number: "
    o = "Enter operation (+, -, *, /): "
    s = "Enter second number"
    r = "Result"
    e = "Error"
if lang == "RU":
    f = "Введите первое число: "
    o = "Введите операцию (+, -, *, /): "
    s = "Введите второе число: "
    r = "Рузультат: "
    e = "Ошибка: "
pip = 'a'
while pip =='a':
    f_num = float(input(f))
    oper = input(o)
    s_num = float(input(s))

    if oper == "+":
        print(r, f_num + s_num)

    elif oper == "-":
        print(r, f_num - s_num)

    elif oper == "*":
        print(r, f_num * s_num)

    elif oper == "/":
        print(r, f_num / s_num)
        
    else:
        print(e)
    pip = input(":")