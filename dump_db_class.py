import shelve

db = shelve.open('/Volumes/Programing/VSCode_Projects/programing_python_book/5_step_Adding_GUI/pratica_conhecimento/main/manager_database')

for key in db:
    print(key)