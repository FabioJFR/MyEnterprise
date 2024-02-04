import tkinter as tk
from tkinter import ttk

class MainGui(tk.Frame):
    def __init__(self, master, controller):
        super().__init__(master)
        self.controller = controller

        canvas = tk.Canvas(self, width=300, height=300)  # Specify the width and height
        canvas.pack(side=tk.TOP, padx=5,pady=5)
        self.photo = tk.PhotoImage(file='imagens/MyEnterprise_icon_300x300.png')
        canvas.create_image(0, 0, anchor=tk.NW, image=self.photo)

        style = ttk.Style()
        style.configure("W.TButton", font=('Verdana', 10))

        self.label = ttk.Label(self, text='Menu', font=('Verdana', 12, 'bold'))
        self.label.pack(pady=8,padx=5)

        img_1 = tk.PhotoImage(file="imagens/user.png")
        self.person_button = ttk.Button(self, text='Interface Pessoa', command=self.controller.show_personGui, width=20, style="W.TButton", image=img_1, compound='left')
        self.person_button.pack(padx=25,pady=5)
        self.manager_button = ttk.Button(self, text='Interface Chefia', command=self.controller.show_managerGui, width=20, style="W.TButton")
        self.manager_button.pack(pady=5,padx=25)
        self.employee_button = ttk.Button(self, text='Interface Empregados', command=self.controller.show_employeeGui, width=20, style="W.TButton")
        self.employee_button.pack(pady=5,padx=25)
        self.candidate_button = ttk.Button(self, text='Interface Candidatos', command= self.controller.show_candidateGui, width=20, style="W.TButton")
        self.candidate_button.pack(pady=5,padx=5)

        self.sobre_button = ttk.Button(self, text='Sobre', command=self.controller.show_sobreGui, width=20, style="W.TButton")
        self.sobre_button.pack(padx=5, pady=5)

        self.button = ttk.Button(self, text='Sair', command=self.quit, width=10, style="W.TButton")
        self.button.pack(padx=10, pady=20)

        self.label_a = ttk.Label(self, text='Produzido por Fábio Revez', font=('Verdana', 8, 'bold'))
        self.label_a.pack(padx=1, pady=5, side=tk.BOTTOM)
