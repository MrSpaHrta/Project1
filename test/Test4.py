import random
import time

comp_turn = ['k', 'n', 'b']
count = [0, 0, 0]

def knd_choice(t):
    if t == 'k': 
        print('камень')
    elif t == 'b': 
        print('бумага')
    elif t == 'n': 
        print('ножницы')

def main():
    gameloop = True
    while gameloop:
        turn = input('k - камень, n - ножницы, b - бумага, exit - выход: ')
        print()
        time.sleep(0.5)
    
        if turn == 'exit': 
            print('выход')
            gameloop = False
        else:
            knd_choice(turn)
            c_turn = random.choice(comp_turn)
            knd_choice(c_turn)
            if(turn == 'k' and c_turn == 'n') or (turn == 'n' and c_turn == 'b') or (turn == 'b' and c_turn == 'k'):
                print('Ты выйграл')
                count[0] += 1 
            
            if(turn == 'n' and c_turn == 'k') or (turn == 'b' and c_turn == 'n') or (turn == 'k' and c_turn == 'b'):
                print('Я тебя трахнул!!!')
                count[1] += 1 

            if(turn == 'k' and c_turn == 'k') or (turn == 'b' and c_turn == 'b') or (turn == 'n' and c_turn == 'n'):
                print('Иди нахуй')
                count[2] += 1
                
        print('Счёт - ', count[0], ':', count[1], 'Нечья - ', count[2])
        if count[1] == 10:
            print("Ну как тебе секс?))")
            
        if count[0] == 10:
            print("Наконец то!!!")
        if count[0] == 10 or count[1] == 10:
            gameloop = False

if __name__ == "__main__":
    main()