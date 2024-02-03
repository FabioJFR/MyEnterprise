import shelve

db = shelve.open('basedados/manager_database')

for key in db:
    print(f'Chave: {key} Conteudo: {db[key]}')