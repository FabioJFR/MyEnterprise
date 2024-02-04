import tkinter as tk
from tkinter import ttk
import webbrowser

class SobreGui(tk.Frame):
    def __init__(self, master, controller):
        super().__init__(master)
        self.controller = controller
        padding = 10
        img_sobre = tk.PhotoImage(file='imagens/sobre_25x25.png')
        self.label = ttk.Label(self, text='Informação', font=('Verdana', 12, 'bold'), image=img_sobre, compound='left')
        self.label.image = img_sobre
        self.label.config(padding=(padding,0,padding,0))
        self.label.pack(pady=10,padx=10)
        self.make_widgets()
    
    def make_widgets(self):
        form = tk.Frame(self)
        form.pack(fill='both')
        # informação da aplicação
        ttk.Label(form, text='Informações sobre a Aplicação', font=('Verdana', 12, 'bold')).pack(pady=10)
        app_info_text = (
            "Esta aplicação armazena dados em bases de dados locais.\n"
            "Esta aplicação não efetua qualquer ligaçao externa.\n"
            "Esta aplicação não recolhe nenhuns dados nela armazenados.\n"
            "Esta aplicação não contem publicidade e não armazena cookies.\n"
            "Todos os dados armazenados consideram-se privados.\n"
            "Todos os dados são propriedade de quem usa a aplicação.\n"
            "Todos os dados armazenados são da responsabilidade do usuário.\n"
            "O desenvolvedor não se responsabiliza por uso indevido ou perca de dados.\n"
            "O desenvolvedor não recolhe nenhum dado armazenado.\n"
            "O desenvolvedor não recolhe dados pessoais.\n"
            "Esta aplicação é em 02/02/2024 grátis."
        )
        ttk.Label(form, text=app_info_text, font=('Verdana', 12)).pack(padx=10, pady=5)


        # informação da licença
        ttk.Label(form, text='Licença', font=('Verdana', 12, 'bold')).pack(pady=10)
        licence_text = (
            "Esta aplicação é licenciada com Creative Commons Licence.\n"
            "Para mais informações sobre a licença, consulte o ficheiro LICENCE."
        )
        ttk.Label(form, text=licence_text, font=('Verdana', 12)).pack(padx=10, pady=5)


        # Developer Information
        ttk.Label(form, text='Informações do Desenvolvedor', font=('Verdana', 12, 'bold')).pack(pady=10)
        developer_info_text = (
            "Desenvolvido por Fábio Revez.\n"
            "Para entrar em contato, envie um e-mail para fabiorevez@hotmail.com."
        )
        ttk.Label(form, text=developer_info_text, font=('Verdana', 12)).pack(padx=10, pady=5)


        # Donation Link
        ttk.Label(form, text='Faça uma doação para apoiar o desenvolvimento:', font=('Verdana', 12)).pack(pady=5)
        donation_link = ttk.Label(form, text='Doar agora', cursor='hand2', foreground='green', font=('Helvetica', 12, 'underline'))
        donation_link.pack(pady=5)
        donation_link.bind("<Button-1>", lambda event: self.open_donation_link())

        style = ttk.Style()
        style.configure("W.TButton", font=('Verdana', 12))

        # Button to return to the main menu
        button_1 = ttk.Button(form, text='Menu Principal', command=self.controller.show_mainGui, width=15, style="W.TButton")
        button_1.pack(pady=10)

    
    def open_donation_link(self):
        # Replace 'https://your_donation_link.com' with your actual donation link
        webbrowser.open_new_tab('https://www.paypal.com/donate/?hosted_button_id=RW3NB9PBF3WGL')