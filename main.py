import tkinter as tk
from controller import Controller

class MyEnterprise:
    def __init__(self, root):
        self.root = root
        self.root.title("MyEnterprise")
        self.root.geometry()
        
        # create the controller to manage frames
        self.controller = Controller(root)  


if __name__ == '__main__':
    root = tk.Tk()
    app = MyEnterprise(root)
    root.mainloop()
