import tkinter as tk
from classes.person import Person
from tkinter import messagebox
import shelve
import ast 
from tkinter import ttk
import logging


class PersonGui(tk.Frame):
    DB_FILE = 'basedados/person_database'
    LOG_FILE = 'logs/persongui.log'

    def __init__(self, master, controller):
        super().__init__(master)
        self.controller = controller
        self.shelve_name = 'basedados/person_database'
        self.fieldnames = ('nome', 'idade', 'morada', 'telefone', 'email','rede_social', 'pais', 'nacionalidade', 'doc_identificacao', 'nif')
        self.entries = {}
        self.db = shelve.open(self.shelve_name, writeback=True)  # Open the database
        padding = 10
        img_pessoas = tk.PhotoImage(file='imagens/pessoas_25x25.png')
        self.label = ttk.Label(self, text='Pessoas', font=('Verdana', 12, 'bold'), image=img_pessoas, compound='left')
        self.label.image = img_pessoas
        self.label.config(padding=(padding,0,padding,0))
        self.label.pack(pady=10,padx=10)
        self.setup_logging()
        self.make_widgets()
        


    def make_widgets(self):
        form = tk.Frame(self)
        form.pack(fill='both')

        # Labels column
        for i, label in enumerate(('key',) + self.fieldnames):
            tk.Label(form, text=label, font=('Verdana', 10, 'bold')).grid(row=i, column=0, pady=1, sticky='e')

        # Entries column
        for i, label in enumerate(('key',) + self.fieldnames):
            ent = ttk.Entry(form)
            ent.grid(row=i, column=1, pady=1, padx=(0, 10), sticky='w')
            self.entries[label] = ent

        # Text field collumn - available keys
        # Text area with scrollbar
        text_frame = tk.Frame(form)
        text_frame.grid(row=0, column=2, rowspan=len(self.fieldnames) + 1, padx=(10, 0), pady=2, sticky='nsew')
        L = tk.Label(text_frame, text='Chaves Disponiveis', font=('Verdana', 10, 'bold'))
        L.grid(row=0, column=0, pady=1,padx=2, sticky='nesw')
        text_area = tk.Text(text_frame, height=20, width=8, wrap='word', font=('Verdana', 10, 'bold'))
        text_area.grid(row=1, column=0, sticky='nsew')
        scrollbar = tk.Scrollbar(text_frame, command=text_area.yview)
        scrollbar.grid(row=1, column=1, sticky='ns')
        text_area.config(yscrollcommand=scrollbar.set, state='normal')
        for key in self.db:
            text_area.insert(index=tk.END, chars=f'{key}\n')
            text_area.tag_configure('center', justify='center', font=('Verdana', 10, 'bold'))
            text_area.tag_add('center', 1.0, 'end')
        text_area.config(state='disabled') 

        style = ttk.Style()
        style.configure("W.TButton", font=('Verdana', 10))

        # Buttons row 1
        row1_buttons = tk.Frame(self)
        row1_buttons.pack(side=tk.TOP)
        
        img_criar = tk.PhotoImage(file='imagens/create_16x16.png')
        button_1 = ttk.Button(row1_buttons, text='Criar|Atualizar', command=self.confirm_update_record, width=15, style='W.TButton', image=img_criar, compound='left')
        button_1.image = img_criar
        button_1.pack(side=tk.LEFT, padx=2,pady=2)

        img_mostrar = tk.PhotoImage(file='imagens/show_16x16.png')
        button_2 = ttk.Button(row1_buttons, text='Mostrar Campos', command=self.fetch_record, width=15, style='W.TButton', image=img_mostrar, compound='left')
        button_2.image = img_mostrar
        button_2.pack(side=tk.LEFT, padx=2,pady=2)

        img_limpar = tk.PhotoImage(file='imagens/clean_16x16.png')
        button_3 = ttk.Button(row1_buttons, text='Limpar Campos', command=self.confirm_clear_board, width=15, style='W.TButton', image=img_limpar, compound='left')
        button_3.image = img_limpar
        button_3.pack(side=tk.RIGHT, padx=2,pady=2)

        # Buttons row 2
        row2_buttons = tk.Frame(self)
        row2_buttons.pack(side=tk.BOTTOM)

        img_apagar = tk.PhotoImage(file='imagens/delete_16x16.png')
        button_4 = ttk.Button(row2_buttons, text='Apagar', command=self.confirm_delete_record, width=15, style='W.TButton', image=img_apagar, compound='left')
        button_4.image = img_apagar
        button_4.pack(side=tk.LEFT, padx=2, pady=2)

        img_menu = tk.PhotoImage(file='imagens/menu_16x16.png')
        button_5 = ttk.Button(row2_buttons, text='Menu Principal', command=self.controller.show_mainGui, width=15, style='W.TButton', image=img_menu, compound='left')
        button_5.image = img_menu
        button_5.pack(side=tk.LEFT, padx=2,pady=2)

        img_sair = tk.PhotoImage(file='imagens/quit_16x16.png')
        button_6 = ttk.Button(row2_buttons, text='Sair', command=self.quit_application, width=15, style='W.TButton', image=img_sair, compound='left')
        button_6.image = img_sair
        button_6.pack(side=tk.RIGHT, padx=2,pady=2)
        
    def open_database(self):
        try:
            self.db = shelve.open(self.DB_FILE, writeback=True)
            self.logger.debug(f'Base de dados encontrada {self.db}')
        except Exception as e:
            self.show_error_message('Ocorreu um erro ao tentar abrir a base de dados',
                                    f'Erro na função open_database(): {str(e)}')

    def close_database(self):
        try:
            if self.db is not None:
                self.db.close()
        except Exception as e:
            self.show_error_message('Erro ao tentar fechar a base de dados',
                                    f'Erro na função close_database(): {str(e)}')

    def show_error_message(self, title, message):
        messagebox.showerror(title=title, message=message)
        self.logger.exception(message)


    def setup_logging(self):
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.DEBUG)

        formatter = logging.Formatter('%(asctime)s [%(levelname)s] %(message)s')

        file_handler = logging.FileHandler(self.LOG_FILE)
        file_handler.setFormatter(formatter)

        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(formatter)

        self.logger.addHandler(file_handler)
        self.logger.addHandler(stream_handler)

    def fetch_record(self):
        try:
            self.open_database()
            key = self.entries['key'].get()
            self.logger.debug(f'Pegando o registro da chave {key}')
            if key in self.db:
                record = self.db[key]
                for field in self.fieldnames:
                    value = repr(getattr(record, field))
                    self.entries[field].delete(0, tk.END)
                    self.entries[field].insert(0, value)
            else:
                messagebox.showinfo(title='Informação', message=f'A chave "{key}" não existe na base de dados.')
                self.logger.debug(f'Erro na função fetch_record(), chave {key} não encontrada')

        except Exception as e:
            self.show_error_message(f'Ocorreu um erro na função fetch_record(): {e}')
        finally:
            self.close_database()

    def confirm_update_record(self):
        confirmed = messagebox.askyesno("Confirme", "Tem a certeza que pretende Criar ou Atualizar o registo?")
        if confirmed:
            self.update_record()


    def update_record(self):
        try:
            self.open_database()
            key = self.entries['key'].get()
            if key in self.db.keys():
                record = self.db[key]
            else:
                record = Person(nome='?', idade='?', morada='?', telefone=0, email='?', rede_social='?', pais='?', nacionalidade='?',
                            doc_identificacao=0, nif=0)

            for field in self.fieldnames:
                user_input = self.entries[field].get()
                if user_input:
                    try:
                        if field in ('idade', 'doc_identificacao', 'nif', 'telefone'):
                            value = int(user_input)
                        elif field in ('nome', 'email', 'rede_social', 'morada', 'pais', 'nationalidade'):
                            value = str(user_input).strip("'")
                        else:
                            value = user_input.strip("'")

                        setattr(record, field, value)
                    except (ValueError, TypeError) as e:
                        messagebox.showinfo(title='ERRO', message='Erro convertendo o valor introduzido no campo')
                        self.logger.exception(
                            f'Erro na função update_record(), convertendo o valor introduzido no campo {field}: {e}')
                        return

            self.db[key] = record
        except Exception as e:
            messagebox.showerror(title='ERRO', message=f'Ocorreu um erro enquanto Criava ou Atualizava o registo')
            self.logger.exception(f'Ocorreu um erro na função update_record(), ao criar ou atualizar o registo: {e}')
        finally:
            self.close_database()


    def confirm_clear_board(self):
        confirmed = messagebox.askyesno("Confirme", "Tem a certeza que pretende limpar todos os campos ?")
        if confirmed:
            self.clean_board()

    def clean_board(self):
        try:
            for field in self.fieldnames:
                self.entries[field].delete(0, tk.END)
        except Exception as e:
            self.logger.debug(f'Erro na função clean_board(): {e}')

    def confirm_delete_record(self):
        confirmed = messagebox.askyesno("Confirme", "Tem a certeza que pretende apagar o registo ?")
        if confirmed:
            self.delete_record()

    def delete_record(self):
        self.open_database()
        try:
            key = self.entries['key'].get()
            if key in self.db.keys():
                del self.db[key]
                messagebox.showinfo(title='Apagar!!!', message=f'{key} Apagado!!')
            else:
                messagebox.showerror(title='Erro', message='A chave não existe na base de dados!')
        except Exception as e:
            self.logger.exception(f'Erro na função delete_record(): {e}')
        self.close_database()

    def show_record_info(self, record):
        self.open_database()
        for field in self.fieldnames:
            info_text = repr(getattr(record, field))
            self.entries[field].delete(0, tk.END)
            self.entries[field].insert(0, info_text)
        self.close_database()

    def confirm_clear_board(self):
        confirmed = messagebox.askyesno("Confirme", "Tem a certeza que pretende limpar todos os campos ?")
        if confirmed:
            self.clean_board()

    def quit_application(self):
        self.close_database()
        self.master.destroy()