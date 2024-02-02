import shelve

class Storage:
    def __init__(self):
        try:
            if not open('/basedados/database.db'):
                self.__database = shelve.open('/basedados/database')
                
        except Exception as e:
            print('Erro algo correu mal! =>',e)
        

    
    def get_object(self, key):
        self.__database = shelve.open('/basedados/database')
        for i in self.__database:
            if key == i:
                object = self.__database[key]
                self.__database.close()
                return object
        return None
    
    def save_to_storage(self,object):
        self.__database = shelve.open('/basedados/database')
        obj = object
        name = object.get_name()
        self.__database[name] = obj
        self.__database.close()

    def load_storage(self):
        self.__database = shelve.open('/basedados/database')
        return self.__database