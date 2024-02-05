from classes.person import Person


class Manager(Person):
    """
    -> classe Manage que herda da classe Person
    -> são adicionados mais uns atributos que diferem da classe Person
    -> novos metodos adicionados
    -> todos os atributos são privados
    """
    def __init__(self, profissao='?',salario=0.0,seccao='?',data_inicio=0, data_fim=0, curriculo='=', nome='?', idade=0,morada='?',telefone=0,email='?',rede_social='?', pais='?', nacionalidade='?', doc_identificacao=0, nif=0):
        self.__profissao = profissao
        self.__salario = salario
        self.__seccao = seccao
        self.__data_inicio = data_inicio
        self.__data_fim = data_fim
        self.__curriculo = curriculo
        
        super().__init__(nome, idade, morada, telefone, email, rede_social, pais, nacionalidade, doc_identificacao, nif)
        
    def __str__(self):
        return '%s =>\n Nome: %s, Idade: %i, Profissão: %s, Salario: %.2f, Secção: %s, Data Inicio: %s, Data Fim: %s, Curriculo: %s, Morada: %s, Telefone: %i, Email: %s, Rede Social: %s, Pais: %s , Nationalidade: %s, Doc. Identiificação: %i, NIF: %i' % (self.__class__.__name__,super().get_nome(),super().get_idade(),self.__profissao,self.__salario,self.__seccao,self.__data_inicio,self.__data_fim,self.__curriculo,super().get_morada(),super().get_telefone(), super().get_email(),super().get_rede_social(), super().get_pais(),super().get_nacionalidade(),super().get_doc_id(),super().get_nif())
    
    def get_profissao(self):
        return self.__profissao
    
    def set_profissao(self, profissao):
        self.__profissao = profissao
    
    
    def get_salario(self):
        return self.__salario
    
    def set_salario(self, salario):
        self.__salario = salario

    
    def get_seccao(self):
        return self.__seccao
    
    def set_seccao(self, seccao):
        self.__seccao = seccao


    def get_data_inicio(self):
        return self.__data_inicio
    
    def set_data_inicio(self, data):
        self.__data_inicio = data

    
    def get_data_fim(self):
        return self.__data_fim
    
    def set_data_fim(self, data):
        self.__data_fim = data

    
    def get_curriculo(self):
        return self.__curriculo
    
    def set_curriculo(self, curriculo):
        self.__curriculo = curriculo

    def giveRaise(self,percent,bonus):
        self.__salario *= (1.0+percent+bonus)


    def get_class_type(self):
        return self.__class__.__name__



    #TODO falta a base de dados para procurar o manager pretendido
    def get_company_details(self):
        return '%s =>\n Nome: %s, Profissão: %s, Salário: %.2f, Secção: %s, Data Inicio: %s, Data Fim: %s, Curriculo: %s' % (self.__class__.__name__,super().get_nome(),self.__profissao,self.__salario,self.__seccao,self.__data_inicio,self.__data_fim,self.__curriculo)

    def get_person_details(self):
        return '%s =>\n Nome: %s, Idade: %i, Morada: %s, Telefone: %i, Email: %s, Rede Social: %s, País: %s, Nationalidade: %s, Doc. Identificação: %i, NIF: %i' % (self.__class__.__name__, super().get_nome(), super().get_idade(), super().get_morada(), super().get_telefone(), super().get_email(), super().get_rede_social(),super().get_pais(), super().get_nacionalidade(), super().get_doc_id(), super().get_nif())
