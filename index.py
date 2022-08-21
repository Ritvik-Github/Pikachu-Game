from tkinter import *
from PIL import ImageTk, Image
# part 2 start
import random
# part 2 end
root = Tk()
root.title("Card Game")
root.geometry("600x400")
root.config(background="blue")

button = ImageTk.PhotoImage(Image.open("button.jpg"))
Abra = ImageTk.PhotoImage(Image.open("abra.jpg"))
Bulbasour = ImageTk.PhotoImage(Image.open("bulbasour.jpg"))
Charmender = ImageTk.PhotoImage(Image.open("charmender.jpg"))
Iyvasour = ImageTk.PhotoImage(Image.open("Iyvasour.jpg"))
Jigglypuff = ImageTk.PhotoImage(Image.open("jigglypuff.jpg"))
Kadabra = ImageTk.PhotoImage(Image.open("kadabra.jpg"))
Meowth = ImageTk.PhotoImage(Image.open("meowth.jpg"))
Nidoking = ImageTk.PhotoImage(Image.open("nidoking.jpg"))
Paras = ImageTk.PhotoImage(Image.open("paras.jpg"))
Persian = ImageTk.PhotoImage(Image.open("persion.jpg"))
Pikachu = ImageTk.PhotoImage(Image.open("pikachu.jpg"))
Ratata = ImageTk.PhotoImage(Image.open("ratata.jpg"))
Sqiurtle = ImageTk.PhotoImage(Image.open("squirtle.jpg"))

pl1 = Label(root, text="Player 1", bg="red", fg="white")
pl1.place(relx=0.1, rely=0.3, anchor=CENTER)

pl2 = Label(root, text="Player 2", bg="royal blue", fg="white")
pl2.place(relx=0.9, rely=0.3, anchor=CENTER)

ps1 = Label(root, bg="red", fg="white")
ps1.place(relx=0.1, rely=0.4, anchor=CENTER)

ps2 = Label(root, bg="royal blue", fg="white")
ps2.place(relx=0.9, rely=0.4, anchor=CENTER)

lbl5 = Label(root, bg="black", fg="white")
lbl5.place(relx=0.5, rely=0.5, anchor=CENTER)
# Part 2 start
image_list = [Abra, Bulbasour, Charmender, Iyvasour, Jigglypuff,Kadabra, Meowth, Nidoking, Paras, Persian, Pikachu, Ratata, Sqiurtle]
powers_list = [30, 60, 50, 100, 70, 70, 60, 90, 40, 70, 200, 40, 50]
player1score = 0

def player1():
    global player1score
    random_no = random.randint(0, len(image_list)+1)
    random_pokemon = image_list[random_no]
    lbl5["image"] = random_pokemon
    player1score = player1score + powers_list[random_no]
    ps1["text"] = str(player1score)
player_1_btn = Button(root,image = button, command = player1)
player_1_btn.place(relx = 0.1, rely = 0.6, anchor = CENTER)

player2score = 0

def player2():
    global player2score
    random_no2 = random.randint(0, len(image_list)+1)
    random_pokemon = image_list[random_no2]
    lbl5["image"] = random_pokemon
    player2score = player2score + powers_list[random_no2]
    ps2["text"] = str(player2score)
player_2_btn = Button(root,image = button, command = player2)
player_2_btn.place(relx = 0.9, rely = 0.6, anchor = CENTER)

root.mainloop()
