import shelve
from classes.employee import Employee
from classes.person import Person
from classes.manager import Manager
from classes.candidate import Candidate



if __name__ == '__main__':
    db = shelve.open('basedados/manager_database')

    for key in db:
        print(f'Chave: {key} Conteudo: {db[key]}')

    
    # person tests
    pessoa = Person(nome='Fabio',idade=43,morada="Aljustrel",telefone=123456789,email='fabio@mail.pt',rede_social='facebook',pais='Portugal',doc_identificacao=123456,nif=987654,nacionalidade='Portuguesa')
    #print(pessoa.__name)
    pessoa.set_nome('luid')
    print(pessoa.get_nome())
    print(pessoa.get_nome())
    c = pessoa.nome = 'davi'
    print(pessoa.get_nome())

    print(pessoa.get_idade())
    pessoa.set_idade(50)
    print(pessoa.get_idade())
    x = pessoa.idade = 60
    print(pessoa.idade)
    print(pessoa)
    a = pessoa.get_nome()
    print(a)
    print(x)
    print(c)
    b = pessoa.get_class_type()
    print(b)
    print(type(b))
    print('################get_atributes_names#####################')
    print(pessoa.get_atribute_names())
    

    # manager test
    manager = Manager('manager',60000,'software','jan-12-2024','00000','resume.txt', 'Xavier',60,'Aljustrel',912345678,'mail@mail.pt', 'facebook','Portugal','Portuguese',5545,462424)
    print(manager)
    print(manager.get_profissao())
    manager.giveRaise(0.20,0)
    print(manager)
    manager1 = Manager(nome='joao',idade=70,profissao='finances',telefone=123456789,email='joao@mail.com',rede_social='facebook',curriculo='resume.txt',salario=45000,seccao='human resources',data_inicio='23-12-2018',data_fim=000000, morada='Beja', pais='portugal',doc_identificacao=98765, nif=123456,nacionalidade='Espanhol')
    print(manager.get_company_details())
    print(manager1)
    print(manager1.get_person_details())

    # employee testes
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

    # candidae tests
    candidate1 = Candidate(nome='Ivo',idade=35,candidatura='operations',telefone=23456,email='mail.pt',rede_social='facebook',curriculo='curriculo.pdf',morada='Aljustrel',pais='portugal', data='12-03-2020', estado='pending',doc_identificacao=12345,nif=746582,nacionalidade='portuguesa')
    print(candidate1)
    candidate1.get_curriculo()
    print(candidate1.get_curriculo())
    print(candidate1.get_data())
    print(candidate1.get_estado())
    print(candidate1.get_nome())
    print(candidate1)
