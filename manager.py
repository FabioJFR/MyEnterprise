from person import Person
from storage import Storage



class Manager(Person):
    """
    -> classe Manage que herda da classe Person
    -> são adicionados mais uns atributos que diferem da classe Person
    -> novos metodos adicionados
    -> todos os atributos são privados
    """
    def __init__(self, job=None,pay=0,section=None,start_date=0, end_date=0, resume=None, name=None, age=None,adress=None,phone=None,email=None,social_network=None, country=None, nacionality=None, doc_ident=0, nif=0, height=0, weight=0):
        self.__job = job
        self.__pay = pay
        self.__section = section
        self.__start_date = start_date
        self.__end_date = end_date
        self.__resume = resume
        
        super().__init__(name, age, adress, phone, email, social_network, country, doc_ident, nif, nacionality, height, weight)
        
    def __str__(self):
        return '%s =>\n Name: %s, Age: %i, Job: %s, Pay: %.2f, Section: %s, Start Date: %s, End Date: %s, Resume: %s, Adress: %s, Phone: %i, Email: %s,Social Network: %s, Country: %s, ID: %i, NIF: %i, Nationality: %s, Height: %.2f, Weight: %.2f' % (self.__class__.__name__,super().get_name(),super().get_age(),self.__job,self.__pay,self.__section,self.__start_date,self.__end_date,self.__resume,super().get_adress(),super().get_phone(), super().get_email(),super.get_social_network(), super().get_coutry(),super().get_id(),super().get_nif(),super().get_nacionality(),super().get_height(),super().get_weight())
    
    def get_job(self):
        return self.__job
    
    
    def get_pay(self):
        return self.__pay
    
    def set_pay(self, pay):
        self.__pay = pay

    
    def get_section(self):
        return self.__section
    
    def set_section(self, section):
        self.__section = section


    def get_data_inicio(self):
        return self.__start_date
    
    def set_data_inicio(self, data):
        self.__start_date = data

    
    def get_data_fim(self):
        return self.__end_date
    
    def set_data_fim(self, data):
        self.__end_date = data

    
    def get_resume(self):
        return self.__resume
    
    def set_resume(self, resume):
        self.__resume = resume

    def giveRaise(self,percent,bonus):
        self.__pay *= (1.0+percent+bonus)


    def get_class_type(self):
        return self.__class__.__name__



    #TODO falta a base de dados para procurar o manager pretendido
    def get_company_details(self):
        return '%s =>\n Name: %s, Job: %s, Pay: %.2f, Section: %s, Start Date: %s, End Date: %s, Resume: %s' % (self.__class__.__name__,super().get_name(),self.__job,self.__pay,self.__section,self.__start_date,self.__end_date,self.__resume)

    def get_person_details(self):
        return '%s =>\n Name: %s, Age: %i, Adress: %s, Phone: %i, Email: %s, Social Network: %s, Country: %s, ID: %i, NIF: %i, Nationality: %s, Height: %.2f, Weight: %.2f ' % (self.__class__.__name__, super().get_name(), super().get_age(), super().get_adress(), super().get_phone(), super().get_email(), super.get_social_network(),super().get_coutry(), super().get_id(), super().get_nif(), super().get_nacionality(), super().get_height(), super().get_weight())



if __name__ == '__main__':
    pessoa = Person('Fabio', 45,'valdoca',912345678, 'email@email.com','facebook','portugal',12345,54321,'portugues',1.74, 72)
    print(pessoa)
    """ pessoa.set_name('luid')
    print(pessoa.get_name())
    pessoa.__name = 'davi'
    print(pessoa.get_name())
    print(pessoa.get_age())
    print(pessoa) """

    manager = Manager('manager',60000,'software','jan-12-2024','00000','resume.txt', 'Xavier',60,'Aljustrel',912345678,'mail@mail.pt', 'facebook','Portugal',5545,462424,'Portuguese',1.85,87.9)
    print(manager)
    print(manager.get_job())
    manager.giveRaise(0.20,0)
    print(manager)
    manager1 = Manager(name='joao',age=70,job='finances',phone=123456789,email='joao@mail.com',social_network='facebook',resume='resume.txt',pay=45000,section='human resources',start_date='23-12-2018',end_date=000000, adress='Beja', country='portugal',doc_ident=98765, nif=123456,nacionality='Espanhol',height=1.69,weight=70)
    print(manager.get_company_details())
    print(manager1)
    print(manager1.get_person_details())

    print("saving stage")
    db = Storage()
    db.save_to_storage(pessoa)
    db.save_to_storage(manager1)

    print("\nLoading stage")
    bd = Storage()
    bd = bd.load_storage()
    for key in bd:
        print('\n')
        print(bd[key])

    print('\nGet keys stage')
    for key in bd:
        print(key)

    print('\nGet obbject stage')
    sd =Storage()
    print(sd.get_object('Fabio'))
    a = (sd.get_object('joao'))
    print('\n')
    print(a.get_job(), a.__class__.__doc__)




