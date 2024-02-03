import tkinter as tk
from tkinter import ttk
import webbrowser

class SobreGui(tk.Frame):
    def __init__(self, master, controller):
        super().__init__(master)
        self.controller = controller
        self.label = tk.Label(self, text='Informação', font=('Helvetica', 12, 'bold'))
        self.label.pack(pady=10)
        self.make_widgets()
    
    def make_widgets(self):
        # informação da aplicação
        ttk.Label(self, text='Informações sobre a Aplicação', font=('Helvetica', 10, 'bold')).pack(pady=10)
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
        ttk.Label(self, text=app_info_text, justify=tk.LEFT).pack(padx=10, pady=5)


        # informação da licença
        ttk.Label(self, text='Licença', font=('Helvetica', 10, 'bold')).pack(pady=10)
        licence_text = (
            "Esta aplicação é licenciada com Creative Commons Licence.\n"
            "Para mais informações sobre a licença, consulte o ficheiro LICENCE."
        )
        ttk.Label(self, text=licence_text, justify=tk.LEFT).pack(padx=10, pady=5)


        # Developer Information
        ttk.Label(self, text='Informações do Desenvolvedor', font=('Helvetica', 10, 'bold')).pack(pady=10)
        developer_info_text = (
            "Desenvolvido por Fábio Revez.\n"
            "Para entrar em contato, envie um e-mail para fabiorevez@hotmail.com."
        )
        ttk.Label(self, text=developer_info_text, justify=tk.LEFT).pack(padx=10, pady=5)


        # Donation Link
        ttk.Label(self, text='Faça uma doação para apoiar o desenvolvimento:', font=('Helvetica', 10)).pack(pady=5)
        donation_link = ttk.Label(self, text='Doar agora', cursor='hand2', foreground='blue', font=('Helvetica', 10, 'underline'))
        donation_link.pack(pady=5)
        donation_link.bind("<Button-1>", lambda event: self.open_donation_link())


        # Button to return to the main menu
        ttk.Button(self, text='Menu Principal', command=self.controller.show_mainGui, width=15).pack(pady=10)

    
    def open_donation_link(self):
        # Replace 'https://your_donation_link.com' with your actual donation link
        webbrowser.open_new_tab('https://www.paypal.com/donate/?hosted_button_id=RW3NB9PBF3WGL')