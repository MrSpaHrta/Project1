from tkinter import *
import random, time

def push(b):
    global game
    global game_left
    global turn
    game[b] = 'X'
    buttons[b].config(text="X", bg="white", state="disabled")
    game_left.remove(b)
    if b == 4 and turn == 0:
        t = random.choice(game_left)
    elif b != 4 and turn == 0:
        t = 4
    if turn > 0:
        t = 8 - b
    if t not in game_left:
        t = random.choice(game_left)
        
    game[t] = '0'
    time.sleep(0.5)
    buttons[t].config(text="0", bg="white", state="disabled")
    if(len(game_left) > 1):
        game_left.remove(t)
    else:
        label['text'] = 'На этом я кончил!'
    turn += 1

game = [None]*9
game_left = list(range(9))
turn = 0

root = Tk()
label = Label(width=20, text="игра крестики-нолики", font=('Arial', 20, 'bold'))
buttons = [Button(width=5, height=2, font=('Arial', 28, 'bold'), bg="green", command=lambda x=i: push(x)) for i in range(9)]

label.grid(row=0, column=0, columnspan=3)

row = 1; col = 0

for i in range(9):
    buttons[i].grid(row=row, column=col)
    col += 1
    if col == 3:
        row +=1
        col = 0

root.mainloop()