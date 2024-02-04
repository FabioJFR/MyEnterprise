from classes.person import Person


class Candidate(Person):
    def __init__(self, curriculo='?', data='?', estado='?',candidatura='?', nome='?', idade='?' ,telefone=0, email='?',rede_social='?', morada='?', pais='?', nacionalidade='?', doc_identificacao=0, nif=0):
        self.__curriculo = curriculo
        self.__data = data
        self.__estado = estado
        self.__candidatura = candidatura
        super().__init__(nome, idade, morada, telefone, email,rede_social, pais, nacionalidade, doc_identificacao, nif)

    def get_curriculo(self):
        return self.__curriculo
        


    def set_candidatura(self, candidatura):
        self.__candidatura = candidatura
    
    def get_candidatura(self):
        return self.__candidatura

        
    def get_data(self):
        return self.__data
        
    def set_data(self, data):
        self.__data = data
        

    def get_estado(self):
        return self.__estado
        
    def set_estado(self, estado):
        self.__estado = estado

    
    def get_class_type(self):
        return self.__class__.__name__

        

if __name__ == '__main__':
    candidate1 = Candidate(nome='Ivo',idade=35,candidatura='operations',telefone=23456,email='mail.pt',rede_social='facebook',curriculo='curriculo.pdf',morada='Aljustrel',pais='portugal', data='12-03-2020', estado='pending',doc_identificacao=12345,nif=746582,nacionalidade='portuguesa')
    print(candidate1)
    candidate1.get_curriculo()
    print(candidate1.get_curriculo())
    print(candidate1.get_data())
    print(candidate1.get_estado())
    print(candidate1.get_nome())
    print(candidate1)

    