from classes.manager import Manager

class Employee(Manager):
    def __init__(self, nome='?', idade=0, profissao='?', morada='?', telefone=0, email='?', rede_social='?', pais='?', nacionalidade='?', doc_identificacao=0, nif=0, salario=0.0, seccao='?', data_inicio='?', data_fim='?', curriculo='?'):
        super().__init__(profissao, salario, seccao, data_inicio, data_fim, curriculo, nome, idade, morada, telefone, email, rede_social, pais, nacionalidade, doc_identificacao, nif)


    def get_class_type(self):
        return self.__class__.__name__

    