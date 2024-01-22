import tkinter as tk
from tkinter import ttk

class MainGui(tk.Frame):
    def __init__(self, master, controller):
        super().__init__(master)

        self.controller = controller
        
        label = ttk.Label(self, text='Menu', font=30)
        label.pack(pady=5,padx=5)

        person_button = ttk.Button(self, text='Person Interface', command=self.controller.show_personGui)
        person_button.pack(padx=25,pady=5)
        manager_button = ttk.Button(self, text='Manager Interface', command=self.controller.show_managerGui)
        manager_button.pack(pady=5,padx=25)
        employee_button = ttk.Button(self, text='Employee Interface', command=self.controller.show_employeeGui)
        employee_button.pack(pady=5,padx=25)
        candidate_button = ttk.Button(self, text='Candidata Interface', command= self.controller.show_candidateGui)
        candidate_button.pack(pady=5,padx=5)
        ttk.Button(self, text='Quit', command=self.quit).pack(padx=10, pady=20,side=tk.BOTTOM)