import shelve

class Storage:
    def __init__(self):
        try:
            if not open('/Volumes/Programing/VSCode_Projects/programing_python_book/5_step_Adding_GUI/pratica_conhecimento/main/storage/database.db'):
                self.__database = shelve.open('/Volumes/Programing/VSCode_Projects/programing_python_book/5_step_Adding_GUI/pratica_conhecimento/main/storage/database')
        except Exception as e:
            print('Erro algo correu mal! =>',e)
        

    
    def get_object(self, key):
        self.__database = shelve.open('/Volumes/Programing/VSCode_Projects/programing_python_book/5_step_Adding_GUI/pratica_conhecimento/main/database')
        for i in self.__database:
            if key == i:
                object = self.__database[key]
                self.__database.close()
                return object
        return None
    
    def save_to_storage(self,object):
        self.__database = shelve.open('/Volumes/Programing/VSCode_Projects/programing_python_book/5_step_Adding_GUI/pratica_conhecimento/main/database')
        obj = object
        name = object.get_name()
        self.__database[name] = obj
        self.__database.close()

    def load_storage(self):
        self.__database = shelve.open('/Volumes/Programing/VSCode_Projects/programing_python_book/5_step_Adding_GUI/pratica_conhecimento/main/database')
        return self.__database