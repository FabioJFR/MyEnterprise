from classes.candidate import Candidate
import tkinter as tk
from tkinter import messagebox, ttk, filedialog
import shelve
import ast
import subprocess
import logging


class CandidateGui(tk.Frame):
    """GUI for managing candidate records."""
    def __init__(self, master, controller):
        """
        Initialize the CandidateGui.

        Parameters:
        - master (tk.Tk): The parent Tkinter window.
        - controller: The controller for managing interactions.
        - shelve_name (str): The name of the shelve database file.
        """
        super().__init__(master)
        self.controller = controller
        self.shelve_name = 'basedados/candidate_database'
        self.fieldnames = ('nome', 'idade', 'candidatura', 'telefone', 'email', 'rede_social', 'morada', 'pais', 'nacionalidade', 'data', 'estado', 'doc_identificacao', 'nif', 'curriculo')
        self.entries = {}
        self.db = None
        padding = 10
        img_candidate = tk.PhotoImage(file='imagens/candidate_25x25.png')
        self.label = ttk.Label(self, text='Candidatos', font=('Verdana', 12, 'bold'), image=img_candidate, compound='left')
        self.label.image = img_candidate
        self.label.config(padding=(padding,0,padding,0))
        self.label.pack(pady=10,padx=10)
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
        L = tk.Label(text_frame, text='Chaves disponiveis', font=('Verdana', 12, 'bold'))
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
            messagebox.showerror(title='ERRO', message='Erro ao tentar abrir a base de dados.')
            logging.exception(f'1->Erro na função open_database(): {str(e)}')
    


    def close_database(self):
        """
            Close the shelve database.
        """
        try:
            if self.db is not None:
                self.db.close()
        except Exception as e:
            messagebox.showerror(title='ERRO', message='Ocorreu um erro ao fechar a base de dados.')
            logging.exception(f'2->Ocorreu um erro na função close_database() ao fechar a base de dados: {str(e)}')

    
    def fetch_record(self):
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
                    logging.debug(f'fech_record -> {self.entries}')
            else:
                messagebox.showinfo(title='Informação', message=f'A chave "{key}" não existe.')
                logging.debug(f'Chave {key} não encontrada')
        except Exception as e:
            messagebox.showerror(title='ERRO', message=f'Ocorreu um erro')
            logging.exception(f'3->Ocorreu um erro na função fetch_record(): {e}')
        finally:
            self.close_database()


    def confirm_update_record(self):
        confirmed = messagebox.askyesno("Confirmação", "Tem a certeza que pretende Criar/Atualizar o registo?")
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
                record = Candidate(nome='?', idade='?', candidatura='?', telefone=0, email='?', rede_social='?',morada='?', pais='?', nacionalidade='?', data='', estado='?', doc_identificacao=0, nif=0, curriculo='?')

            for field in self.fieldnames:
                # Use safer alternative ast.literal_eval instead of eval for user input
                user_input = self.entries[field].get()
                if user_input:
                    try:
                        if field in ('idade', 'doc_identificacao', 'nif', 'telefone'):
                            value = int(user_input)
                        elif field in ('nome', 'candidatura', 'email', 'rede_social', 'morada', 'pais', 'data', 'estado', 'nacionalidade'):
                            value = str(user_input).strip("'")
                        else:
                            value = user_input.strip("'")

                        setattr(record, field, value)
                    except (ValueError, TypeError) as e:
                        messagebox.showinfo(title='ERRO', message='Erro convertendo o valor introduzido no campo')
                        logging.exception(f'4->Erro na função update_record(), convertendo o valor introduzido no campo {field}: {e}')
                        return

            self.db[key] = record
        except Exception as e:
            messagebox.showerror(title='ERRO', message='Ocorreu um erro enquanto Criava ou Atualizava o registo')
            logging.exception(f'5->Erro na função update_record(): {e}')
        finally:
            self.close_database()


    def clean_board(self):
        for field in self.fieldnames:
            self.entries[field].delete(0, tk.END)

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
                messagebox.showerror(title='Erro', message='A chave não existe na base de dados')
        except Exception as e:
            logging.exception(f'6->Erro na função delete_record(): {e}')
        finally:
            self.close_database()

    def show_record_info(self, record):
        self.open_database()
        for field in self.fieldnames:
            info_text = repr(getattr(record, field))
            self.entries[field].delete(0, tk.END)
            self.entries[field].insert(0, info_text)
        self.close_database()

    def confirm_clear_board(self):
        confirmed = messagebox.askyesno("Confirmação", "Tem a certeza que pretende limpar os campos ?")
        if confirmed:
            self.clean_board()

    def select_resume(self):
        try:
            file_path = filedialog.askopenfilename(title='Selecionar Curriculo', filetypes=[('PDF Files', '*.pdf')])
            if file_path:
                self.entries['curriculo'].delete(0, tk.END)
                self.entries['curriculo'].insert(0, f"'{file_path}'")
        except Exception as e:
            logging.exception(f'7->Erro na função select_resume(): {e}')

    def open_resume_external(self):
        try:
            # Get the resume field value (file path)
            resume_path = ast.literal_eval(self.entries['curriculo'].get())
            if resume_path:
                # Use subprocess to open the file in the default PDF viewer
                subprocess.run(['open', resume_path], check=True)
        except (FileNotFoundError,Exception) as e:
            messagebox.showerror(title='Erro', message='Ocorreu um erro ao tentar abrir o Curriculo')
            logging.exception(f'8->Ocorreu um erro na função open_resume_external(), ao abrir o curriculo: {e}')
    

    """ # para windows (we use the os library)
    def select_resume(self):
        try:
            file_path = filedialog.askopenfilename(title='Seleccione o curriculo:', filetypes=[('PDF Files', '*.pdf')])
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
            resume_path = self.entries['curriculo'].get().strip("'")
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
        self.entries['curriculo'].delete(0, tk.END)
        self.entries['curriculo'].insert(0, file_path) """


    def setup_logging(self):
        logging.basicConfig(level=logging.DEBUG,  # Set the logging level
                    format='%(asctime)s [%(levelname)s] %(message)s',
                    handlers=[logging.FileHandler('logs/candidategui.log'), logging.StreamHandler()])
