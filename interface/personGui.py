import tkinter as tk
from classes.person import Person
from tkinter import messagebox
import shelve
import ast 
from tkinter import ttk
import logging


class PersonGui(tk.Frame):
    def __init__(self, master, controller, shelve_name='basedados/person_database'):
        super().__init__(master)
        self.controller = controller
        self.shelveName = shelve_name
        self.fieldnames = ('name', 'age', 'adress', 'phone', 'email','social_network', 'country', 'nacionality', 'doc_ident', 'nif', 'height', 'weight')
        self.entries = {}
        self.db = shelve.open(self.shelveName, writeback=True)  # Open the database
        self.label = tk.Label(self, text='Person Interface')
        self.label.pack(pady=10)
        self.make_widgets()
        self.setup_logging()


    def make_widgets(self):
        form = tk.Frame(self)
        form.pack()

        # Labels column
        for i, label in enumerate(('key',) + self.fieldnames):
            tk.Label(form, text=label).grid(row=i, column=0, pady=3.7, sticky='e')

        # Entries column
        for i, label in enumerate(('key',) + self.fieldnames):
            ent = ttk.Entry(form)
            ent.grid(row=i, column=1, pady=3.7, padx=(0, 10), sticky='w')
            self.entries[label] = ent

        # Text field collumn - available keys
        # Text area with scrollbar
        text_frame = tk.Frame(form)
        text_frame.grid(row=0, column=2, rowspan=len(self.fieldnames) + 1, padx=(10, 0), pady=10, sticky='nsew')
        L = tk.Label(text_frame, text='Available keys')
        L.grid(row=0, column=0, pady=1,padx=2, sticky='nesw')
        text_area = tk.Text(text_frame, height=30, width=8, wrap='word')
        text_area.grid(row=1, column=0, sticky='nsew')
        scrollbar = tk.Scrollbar(text_frame, command=text_area.yview)
        scrollbar.grid(row=1, column=1, sticky='ns')
        text_area.config(yscrollcommand=scrollbar.set, state='normal')
        for key in self.db:
            text_area.insert(index=tk.END, chars=f'{key}\n')
            text_area.tag_configure('center', justify='center')
            text_area.tag_add('center', 1.0, 'end')
        text_area.config(state='disabled') 

        # Buttons row 1
        row1_buttons = tk.Frame(self)
        row1_buttons.pack(side=tk.TOP)
        tk.Button(row1_buttons, text='Menu Principal', command=self.controller.show_mainGui, width=12).pack(side=tk.LEFT, padx=1)
        tk.Button(row1_buttons, text='Criar|Atualizar', command=self.confirm_update_record, width=12).pack(side=tk.LEFT, padx=1)
        tk.Button(row1_buttons, text='Pegar', command=self.fetch_record, width=12).pack(side=tk.LEFT, padx=1)

        # Buttons row 2
        row2_buttons = tk.Frame(self)
        row2_buttons.pack(side=tk.BOTTOM)
        tk.Button(row2_buttons, text='Apagar', command=self.confirm_delete_record, width=20).pack(side=tk.LEFT, padx=1)
        tk.Button(row2_buttons, text='Limpar', command=self.confirm_clear_board, width=20).pack(side=tk.RIGHT, padx=1)
        
        
    def open_database(self):
        """
            Open the shelve database and assign it to self.db.
            Display an error message if an exception occurs.
        """
        try:
            self.db = shelve.open(self.shelve_name, writeback=True)
            logging.debug(f'Base de dados encontrada {self.db}')
        except Exception as e:
            messagebox.showerror(title='ERRO', message='Ocorreu um erro ao abrir a base de dados.')
            logging.exception(f'1->Ocorreu um erro na função open_database() ao abrir a base de dados: {str(e)}')
    

    def close_database(self):
        """Close the shelve database."""
        try:
            if self.db is not None:
                self.db.close()
        except Exception as e:
            messagebox.showerror(title='ERRO', message='Ocorreu um erro ao fechar a base de dados.')
            logging.exception(f'2->Ocorreu um erro na função close_database() ao fechar a base de dados: {str(e)}')


    def fetch_record(self):
        """
        Fetch a candidate record from the shelve database based on the provided key.
        Display the record information or an error message.
        """
        try:
            self.open_database()
            key = self.entries['key'].get()
            logging.debug(f'Pegando o registo da chave {key}')

            if key in self.db:
                record = self.db[key]
                logging.debug(f'Registo encontrado {record}')

                for field in self.fieldnames:
                    value = repr(getattr(record, field))
                    self.entries[field].delete(0, tk.END)
                    self.entries[field].insert(0, value)

            else:
                messagebox.showinfo(title='Informação', message=f'A chave "{key}" não existe.')
                logging.debug(f'Chave {key} não encontrada')

        except Exception as e:
            messagebox.showerror(title='ERRO', message='Ocorreu um erro')
            logging.exception(f'3->Ocorreu um erro na função fetch_record(): {e}')

        finally:
            self.close_database()



    def confirm_update_record(self):
        confirmed = messagebox.askyesno("Confirme", "Tem a certeza que pretende Criar ou Atualizar o registo?")
        if confirmed:
            self.update_record()


    """ def update_record(self):
        try:
            self.db = shelve.open(self.shelveName, writeback=True) 
            key = self.entries['key'].get()
        except Exception as e:
            messagebox.showerror(title='ERROR', message=f'An error was raised: {e}')
        if key in self.db.keys():
            record = self.db[key]
        else:
            record = Person(name='?', age='?', adress='?', phone=0, email='?',social_network='?', country='?', nacionality='?',
                            doc_ident=0, nif=0, height=0, weight=0)

        for field in self.fieldnames: 
            # Use safer alternative ast.literal_eval instead of eval for user input
            try:
                value = ast.literal_eval(self.entries[field].get())
            except (SyntaxError, ValueError) as e:
                messagebox.showerror(title='ERROR', message=f'Error evaluating input: {e}')
                return
            setattr(record, field, value)

        self.db[key] = record
        self.db.close() """

    def update_record(self):
        """
        Update or create a candidate record in the shelve database based on user input.
        Displays an error message if an exception occurs during the update process.
        """
        try:
            self.open_database()

            key = self.entries['key'].get()
            if key in self.db.keys():
                record = self.db[key]
                logging.debug(f'Função update_record() - pegou o record.\n {record}')
            else:
                record = Person(name='?', age='?', adress='?', phone=0, email='?',social_network='?', country='?', nacionality='?',
                            doc_ident=0, nif=0, height=0, weight=0)

            for field in self.fieldnames:
                # Use safer alternative ast.literal_eval instead of eval for user input
                user_input = self.entries[field].get()
                if user_input:
                    try:
                        if field in ('age', 'doc_ident', 'nif', 'phone'):
                            value = int(user_input)
                        elif field in ('height', 'weight'):
                            value = float(user_input)
                        elif field in ('name', 'email', 'social_network', 'address', 'country', 'nationality'):
                            value = str(user_input).strip("'")
                        else:
                            value = user_input.strip("'")

                        setattr(record, field, value)
                    except (ValueError, TypeError) as e:
                        messagebox.showinfo(title='ERRO', message=f'Erro convertendo o valor introduzido no campo')
                        logging.exception(f'4->Erro na função update_record(), convertendo o valor introduzido no campo {field}: {e}')
                        return

            self.db[key] = record
        except Exception as e:
            messagebox.showerror(title='ERRO', message=f'Ocorreu um erro enquanto Criava ou Atualizava o registo')
            logging.exception(f'5->Ocorreu um erro na função update_record(), enquanto criava ou atualizava o registo: {e}')
        finally:
            self.close_database()


    def clean_board(self):
        for field in self.fieldnames:
            self.entries[field].delete(0, tk.END)


    def confirm_delete_record(self):
        confirmed = messagebox.askyesno("Confirme", "Tem a certeza que pretende apagar o registo?")
        if confirmed:
            self.delete_record()


    def delete_record(self):
        try:
            self.open_database()
            key = self.entries['key'].get()
        except ValueError as e:
            messagebox.showerror(title='Informação', message=f'Introduza uma chave que pretenda apagar.')
            logging.exception(f'6->Erro na função delete_record(), nenhuma chave intruduzida para apagar: {e}')
        if key in self.db.keys():
            del self.db[key]
            messagebox.showinfo(title='Apagar!!!' ,message=f'{key} Apagado!!')
            self.close_database()

    
    def confirm_clear_board(self):
        confirmed = messagebox.askyesno("Confirme", "Tem a certeza que pretende limpar todos os campos ?")
        if confirmed:
            self.clean_board()


    def setup_logging(self):
        logging.basicConfig(level=logging.DEBUG,  # Set the logging level
                    format='%(asctime)s [%(levelname)s] %(message)s',
                    handlers=[logging.FileHandler('logs/person.log'), logging.StreamHandler()])