import tkinter as tk
from tkinter import messagebox, ttk, filedialog
import shelve
import ast
from employee import Employee
import subprocess

class EmployeeGui(tk.Frame):
    def __init__(self, master, controller):
        super().__init__(master)
        self.controller = controller
        self.shelveName = '/Volumes/Programing/VSCode_Projects/programing_python_book/5_step_Adding_GUI/pratica_conhecimento/MyEnterprise/employee_database'
        self.fieldnames = ('name', 'age', 'job', 'adress', 'phone', 'email','social_network', 'country', 'nacionality', 'doc_ident', 'nif', 'pay', 'section', 'start_date', 'end_date', 'height', 'weight', 'resume')
        self.entries = {}
        self.db = None
        self.label = tk.Label(self, text='Candidate Interface')
        self.label.pack(pady=10)
        self.make_widgets()

    def make_widgets(self):
        self.open_database()
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

        # Text field column - available keys
        # Text area with scrollbar
        text_frame = tk.Frame(form)
        text_frame.grid(row=0, column=2, rowspan=len(self.fieldnames) + 1, padx=(10, 0), pady=10, sticky='nsew')
        L = tk.Label(text_frame, text='Available keys')
        L.grid(row=0, column=0, pady=1, padx=2, sticky='nesw')
        text_area = tk.Text(text_frame, height=30, width=8, wrap='word')
        text_area.grid(row=1, column=0, sticky='nsew')
        scrollbar = tk.Scrollbar(text_frame, command=text_area.yview)
        scrollbar.grid(row=1, column=1, sticky='ns')
        text_area.config(yscrollcommand=scrollbar.set, state='normal')
        for key in self.db:
            text_area.insert(index=tk.END, chars=f'{key}\n')
        text_area.config(state='disabled')

        # Buttons row
        tk.Button(self, text='Main Menu', command=self.controller.show_mainGui).pack(side=tk.RIGHT, padx=5, pady=20)
        tk.Button(self, text='Create|Update', command=self.confirm_update_record).pack(side=tk.LEFT, padx=5, pady=20)
        tk.Button(self, text='Fetch', command=self.fetch_record).pack(side=tk.LEFT, padx=5, pady=20)
        tk.Button(self, text='Delete', command=self.confirm_delete_record).pack(side=tk.LEFT, padx=5, pady=20)
        tk.Button(self, text='Clear', command=self.confirm_clear_board).pack(side=tk.RIGHT, padx=5, pady=20)
        tk.Button(self, text='Select Resume', command=self.select_resume).pack(side=tk.RIGHT, padx=5, pady=20)
        tk.Button(self, text='Open Resume', command=self.open_resume_external).pack(side=tk.RIGHT, padx=5, pady=20)
        

    def open_database(self):
        try:
            self.db = shelve.open(self.shelveName, writeback=True)
        except Exception as e:
            messagebox.showerror(title='ERROR', message=f'An error occurred while opening the database: {e}')

    def close_database(self):
        try:
            if self.db is not None:
                self.db.close()
        except Exception as e:
            messagebox.showerror(title='ERROR', message=f'An error occurred while closing the database: {e}')

    def fetch_record(self):
        self.open_database()

        key = self.entries['key'].get()
        try:
            record = self.db[key]
            self.show_record_info(record)
        except KeyError:
            messagebox.showerror(title='Error', message='No such key!')
        finally:
            self.close_database()

    def confirm_update_record(self):
        confirmed = messagebox.askyesno("Confirmation", "Are you sure you want to create/update the record?")
        if confirmed:
            self.update_record()

    def update_record(self):
        self.open_database()

        key = self.entries['key'].get()
        if key in self.db.keys():
            record = self.db[key]
        else:
            record = Employee(name='?', age='?', job='?', adress='?', phone='?', email='?',social_network='?', country='?', nacionality='?', doc_ident='?', nif='?', pay='?', section='?', start_date='?', end_date='?', height='?', weight='?', resume='?')

        for field in self.fieldnames:
            # Use safer alternative ast.literal_eval instead of eval for user input
            try:
                value = ast.literal_eval(self.entries[field].get())
            except (SyntaxError, ValueError) as e:
                messagebox.showerror(title='ERROR', message=f'Error evaluating input: {e}')
                return
            setattr(record, field, value)

        self.db[key] = record
        self.close_database()

    def clean_board(self):
        for field in self.fieldnames:
            self.entries[field].delete(0, tk.END)

    def confirm_delete_record(self):
        confirmed = messagebox.askyesno("Confirmation", "Are you sure you want to delete the record?")
        if confirmed:
            self.delete_record()

    def delete_record(self):
        self.open_database()

        key = self.entries['key'].get()
        if key in self.db.keys():
            del self.db[key]
            messagebox.showinfo(title='Delete!!!', message=f'{key} Deleted!!')
        else:
            messagebox.showerror(title='Error', message='No such key!')

        self.close_database()

    def show_record_info(self, record):
        self.open_database()
        for field in self.fieldnames:
            info_text = repr(getattr(record, field))
            self.entries[field].delete(0, tk.END)
            self.entries[field].insert(0, info_text)
        self.close_database()

    def confirm_clear_board(self):
        confirmed = messagebox.askyesno("Confirmation", "Are you sure you want to clear the board?")
        if confirmed:
            self.clean_board()

    def select_resume(self):
        file_path = filedialog.askopenfilename(title='Select Resume', filetypes=[('PDF Files', '*.pdf')])
        if file_path:
            self.entries['resume'].delete(0, tk.END)
            self.entries['resume'].insert(0, f"'{file_path}'")


    def open_resume_external(self):
        try:
            # Get the resume field value (file path)
            resume_path = ast.literal_eval(self.entries['resume'].get())
            if resume_path:
                # Use subprocess to open the file in the default PDF viewer
                subprocess.run(['open', resume_path], check=True)
        except Exception as e:
            messagebox.showerror(title='Error', message=f'An error occurred while opening the resume: {e}')




""" import tkinter as tk 
from employee import Employee
from tkinter import messagebox
import shelve
import ast 
from tkinter import ttk

class EmployeeGui(tk.Frame):
    def __init__(self, master, controller):
        super().__init__(master)
        self.controller = controller
        self.shelveName = '/Volumes/Programing/VSCode_Projects/programing_python_book/5_step_Adding_GUI/pratica_conhecimento/MyEnterprise/employee_database'
        self.fieldnames = ('name', 'age', 'job', 'adress', 'phone', 'email','social_network', 'country', 'nacionality', 'doc_ident', 'nif', 'pay', 'section', 'start_date', 'end_date', 'height', 'weight', 'resume')
        self.entries = {}
        self.db = shelve.open(self.shelveName, writeback=True)
        self.label = tk.Label(self, text='Employee Interface')
        self.label.pack(pady=10)
        self.make_widgets()
        self.controller.setup_logging()

    def make_widgets(self):
        form = tk.Frame(self)
        form.pack()

        for i, label in enumerate(('key',) + self.fieldnames):
            tk.Label(form, text=label).grid(row=i, column=0, pady=3.7, sticky='e')

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
        text_area.config(state='disabled')

        tk.Button(self, text='Fetch', command=self.fetch_record).pack(side=tk.LEFT, padx=5, pady=20)
        tk.Button(self, text='Create|Update', command=self.confirm_update_record).pack(side=tk.LEFT, padx=5,pady=20)
        tk.Button(self, text='Delete', command=self.confirm_delete_record).pack(side=tk.LEFT, padx=5, pady=20)
        tk.Button(self, text='Clean', command=self.clean_board).pack(side=tk.RIGHT, padx=5, pady=20)
        tk.Button(self, text='Main Menu', command=self.controller.show_mainGui).pack(side=tk.RIGHT, padx=5, pady=20)

    def fetch_record(self):
        try:
            self.db = shelve.open(self.shelveName, writeback=True) 
            key = self.entries['key'].get()
        except Exception as e:
            messagebox.showerror(title='ERROR', message=f'An error was raised: {e}')
        try:
            record = self.db[key]
        except KeyError:
            messagebox.showerror(title='Error', message='No such key!')
        else:
            for field in self.fieldnames:
                self.entries[field].delete(0, tk.END)
                self.entries[field].insert(0, repr(getattr(record, field)))
        self.db.close()


    def confirm_update_record(self):
        confirmed = messagebox.askyesno("Confirmation", "Are you sure you want to create/update the record?")
        if confirmed:
            self.update_record()


    def update_record(self):
        try:
            self.db = shelve.open(self.shelveName, writeback=True) 
            key = self.entries['key'].get()
        except Exception as e:
            messagebox.showerror(title='ERROR', message=f'An error was raised: {e}')

        if key in self.db.keys():
            record = self.db[key]
        else:
            record = Employee(name='?', age='?', job='?', adress='?', phone='?', email='?',social_network='?', country='?', nacionality='?', doc_ident='?', nif='?', pay='?', section='?', start_date='?', end_date='?', height='?', weight='?', resume='?')

        for field in self.fieldnames:
            # Use safer alternative ast.literal_eval instead of eval for user input
            try:
                value = ast.literal_eval(self.entries[field].get())
            except (SyntaxError, ValueError) as e:
                messagebox.showerror(title='ERROR', message=f'Error evaluating input: {e}')
                return
            setattr(record, field, value)

        self.db[key] = record
        self.db.close()

    def clean_board(self):
        for field in self.fieldnames:
            self.entries[field].delete(0, tk.END)

    
    def confirm_delete_record(self):
        confirmed = messagebox.askyesno("Confirmation", "Are you sure you want to delete the record?")
        if confirmed:
            self.delete_record()


    def delete_record(self):
        try:
            self.db = shelve.open(self.shelveName, writeback=True) 
            key = self.entries['key'].get()
        except ValueError as e:
            messagebox.showerror(title='Information', message=f'Please sumply a key to delete: {e}')

        if key in self.db.keys():
            del self.db[key]
            messagebox.showinfo(title='Delete!!!' ,message=f'{key} Deleted!!')
            self.db.close()
 """

""" import tkinter as tk
from tkinter import ttk, filedialog, messagebox, Scrollbar, Text
import shelve
import ast
import PyPDF2
from employee import Employee

class EmployeeGui(tk.Frame):
    def __init__(self, master, controller):
        super().__init__(master)
        self.controller = controller
        self.shelveName = '/Volumes/Programing/VSCode_Projects/programing_python_book/5_step_Adding_GUI/pratica_conhecimento/MyEnterprise/employee_database'
        self.fieldnames = ('name', 'age', 'job', 'adress', 'phone', 'email','social_network', 'country', 'nacionality', 'doc_ident', 'nif', 'pay', 'section', 'start_date', 'end_date', 'height', 'weight', 'resume')
        self.entries = {}
        self.db = self.db = shelve.open(self.shelveName, writeback=True)
        self.label = tk.Label(self, text='Candidate Interface')
        self.label.pack(pady=10)
        self.make_widgets()

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

        # Text field column - available keys
        # Text area with scrollbar
        text_frame = tk.Frame(form)
        text_frame.grid(row=0, column=2, rowspan=len(self.fieldnames) + 1, padx=(10, 0), pady=10, sticky='nsew')
        L = tk.Label(text_frame, text='Available keys')
        L.grid(row=0, column=0, pady=1, padx=2, sticky='nesw')
        text_area = tk.Text(text_frame, height=30, width=8, wrap='word')
        text_area.grid(row=1, column=0, sticky='nsew')
        scrollbar = tk.Scrollbar(text_frame, command=text_area.yview)
        scrollbar.grid(row=1, column=1, sticky='ns')
        text_area.config(yscrollcommand=scrollbar.set, state='normal')
        for key in self.db:
            text_area.insert(index=tk.END, chars=f'{key}\n')
        text_area.config(state='disabled')

        # Buttons row
        tk.Button(self, text='Fetch', command=self.fetch_record).pack(side=tk.LEFT, padx=5, pady=20)
        tk.Button(self, text='Create|Update', command=self.confirm_update_record).pack(side=tk.LEFT, padx=5, pady=20)
        tk.Button(self, text='Delete', command=self.confirm_delete_record).pack(side=tk.LEFT, padx=5, pady=20)
        tk.Button(self, text='Clear', command=self.clean_board).pack(side=tk.RIGHT, padx=5,pady=20)
        tk.Button(self, text='Select Resume', command=self.select_resume).pack(side=tk.RIGHT, padx=5, pady=20)
        tk.Button(self, text='Main Menu', command=self.controller.show_mainGui).pack(side=tk.RIGHT, padx=5, pady=20)

    def open_database(self):
        try:
            self.db = shelve.open(self.shelveName, writeback=True)
        except Exception as e:
            messagebox.showinfo(title='ERROR', message=f'An error occurred while opening the database: {e}')

    def close_database(self):
        try:
            if self.db is not None:
                self.db.close()
        except Exception as e:
            messagebox.showinfo(title='ERROR', message=f'An error occurred while closing the database: {e}')

    def fetch_record(self):
        self.open_database()

        key = self.entries['key'].get()
        try:
            record = self.db[key]
            self.show_record_info(record)
        except KeyError:
            messagebox.showerror(title='Error', message='No such key!')
        finally:
            self.close_database()

    def confirm_update_record(self):
        confirmed = messagebox.askyesno("Confirmation", "Are you sure you want to create/update the record?")
        if confirmed:
            self.update_record()

    def update_record(self):
        self.open_database()

        key = self.entries['key'].get()
        if key in self.db.keys():
            record = self.db[key]
        else:
            record = Employee(name='?', age='?', job='?', adress='?', phone='?', email='?',social_network='?', country='?', nacionality='?', doc_ident='?', nif='?', pay='?', section='?', start_date='?', end_date='?', height='?', weight='?', resume='?')

        for field in self.fieldnames:
            if field == 'resume':
                # Handle the resume field separately by storing the PDF file content
                resume_path = self.entries['resume'].get()
                try:
                    with open(resume_path, 'rb') as resume_file:
                        pdf_content = resume_file.read()
                        setattr(record, field, pdf_content)
                except FileNotFoundError:
                    messagebox.showinfo(title='Error', message=f'Resume file not found: {resume_path}')
            else:
                # Use safer alternative ast.literal_eval instead of eval for user input
                try:
                    value = ast.literal_eval(self.entries[field].get())
                except (SyntaxError, ValueError) as e:
                    messagebox.showinfo(title='ERROR', message=f'Error evaluating input: {e}')
                    return
                setattr(record, field, value)

        self.db[key] = record
        self.close_database()

    def clean_board(self):
        for field in self.fieldnames:
            self.entries[field].delete(0, tk.END)

    def confirm_delete_record(self):
        confirmed = messagebox.askyesno("Confirmation", "Are you sure you want to delete the record?")
        if confirmed:
            self.delete_record()

    def delete_record(self):
        self.open_database()

        key = self.entries['key'].get()
        if key in self.db.keys():
            del self.db[key]
            messagebox.showinfo(title='Delete!!!', message=f'{key} Deleted!!')
        else:
            messagebox.showinfo(title='Error', message='No such key!')

        self.close_database()

    def select_resume(self):
        file_path = filedialog.askopenfilename(title='Select Resume', filetypes=[('PDF Files', '*.pdf')])
        if file_path:
            self.entries['resume'].delete(0, tk.END)
            self.entries['resume'].insert(0, file_path)

    def show_record_info(self, record):
        for field in self.fieldnames:
            if field == 'resume':
                # Display "Resume Attached" instead of showing the binary content
                info_text = "Resume Attached" if getattr(record, field) else ""
            else:
                info_text = repr(getattr(record, field))
            self.entries[field].delete(0, tk.END)
            self.entries[field].insert(0, info_text)

    def clean_board(self):
        for field in self.fieldnames:
            self.entries[field].delete(0, tk.END) """




            