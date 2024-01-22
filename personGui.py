import tkinter as tk
from person import Person
from tkinter import messagebox
import shelve
import ast 
from tkinter import ttk

class PersonGui(tk.Frame):
    def __init__(self, master, controller):
        super().__init__(master)
        self.controller = controller
        self.shelveName = '/Volumes/Programing/VSCode_Projects/programing_python_book/5_step_Adding_GUI/pratica_conhecimento/MyEnterprise/person_database'
        self.fieldnames = ('name', 'age', 'adress', 'phone', 'email','social_network', 'country', 'nacionality', 'doc_ident', 'nif', 'height', 'weight')
        self.entries = {}
        self.db = shelve.open(self.shelveName, writeback=True)  # Open the database
        self.label = tk.Label(self, text='Person Interface')
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
            

        # Buttons row
        tk.Button(self, text='Fetch', command=self.fetch_record).pack(side=tk.LEFT, padx=5,pady=20)
        tk.Button(self, text='Create|Update', command=self.confirm_update_record).pack(side=tk.LEFT, padx=5,pady=20)
        tk.Button(self, text='Delete', command=self.confirm_delete_record).pack(side=tk.LEFT, padx=5, pady=20)
        tk.Button(self, text='Clear', command=self.clean_board).pack(side=tk.RIGHT, padx=5,pady=20)
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
            record = Person(name='?', age='?', adress='?', phone=0, email='?',social_network='?', country='?', nacionality='?',
                            doc_ident=0, nif=0, height=0, weight=0)

        for field in self.fieldnames:
            """ # must use safer way then eval to evaluate records
            try:
                value = eval(self.entries[field].get())
            except Exception as e:
                messagebox.showerror(title='ERROR', message=f'Error evaluating input: {e}\n\nYou probably left an empty field or typed an iinvalid character')
                return """
            
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