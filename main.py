import tkinter
from tkinter import *
from tkinter import ttk

#---------------------------CORES----------------------------------

co0 = "#FFFFFF" #BRANCO
co1 = "#333333" #PRETO - pesado
co2 = "#fcc058" #Laranja
co3 = "#38576b" #Valor
co4 = "#3297a8" #zul
co5 = "#fff873" #Amarelo
co6 = "#fcc058" #Laranja
co7 = "#e85151" #Vermelho
co8 = co4
co10 = "#fcfbf7"
fundo = "#3b3b3b" #preto

janela = Tk()
janela.title('')
janela.geometry("260x370")
janela.configure(bg=fundo)

#-----------------------DIVISÃO DA TELA EM DOIS FRAMES--------------------------------

frame_cima = Frame(janela, width=240, height=100, bg=co1, relief="raised")
frame_cima.grid(row=0, column=0, sticky=NW, padx=10, pady=10)

frame_baixo = Frame(janela, width=240, height=300, bg=fundo, relief="flat")
frame_baixo.grid(row=1, column=0, sticky=NW)

#-------------------------------FRAME CIMA---------------------------------

app_X = Label(frame_cima, text='X', height=1, relief='flat', anchor='center', font=('Ivy 40 bold'), bg=co1, fg=co7)
app_X.place(x=25, y=10)
app_X = Label(frame_cima, text='Jogador 1', height=1, relief='flat', anchor='center', font=('Ivy 7 bold'), bg=co1, fg=co0)
app_X.place(x=17, y=70)
app_X_pontos = Label(frame_cima, text='0', height=1, relief='flat', anchor='center', font=('Ivy 30 bold'), bg=co1, fg=co0)
app_X_pontos.place(x=80, y=20)

app_separador = Label(frame_cima, text=':', height=1, relief='flat', anchor='center', font=('Ivy 30 bold'), bg=co1, fg=co0)
app_separador.place(x=110, y=20)

app_O = Label(frame_cima, text='O', height=1, relief='flat', anchor='center', font=('Ivy 40 bold'), bg=co1, fg=co4)
app_O.place(x=175, y=10)
app_O = Label(frame_cima, text='Jogador 2', height=1, relief='flat', anchor='center', font=('Ivy 7 bold'), bg=co1, fg=co0)
app_O.place(x=165, y=70)
app_O_pontos = Label(frame_cima, text='0', height=1, relief='flat', anchor='center', font=('Ivy 30 bold'), bg=co1, fg=co0)
app_O_pontos.place(x=130, y=20)

#-------------------------------FRAME BAIXO---------------------------------

#--------------------------linhas verticais---------------------------
app_ = Label(frame_baixo, text='', height=23, relief='flat',pady=5, anchor='center', font=('Ivy 4 bold'), bg=co0, fg=co7)
app_.place(x=90, y=15)
app_ = Label(frame_baixo, text='', height=23, relief='flat',pady=5, anchor='center', font=('Ivy 4 bold'), bg=co0, fg=co7)
app_.place(x=157, y=15)

#-------------------------linhas horizontais--------------------------
app_ = Label(frame_baixo, text=' ', width=195, relief='flat',padx=2, pady=1, anchor='center', font=('Ivy 1 bold'), bg=co0, fg=co7)
app_.place(x=25, y=63)
app_ = Label(frame_baixo, text=' ', width=195, relief='flat',padx=2, pady=1, anchor='center', font=('Ivy 1 bold'), bg=co0, fg=co7)
app_.place(x=25, y=123)

#-------------------------------linha 0-------------------------------
botao_0 = Button(frame_baixo, text='', width=2, height=1, font=('Ivy 20 bold'), overrelief=RIDGE, relief="flat" , bg=fundo, fg=co7)
botao_0.place(x=25, y=15)

botao_1 = Button(frame_baixo, text='', width=2, height=1, font=('Ivy 20 bold'), overrelief=RIDGE, relief="flat" , bg=fundo, fg=co7)
botao_1.place(x=92, y=15)

botao_2 = Button(frame_baixo, text='', width=2, height=1, font=('Ivy 20 bold'), overrelief=RIDGE, relief="flat" , bg=fundo, fg=co7)
botao_2.place(x=159, y=15)

#-------------------------------linha 1-------------------------------
botao_3 = Button(frame_baixo, text='', width=2, height=1, font=('Ivy 20 bold'), overrelief=RIDGE, relief="flat" , bg=fundo, fg=co7)
botao_3.place(x=25, y=76)

botao_4 = Button(frame_baixo, text='', width=2, height=1, font=('Ivy 20 bold'), overrelief=RIDGE, relief="flat" , bg=fundo, fg=co7)
botao_4.place(x=92, y=76)

botao_5 = Button(frame_baixo, text='', width=2, height=1, font=('Ivy 20 bold'), overrelief=RIDGE, relief="flat" , bg=fundo, fg=co7)
botao_5.place(x=159, y=76)


janela.mainloop()