class Person():
    def __init__(self, nome='?', idade=0,morada='?',telefone=0,email='?',rede_social='?',pais='?',nacionalidade ='?', doc_identificacao=0, nif=0):
        self.__nome = nome
        self.__idade = idade
        self.__morada = morada
        self.__telefone = telefone
        self.__email = email
        self.__rede_social = rede_social
        self.__pais = pais
        self.__doc_identificacao = doc_identificacao
        self.__nif = nif
        self.__nacionalidade = nacionalidade
        

    def __str__(self):
        return '%s =>\n Nome: %s, Idade: %i, Morada: %s, Telefone: %i, Email: %s, Rede Social: %s, País: %s, Nationalidade: %s, ID: %i, NIF: %i' % (self.__class__.__name__, self.__nome, self.__idade, self.__morada, self.__telefone, self.__email, self.__rede_social, self.__pais, self.__nacionalidade, self.__doc_identificacao, self.__nif)


    def get_nome(self):
        return self.__nome
    
    def set_nome(self, nome): 
        self.__nome = nome

    
    def get_idade(self):
        return self.__idade
    
    def set_idade(self, idade):
        self.__idade = idade

    
    def get_morada(self):
        return self.__morada

    def set_morada(self, morada):
        self.__morada = morada

    
    def get_rede_social(self):
        return self.__rede_social
    
    def set_rede_social(self, rede_social):
        self.__rede_social = rede_social

    
    def get_telefone(self):
        return self.__telefone
    
    def set_telefone(self, telefone):
        self.__telefone = telefone
    

    def get_email(self):
        return self.__email
    
    def set_email(self, email):
        self.__email = email

    
    def get_pais(self):
        return self.__pais
    
    def set_pais(self, pais):
        self.__pais = pais

    
    def get_doc_id(self):
        return self.__doc_identificacao
    
    def set_doc_id(self, doc_id):
        self.__doc_identificacao = doc_id

    
    def get_nif(self):
        return self.__nif
    
    def set_nif(self, nif):
        self.__nif = nif


    def get_nacionalidade(self):
        return self.__nacionalidade
    
    def set_nacionalidade(self, nacionalidade):
        self.__nacionalidade = nacionalidade

    
    def get_class_type(self):
        return self.__class__.__name__

    
    def get_atribute_names(self):
        private_attributes = [att for att in dir(self) if '_' not in att]
        a = []
        for i in private_attributes:
            print(i)
            #s = i.split('_Person')
            a.append(i)
        return a
    