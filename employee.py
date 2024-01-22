from manager import Manager

class Employee(Manager):
    def __init__(self, name=None, age=None, job=None, adress=None, phone=0, email=None,social_network=None, country=None, nacionality=None, doc_ident=0, nif=0, pay=0.0, section=None, start_date=0, end_date=0, resume=None, height=0, weight=0):
        super().__init__(job, pay, section, start_date, end_date, resume, name, age, adress, phone, email,social_network, country, doc_ident, nif, nacionality, height, weight)


    def get_class_type(self):
        return self.__class__.__name__

if __name__ == '__main__':
    staff1 = Employee(name='pedro',age=29,nacionality='Portugues',country='Portugal',phone=345678231,email='pedro@mail.com',social_network='facebook',adress='portalegre',doc_ident=345987234,nif=98074532,height=1.70,weight=65.4,job='janitor',pay=17000,section='staff',start_date='15-05-2015',end_date='000000',resume='resume.txt')

    print(staff1)
    print(staff1.get_person_details())
    print(staff1.get_company_details())
    staff1.giveRaise(0.10,0)
    print(staff1.get_company_details())
    staff1.__name= 'ivo'
    staff1.__age = 56
    print(staff1.get_person_details())
    staff1.set_age(34)
    print(staff1.get_person_details())