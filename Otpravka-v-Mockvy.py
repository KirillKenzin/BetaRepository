
from tkinter import *
import random


G_WIDTH = 1000
G_HEIGHT = 600
ITEM = 20
ITEM_WORLD = 40
COLOR1 = 'cyan'
COLOR2 = 'green'
G_X = 24
G_Y = 14
G_X_N = 0
G_Y_N = 0
G_L = []
G_S = 1
G_W = []
V_G_X = G_WIDTH/ITEM
V_G_Y = G_HEIGHT/ITEM
P_L = []
P_S = 20
COLOR3 = 'yellow'
COLOR4 = 'white'
WHILE_CHECK1 = 0
W_X = 24
W_Y = 14
GL_CHECK = True


root = Tk()
root.title('Отправка в Москву')
root.resizable(False, False)
# root.wm_attributes('-topmost', 1)


canvas = Canvas(root, width=G_WIDTH, height=G_HEIGHT, background ='black', bd=0, highlightthickness=0)


canvas.pack()


def S_P_I(canvas, x, y):
    global G_L
    id1 = canvas.create_rectangle(x * ITEM, y * ITEM, x * ITEM + ITEM,
                                  y * ITEM + ITEM, fill = COLOR1)
    
    id2 = canvas.create_rectangle(x * ITEM + 2, y * ITEM + 2, x * ITEM + ITEM - 2,
                                  y * ITEM + ITEM - 2, fill = COLOR2)
    #G_L.append([x, y, id1, id2])
    print(G_L)

S_P_I(canvas, G_X, G_Y)


def World(canvas, x, y):
    global G_W

    id1 = canvas.create_rectangle((x) * ITEM, (y + 1) * ITEM, (x) * ITEM + ITEM,
                                  (y + 1) * ITEM + ITEM, fill=COLOR2)

    id2 = canvas.create_rectangle(x * ITEM, y * ITEM, x * ITEM + ITEM,
                                  y * ITEM + ITEM, fill=COLOR2)

    id3 = canvas.create_rectangle((x) * ITEM, (y + 2) * ITEM, (x) * ITEM + ITEM,
                                  (y + 2) * ITEM + ITEM, fill=COLOR2)

    id4 = canvas.create_rectangle((x + 2) * ITEM, (y) * ITEM, (x + 2) * ITEM + ITEM,
                                  (y) * ITEM + ITEM, fill=COLOR2)

    id5 = canvas.create_rectangle((x + 2) * ITEM, (y + 1) * ITEM, (x + 2) * ITEM + ITEM,
                                  (y + 1) * ITEM + ITEM, fill=COLOR2)

    id6 = canvas.create_rectangle((x + 2) * ITEM, (y + 2) * ITEM, (x +2) * ITEM + ITEM,
                                  (y + 2) * ITEM + ITEM, fill=COLOR2)

    id7 = canvas.create_rectangle((x - 1) * ITEM, (y + 4) * ITEM, (x - 1) * ITEM + ITEM,
                                  (y + 4) * ITEM + ITEM, fill=COLOR2)

    id8 = canvas.create_rectangle((x) * ITEM, (y + 5) * ITEM, (x) * ITEM + ITEM,
                                  (y + 5) * ITEM + ITEM, fill=COLOR2)

    id9 = canvas.create_rectangle((x + 1) * ITEM, (y + 5) * ITEM, (x + 1) * ITEM + ITEM,
                                  (y + 5) * ITEM + ITEM, fill=COLOR2)

    id10 = canvas.create_rectangle((x + 2) * ITEM, (y + 5) * ITEM, (x + 2) * ITEM + ITEM,
                                  (y + 5) * ITEM + ITEM, fill=COLOR2)

    id11 = canvas.create_rectangle((x + 3) * ITEM, (y + 4) * ITEM, (x + 3) * ITEM + ITEM,
                                  (y + 4) * ITEM + ITEM, fill=COLOR2)

    G_W.append([x, y, id1, id2, id3, id4, id5, id6, id7, id8, id9, id10, id11])


while WHILE_CHECK1 < P_S:
    W_X = random.randrange(int(V_G_X))
    W_Y = random.randrange(int(V_G_Y))
    id1 = canvas.create_oval(W_X * ITEM, W_Y * ITEM, W_X * ITEM + ITEM,
                             W_Y * ITEM + ITEM, fill=COLOR3)

    id2 = canvas.create_oval(W_X * ITEM + 2, W_Y * ITEM + 2, W_X * ITEM + ITEM - 2,
                             W_Y * ITEM + ITEM - 2, fill=COLOR4)

    P_L.append([W_X, W_Y, id1, id2])
    WHILE_CHECK1 = WHILE_CHECK1 + 1


def Kvadrat_World(casvas, x, y):
    if WHILE_CHECK1 == 20 or 21:
        P_L.append([W_X, W_Y, id1, id2])
    print(P_L)


Kvadrat_World(canvas, 2, 2)


def Check_I():
    if len(G_W) >= G_S:
        Temp = G_W.pop(0)
        print(Temp)
        canvas.delete(Temp[2])
        canvas.delete(Temp[3])
        canvas.delete(Temp[4])
        canvas.delete(Temp[5])
        canvas.delete(Temp[6])
        canvas.delete(Temp[7])
        canvas.delete(Temp[8])
        canvas.delete(Temp[9])
        canvas.delete(Temp[10])
        canvas.delete(Temp[11])
        canvas.delete(Temp[12])
        # canvas.delete(Temp[13])

    # elif len(G_L) >= G_S:
    #     Temp = G_L.pop(0)
    #     print(Temp)
    #     canvas.delete(Temp[2])
    #     canvas.delete(Temp[3])


def Check_W():
    if len(G_L) >= G_S:
        Temp = G_L.pop(0)
        print(Temp)
        canvas.delete(Temp[2])
        canvas.delete(Temp[3])

def Check_D(F_X, F_Y):
    global GL_CHECK
    for i in range(len(G_W)):
        if G_W [i][0] == F_X and G_W [i][1] == F_Y:
            GL_CHECK = False
            
def G_MOVE(event):
    global G_X
    global G_Y

    global W_X
    global W_Y

    global GL_CHECK

    if GL_CHECK == True:
        G_X_N = 0
        G_Y_N = 0
        if event.keysym == 'Left':
            G_X_N = 1
            G_Y_N = 0
            Check_I()
            Check_W()

        elif event.keysym == 'Right':
            G_X_N = -1
            G_Y_N = 0
            Check_I()
            Check_W()

        elif event.keysym == 'Up':
            G_X_N = 0
            G_Y_N = 1
            Check_I()
            Check_W()

        elif event.keysym == 'Down':
            G_X_N = 0
            G_Y_N = -1
            Check_I()
            Check_W()

        else:
            pass
    else:
        pass

    Check_D(W_X + G_X_N, W_Y + G_Y_N)
    G_X = G_X + G_X_N
    G_Y = G_Y + G_Y_N
    W_X = W_X + G_X_N
    W_Y = W_Y + G_Y_N
    World(canvas, G_X, G_Y)
    Kvadrat_World(canvas, W_X, W_Y)


canvas.bind_all('<KeyPress-Left>', G_MOVE)
canvas.bind_all('<KeyPress-Right>', G_MOVE)
canvas.bind_all('<KeyPress-Up>', G_MOVE)
canvas.bind_all('<KeyPress-Down>', G_MOVE)


root.update()
root.mainloop()
