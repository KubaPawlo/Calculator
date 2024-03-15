from tkinter import *
import tkinter.colorchooser as cch
import tkinter.messagebox as msb
from math import pi
from math import exp
from math import sqrt

class Kalkulator:
    def __init__(self, master):
        self.master = master
        self.master.wm_title('Kalkulator')

        self.frame = Frame(self.master, width=600, height=300)
        self.frame.pack()

        # Utwórz przyciski z cyframi 0-9 oraz operacjami +, -, *, /
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', 'C', '=', '+',
            '(', ')'
        ]

        row_val = 1
        col_val = 1

        # Przyciski od 0 do 9 oraz operacje
        for button in buttons:
            # lambda to kreowanie anonimowej, krótkiej funkcji jednolinijkowej
            Button(self.frame, text=button, command=lambda b=button: self.dodaj_do_wyniku(b)).grid(row=row_val, column=col_val)
            col_val += 1
            if col_val > 4:
                col_val = 1
                row_val += 1

        self.wynik = ""

        Pi = Button(self.frame, text='Pi', command=lambda: self.dodaj_do_wyniku(str(pi))).grid(row=5, column=3)

        Euler_constant = Button(self.frame, text='Euler_const', command=lambda: self.dodaj_do_wyniku((str(exp(1))))).grid(row=5, column= 5)

        Sqrt= Button(self.frame, text= 'sqrt', command= lambda: self.dodaj_do_wyniku(str('sqrt'))).grid(row=4, column=5)

        color_button = Button(self.frame, text='Wybierz kolor', command=self.wybierz_kolor)
        color_button.grid(row=6, column=0)

        self.result_var = StringVar()
        Label(self.frame, textvariable=self.result_var).grid(row=7, column=0)

    def dodaj_do_wyniku(self, value):
        if value == 'C':
            self.wynik = ""
        elif value == '=':
            try:
                self.wynik = str(eval(self.wynik))
            except:
                self.wynik = 'Błąd'
        else:
            self.wynik += value

        self.result_var.set(self.wynik)

    def wybierz_kolor(self):
        color = cch.askcolor()[1]
        if color:
            self.frame.configure(bg=color)
            msb.showinfo("Wybrany kolor to ", color)

root = Tk()
kalkulator = Kalkulator(root)
root.mainloop()