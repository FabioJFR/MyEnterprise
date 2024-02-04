from classes.manager import Manager

class Employee(Manager):
    def __init__(self, nome='?', idade=0, profissao='?', morada='?', telefone=0, email='?', rede_social='?', pais='?', nacionalidade='?', doc_identificacao=0, nif=0, salario=0.0, seccao='?', data_inicio='?', data_fim='?', curriculo='?'):
        super().__init__(profissao, salario, seccao, data_inicio, data_fim, curriculo, nome, idade, morada, telefone, email, rede_social, pais, nacionalidade, doc_identificacao, nif)


    def get_class_type(self):
        return self.__class__.__name__

if __name__ == '__main__':
    staff1 = Employee(nome='pedro',idade=29,nacionalidade='Portugues',pais='Portugal',telefone=345678231,email='pedro@mail.com',rede_social='facebook',morada='portalegre',doc_identificacao=345987234,nif=98074532,profissao='janitor',salario=17000,seccao='staff',data_inicio='15-05-2015',data_fim='000000',curriculo='resume.txt')

    print(staff1)
    print(staff1.get_person_details())
    print(staff1.get_company_details())
    staff1.giveRaise(0.10,0)
    print(staff1.get_company_details())
    staff1.__nome= 'ivo'
    staff1.__idade = 56
    print(staff1.get_person_details())
    staff1.set_idade(34)
    print(staff1.get_person_details())