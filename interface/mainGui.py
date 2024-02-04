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

        padding = 10

        img_menu = tk.PhotoImage(file='imagens/menu_25x25.png')
        self.label = ttk.Label(self, text='Menu', font=('Verdana', 12, 'bold'), image=img_menu, compound='left')
        self.label.image = img_menu
        #self.label.config(padding=(padding,0,padding,0))
        self.label.pack(pady=10,padx=10)

        img_1 = tk.PhotoImage(file="imagens/pessoas_16x16.png")
        self.person_button = ttk.Button(self, text='Interface Pessoa', command=self.controller.show_personGui, width=30, style="W.TButton", image=img_1, compound='left')
        self.person_button.image = img_1
        #self.person_button.config(padding=(padding,0 , padding,0))
        self.person_button.pack(padx=25,pady=5)

        img_manager = tk.PhotoImage(file="imagens/manager_16x16.png")
        self.manager_button = ttk.Button(self, text='Interface Chefia', command=self.controller.show_managerGui, width=30, style="W.TButton", image=img_manager, compound='left')
        self.manager_button.image = img_manager  # Keep a reference to the image
        # Adjust the padding to center the text and image
        #self.manager_button.config(padding=(padding, 0, padding, 0))
        self.manager_button.pack(pady=5, padx=25)

        img_employee = tk.PhotoImage(file='imagens/employee_16x16.png')
        self.employee_button = ttk.Button(self, text='Interface Empregados', command=self.controller.show_employeeGui, width=30, style="W.TButton", image=img_employee, compound='left')
        self.employee_button.image = img_employee
        #self.employee_button.config(padding=(padding,0, padding,0))
        self.employee_button.pack(pady=5,padx=25)

        img_cadidate = tk.PhotoImage(file='imagens/candidate_16x16.png')
        self.candidate_button = ttk.Button(self, text='Interface Candidatos', command= self.controller.show_candidateGui, width=30, style="W.TButton", image=img_cadidate, compound='left')
        self.candidate_button.image = img_cadidate
        #self.employee_button.config(padding=(padding, 0, padding,0))
        self.candidate_button.pack(pady=5,padx=5)

        img_sobre = tk.PhotoImage(file='imagens/sobre_16x16.png')
        self.sobre_button = ttk.Button(self, text='Sobre', command=self.controller.show_sobreGui, width=30, style="W.TButton", image=img_sobre, compound='left')
        self.sobre_button.image = img_sobre
        #self.sobre_button.config(padding=(padding,0,padding,0))
        self.sobre_button.pack(padx=5, pady=5)

        img_sair = tk.PhotoImage(file='imagens/quit_16x16.png')
        self.sair_button = ttk.Button(self, text='Sair', command=self.quit, width=20, style="W.TButton", image=img_sair, compound='left')
        self.sair_button.image = img_sair
        #self.sair_button.config(padding=(padding,0,padding,0))
        self.sair_button.pack(padx=10, pady=20)

        self.label_a = ttk.Label(self, text='Produzido por Fábio Revez', font=('Verdana', 8, 'bold'))
        self.label_a.pack(padx=1, pady=5, side=tk.BOTTOM)
