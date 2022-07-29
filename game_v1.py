# Game Ping-Pong

#Importação de classes
from tkinter import *
import random
import time

# Variavel level recebendo uma entrada de dados como string e transformando para um tipo inteiro
level = int(input("Qual nível você gostaria de jogar? 1/2/3/4/5 \n"))
length = 500/level


root = Tk()
root.title("Ping Pong")
root.resizable(0,0)
root.wm_attributes("-topmost", -1)

canvas = Canvas(root, width=800, height=600, bd=0,highlightthickness=0)
canvas.pack()

root.update()

# Variável
count = 0
lost = False

# Criação da classe bola
class Bola:
    #Definição de uma função para movimentação da barra
    def __init__(self, canvas, Barra, color):
        self.canvas = canvas
        self.Barra = Barra
        self.id = canvas.create_oval(0, 0, 15, 15, fill=color)
        self.canvas.move(self.id, 245, 200)

        starts_x = [-3, -2, -1, 1, 2, 3]
        random.shuffle(starts_x)

        self.x = starts_x[0]
        self.y = -3

        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()


    def draw(self):
        self.canvas.move(self.id, self.x, self.y)

        pos = self.canvas.coords(self.id)
        # Condicional IF
        if pos[1] <= 0:
            self.y = 3
        # Condicional IF    
        if pos[3] >= self.canvas_height:
            self.y = -3
        # Condicional IF
        if pos[0] <= 0:
            self.x = 3
        # Condicional IF    
        if pos[2] >= self.canvas_width:
            self.x = -3

        self.Barra_pos = self.canvas.coords(self.Barra.id)

        # Condicional IF
        if pos[2] >= self.Barra_pos[0] and pos[0] <= self.Barra_pos[2]:
            # Condicional IF dentro de outro IF
            if pos[3] >= self.Barra_pos[1] and pos[3] <= self.Barra_pos[3]:
                self.y = -3
                global count
                count +=1
                score()

        # Condicional IF/ELSE
        if pos[3] <= self.canvas_height:
            self.canvas.after(10, self.draw)
        else:
            game_over()
            global lost
            lost = True

# Criação da classe da Barra
class Barra:
    # Definindo a função para a Barra
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0, 0, length, 10, fill=color)
        self.canvas.move(self.id, 200, 400)

        self.x = 0

        self.canvas_width = self.canvas.winfo_width()

        self.canvas.bind_all("<KeyPress-Left>", self.move_left)
        self.canvas.bind_all("<KeyPress-Right>", self.move_right)

    def draw(self):
        self.canvas.move(self.id, self.x, 0)

        self.pos = self.canvas.coords(self.id)
        # Condicional IF
        if self.pos[0] <= 0:
            self.x = 0
        # Condicional IF
        if self.pos[2] >= self.canvas_width:
            self.x = 0
        
        global lost
        
        # Condicional IF
        if lost == False:
            self.canvas.after(10, self.draw)

    # Função para mover para a esquerda
    def move_left(self, event):
        if self.pos[0] >= 0:
            self.x = -3
    # Função para mover para a direita
    def move_right(self, event):
        if self.pos[2] <= self.canvas_width:
            self.x = 3

# Função para iniciar o jogo
def start_game(event):
    global lost, count
    lost = False
    count = 0
    score()
    canvas.itemconfig(game, text=" ")

    time.sleep(1)
    Barra.draw()
    Bola.draw()

# Função para acrescentar os pontos
def score():
    canvas.itemconfig(score_now, text="Pontos: " + str(count))
# Função para fim do jogo
def game_over():
    canvas.itemconfig(game, text="Game over!")


Barra = Barra(canvas, "orange")
Bola = Bola(canvas, Barra, "purple")


score_now = canvas.create_text(430, 20, text="Pontos: " + str(count), fill = "green", font=("Arial", 16))
game = canvas.create_text(400, 300, text=" ", fill="red", font=("Arial", 40))


canvas.bind_all("<Button-1>", start_game)

root.mainloop()



