import tkinter as tk
from interface.personGui import PersonGui
from interface.managerGui import ManagerGui
from interface.employeeGui import EmployeeGui
from interface.candidateGui import CandidateGui
from interface.mainGui import MainGui
from interface.sobreGui import SobreGui
from tkinter.messagebox import *
import logging


# controller gui
class Controller:
    def __init__(self, root):
        self.root = root
        self.show_mainGui()
        self.setup_logging_a()
        

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
            if hasattr(self, 'sobreGui'):
                self.sobreGui.destroy()
            if hasattr(self, 'mainGui'):
                self.mainGui.destroy()

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
            if hasattr(self, 'sobreGui'):
                self.sobreGui.destroy()

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
            if hasattr(self, 'sobreGui'):
                self.sobreGui.destroy()
            
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
            if hasattr(self, 'sobreGui'):
                self.sobreGui.destroy()

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
            if hasattr(self, 'employeeGui'):
                self.employeeGui.destroy()
            if hasattr(self, 'sobreGui'):
                self.sobreGui.destroy()

            self.candidateGui = CandidateGui(self.root, self)
            self.candidateGui.pack()
        except Exception as e:
            logging.error('Error in CandidateGui: %s', str(e))
            self.show_error_message('Error in CandidateGui', str(e))

    def show_sobreGui(self):
        try:
            if hasattr(self, 'personGui'):
                self.personGui.destroy()
            if hasattr(self, 'managerGui'):
                self.managerGui.destroy()
            if hasattr(self, 'employeeGui'):
                self.employeeGui.destroy()
            if hasattr(self, 'candidateGui'):
                self.candidateGui.destroy()
            if hasattr(self, 'mainGui'):
                self.mainGui.destroy()
            if hasattr(self, 'sobreGui'):
                self.sobreGui.destroy()

            self.sobreGui = SobreGui(self.root, self)
            self.sobreGui.pack()

        except Exception as e:
            logging.error('Error in SobreGui: %s', str(e))
            self.show_error_message("Error in SobreGui Frame", str(e))

    def show_error_message(self, title, message):
        error_popup = tk.Toplevel(self.root)
        error_popup.title(title)

        error_label = tk.Label(error_popup, text=message)
        error_label.pack(padx=20,pady=20)

        ok_button = tk.Button(error_popup, text='OK', command=error_popup.destroy)
        ok_button.pack(pady=10)


    def setup_logging_a(self):
        logging.basicConfig(level=logging.DEBUG,  # Set the logging level
                    format='%(asctime)s [%(levelname)s] %(message)s',
                    handlers=[logging.FileHandler('logs/controler.log'), logging.StreamHandler()])
        
    
    

