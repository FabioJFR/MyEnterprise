import tkinter as tk
from MyEnterprise.controller import Controller
import sys



class MyEnterprise:
    def __init__(self, root):
        self.root = root
        self.root.title("MyEnterprise")
        self.root.geometry()
        self.root.resizable(False, False)
        
        # create the controller to manage frames
        self.controller = Controller(root)


if __name__ == '__main__':
    print('caminho aqui: ',sys.path)
    root = tk.Tk()
    img = tk.PhotoImage(file='imagens/MyEnterprise_icon.png')
    root.iconphoto(True, img)
    root.iconbitmap(bitmap='images/MyEnterprise_icon.ico')
    root.wm_title('MyEnterprise')
    

    app = MyEnterprise(root)
    root.mainloop()
