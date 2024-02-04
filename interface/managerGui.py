import tkinter as tk
from tkinter import messagebox, ttk, filedialog
import shelve
import ast
from classes.manager import Manager
import subprocess
import logging

class ManagerGui(tk.Frame):
    def __init__(self, master, controller):
        super().__init__(master)
        self.controller = controller
        self.shelve_name = 'basedados/manager_database'
        self.fieldnames = ( 'name', 'age', 'job','phone', 'email','social_network', 'section', 'pay', 'adress', 'country', 'nacionality', 'doc_ident', 'nif', 'start_date', 'end_date', 'resume')
        self.entries = {}
        self.db = None
        self.label = tk.Label(self, text='Chefia', font=('Verdana', 12, 'bold'))
        self.label.pack(pady=10)
        self.setup_logging()
        self.make_widgets()
        

    def make_widgets(self):
        self.open_database()
        form = tk.Frame(self)
        form.pack(fill='both')

        # Labels column
        for i, label in enumerate(('key',) + self.fieldnames):
            tk.Label(form, text=label, font=('Verdana', 10, 'bold')).grid(row=i, column=0, pady=2, sticky='e')

        # Entries column
        for i, label in enumerate(('key',) + self.fieldnames):
            ent = ttk.Entry(form)
            ent.grid(row=i, column=1, pady=2, padx=(0, 10), sticky='w')
            self.entries[label] = ent

        # Text field column - available keys
        # Text area with scrollbar
        text_frame = tk.Frame(form)
        text_frame.grid(row=0, column=2, rowspan=len(self.fieldnames) + 1, padx=(10, 0), pady=5, sticky='nsew')
        L = tk.Label(text_frame, text='Available keys', font=('Verdana', 10, 'bold'))
        L.grid(row=0, column=0, pady=1, padx=2,sticky='nesw')
        text_area = tk.Text(text_frame, height=20, width=10, wrap='word', font=('Verdana', 10, 'bold'))
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
        button_1 = ttk.Button(row1_buttons, text='Criar|Atualizar', command=self.confirm_update_record, width=17, style='W.TButton')
        button_1.pack(side=tk.LEFT, padx=2,pady=2)
        button_2 = ttk.Button(row1_buttons, text='Mostrar Campos', command=self.fetch_record, width=17, style='W.TButton')
        button_2.pack(side=tk.LEFT, padx=2,pady=2)
        button_3 = ttk.Button(row1_buttons, text='Selecionar Curriculo', command=self.select_resume, width=17, style='W.TButton')
        button_3.pack(side=tk.RIGHT, padx=2,pady=2)

        # Buttons row 2
        row2_buttons = tk.Frame(self)
        row2_buttons.pack()
        button_6 = ttk.Button(row2_buttons, text='Apagar', command=self.confirm_delete_record, width=17, style='W.TButton')
        button_6.pack(side=tk.LEFT, padx=2,pady=2)
        button_5 =ttk.Button(row2_buttons, text='Limpar Campos', command=self.confirm_clear_board, width=17, style='W.TButton')
        button_5.pack(side=tk.LEFT, padx=2,pady=2)
        button_4 = ttk.Button(row2_buttons, text='Abrir Curriculo', command=self.open_resume_external, width=17, style='W.TButton')
        button_4.pack(side=tk.RIGHT, padx=2,pady=2)
        
        # Buttons row 3
        row3_buttons = tk.Frame(self)
        row3_buttons.pack(side=tk.BOTTOM)
        button_7 = ttk.Button(row3_buttons, text='Menu Principal', command=self.controller.show_mainGui, width=26, style='W.TButton')
        button_7.pack(side=tk.LEFT, padx=5,pady=2)
        button_8 = ttk.Button(row3_buttons, text='Sair', command=self.quit, width=25, style='W.TButton')
        button_8.pack(side=tk.RIGHT, padx=5,pady=2)


    def open_database(self):
        """
            Open the shelve database and assign it to self.db.
            Display an error message if an exception occurs.
        """
        try:
            self.db = shelve.open(self.shelve_name, writeback=True)
            logging.debug(f'Base de dados encontrada {self.db}')
        except Exception as e:
            messagebox.showerror(title='ERRO', message='Ocorreu um erro ao tentar abrir a base de dados')
            logging.exception(f'1->Erro na fução open-database(): {str(e)}')
    

    def close_database(self):
        """Close the shelve database."""
        try:
            if self.db is not None:
                self.db.close()
        except Exception as e:
            messagebox.showerror(title='ERRO', message='Erro ao tentar fechar a base de dados')
            logging.exception(f'2->Erro na função close_database(): {str(e)}')


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

                for field in self.fieldnames:
                    value = repr(getattr(record, field))
                    self.entries[field].delete(0, tk.END)
                    self.entries[field].insert(0, value)

            else:
                messagebox.showinfo(title='Informação', message=f'A chave "{key}" não existe na base de dados.')
                logging.debug(f'3->Erro na função fetch_record(), chave {key} não encontrada')

        except Exception as e:
            messagebox.showerror(title='ERRO', message='Ocorreu um erro.')
            logging.exception(f'4->Ocorreu um erro na função fetch_record(): {e}')

        finally:
            self.close_database()


    def confirm_update_record(self):
        confirmed = messagebox.askyesno("Confirme", "Tem a certeza que pretende Criar ou Atualizar o registo?")
        if confirmed:
            self.update_record()


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
                
            else:
                record = Manager(name='?', age='?', job='?', adress='?', phone='?', email='?',social_network='?', country='?', nacionality='?', doc_ident='?', nif='?', pay='?', section='?', start_date='?', end_date='?', resume='?')

            for field in self.fieldnames:
                # Use safer alternative ast.literal_eval instead of eval for user input
                user_input = self.entries[field].get()
                if user_input:
                    try:
                        if field in ('age', 'doc_ident', 'nif', 'phone'):
                            value = int(user_input)
                        elif field in ('pay'):
                            value = float(user_input)
                        elif field in ('name', 'job', 'email', 'social_network', 'address', 'country', 'date', 'start_date', 'end_date', 'section', 'nationality', 'resume'):
                            value = str(user_input).strip("'")
                        else:
                            value = user_input.strip("'")

                        setattr(record, field, value)
                    except (ValueError, TypeError) as e:
                        messagebox.showinfo(title='ERRO', message='Erro convertendo o valor introduzido no campo')
                        logging.exception(f'5->Erro na função update_record(), convertendo o valor introduzido no campo {field}: {e}')
                        return

            self.db[key] = record
        except Exception as e:
            messagebox.showerror(title='ERRO', message=f'Ocorreu um erro enquanto Criava ou Atualizava o registo')
            logging.exception(f'6->Ocorreu um erro na função update_record(), ao criar ou atualizar o registo: {e}')
        finally:
            self.close_database()


    def clean_board(self):
        try:
            for field in self.fieldnames:
             self.entries[field].delete(0, tk.END)
        except Exception as e:
            logging.debug(f'7->Erro na função clean_board(): {e}')


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
            logging.exception(f'8->Erro na função delete_record(): {e}')
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


    def select_resume(self):
        try:
            file_path = filedialog.askopenfilename(title='Selecionar curriculo:', filetypes=[('PDF Files', '*.pdf')])
            if file_path:
                self.entries['resume'].delete(0, tk.END)
                self.entries['resume'].insert(0, f"'{file_path}'")
        except Exception as e:
            messagebox.showerror(title='Erro!', message='Erro ao selecionar o arquivo, deve ser do tipo PDF.')
            logging.exception(f'9->Erro na função select_resume(): {e}')


    def open_resume_external(self):
        try:
            # Get the resume field value (file path)
            resume_path = ast.literal_eval(self.entries['resume'].get())
            if resume_path:
                # Use subprocess to open the file in the default PDF viewer
                subprocess.run(['open', resume_path], check=True)
        except (FileNotFoundError,Exception) as e:
            messagebox.showerror(title='Error', message='Ocorreu um erro ao tentar abrir o curriculo.')
            logging.exception(f'10->Ocorreu um erro na função open_resume_external(), ao tentar abrir o curriculo. {e}')
    

    """ # para windows (we use the os library)
    def select_resume(self):
        try:
            file_path = filedialog.askopenfilename(title='Select Resume', filetypes=[('PDF Files', '*.pdf')])
            if file_path:
                self.update_resume_entry(file_path)
        except FileNotFoundError as e:
            messagebox.showerror(title='Error', message='File not found.')
            logging.exception(f'Error in select_resume(): {e}')
        except Exception as e:
            messagebox.showerror(title='Error', message='An error occurred while selecting the resume.')
            logging.exception(f'Error in select_resume(): {e}')


    def open_resume_external(self):
        try:
            resume_path = self.entries['resume'].get().strip("'")
            if resume_path:
                os.startfile(resume_path)
        except FileNotFoundError as e:
            messagebox.showerror(title='Error', message='File not found.')
            logging.exception(f'Error in open_resume_external(): {e}')
        except Exception as e:
            messagebox.showerror(title='Error', message='An error occurred while opening the resume.')
            logging.exception(f'Error in open_resume_external(): {e}')


    def update_resume_entry(self, file_path):
        # Remove single quotes if present
        file_path = file_path.strip("'")
        self.entries['resume'].delete(0, tk.END)
        self.entries['resume'].insert(0, file_path) """


    def setup_logging(self):
        logging.basicConfig(level=logging.DEBUG,  # Set the logging level
                    format='%(asctime)s [%(levelname)s] %(message)s',
                    handlers=[logging.FileHandler('logs/managergui.log'), logging.StreamHandler()])