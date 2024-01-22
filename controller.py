import tkinter as tk
import logging
from personGui import PersonGui
from managerGui import ManagerGui
from employeeGui import EmployeeGui
from candidateGui import CandidateGui
from mainGui import MainGui
from tkinter.messagebox import *

# controller gui
class Controller:
    def __init__(self, root):
        self.root = root
        self.setup_logging()
        self.show_mainGui()
    
    # setup loggin errors
    def setup_logging(self):
        for handler in logging.root.handlers[:]:
            logging.root.removeHandler(handler)
        logging.basicConfig(filename='/Volumes/Programing/VSCode_Projects/programing_python_book/5_step_Adding_GUI/pratica_conhecimento/MyEnterprise/app.log', encoding='utf-8' ,filemode='a', level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)c')


    def show_mainGui(self):
        try:
            if hasattr(self, 'personGui'):
                self.personGui.destroy()
            if hasattr(self, 'managerGui'):
                self.managerGui.destroy()
            if hasattr(self, 'employeeGui'):
                self.employeeGui.destroy()
            if hasattr(self, 'candidateGui'):
                self.candidateGui.destroy()

            self.mainGui = MainGui(self.root, self)
            self.mainGui.pack()

        except Exception as e:
            logging.error('Error in MainGui: %s', str(e))
            self.show_error_message("Error in MainGui Frame", str(e))
        


        
    def show_personGui(self):
        try:
            self.mainGui.destroy()
            if hasattr(self, 'managerGui'):
                self.managerGui.destroy()
            if hasattr(self, 'employeeGui'):
                self.employeeGui.destroy()
            if hasattr(self, 'candidateGui'):
                self.candidateGui.destroy()

            self.personGui = PersonGui(self.root, self)
            self.personGui.pack()
        
        except Exception as e:
            logging.error('Error in PersonGui: %s', str(e))
            self.show_error_message("Error in PersonGui Frame", str(e))

    
    def show_managerGui(self):
        try:
            self.mainGui.destroy()
            if hasattr(self, 'personGui'):
                self.personGui.destroy()
            if hasattr(self, 'employeeGui'):
                self.employeeGui.destroy()
            if hasattr(self, 'candidateGui'):
                self.candidateGui.destroy()
            
            self.managerGui = ManagerGui(self.root, self)
            self.managerGui.pack()
        except Exception as e:
            logging.error('Error in ManagerGui: %s', str(e))
            self.show_error_message("Error in ManagerGui", str(e))

    def show_employeeGui(self):
        try:
            self.mainGui.destroy()
            if hasattr(self, 'personGui'):
                self.personGui.destroy()
            if hasattr(self, 'managerGui'):
                self.managerGui.destroy()
            if hasattr(self, 'candidateGui'):
                self.candidateGui.destroy()

            self.employeeGui = EmployeeGui(self.root, self)
            self.employeeGui.pack()
        except Exception as e:
            logging.error('Error in EmployeeGui: %s', str(e))
            self.show_error_message('Error in EmployeeGui', str(e))
    
    def show_candidateGui(self):
        try:
            self.mainGui.destroy()
            if hasattr(self, 'personGui'):
                self.personGui.destroy()
            if hasattr(self, 'managerGui'):
                self.managerGui.destroy()
            if hasattr(self, 'employeegui'):
                self.employeeGui.destroy()

            self.candidateGui = CandidateGui(self.root, self)
            self.candidateGui.pack()
        except Exception as e:
            logging.error('Error in CandidateGui: %s', str(e))
            self.show_error_message('Error in CandidateGui', str(e))

    def show_error_message(self, title, message):
        error_popup = tk.Toplevel(self.root)
        error_popup.title(title)

        error_label = tk.Label(error_popup, text=message)
        error_label.pack(padx=20,pady=20)

        ok_button = tk.Button(error_popup, text='OK', command=error_popup.destroy)
        ok_button.pack(pady=10)


    