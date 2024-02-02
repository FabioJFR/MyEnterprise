# classe pessoa - dados relativos a uma pessoa
import inspect
class Person():
    def __init__(self, name=None, age=None,adress=None,phone=None,email=None,social_network=None,country=None,nacionality = None, doc_ident=0, nif=0, height=0.0, weight=0.0):
        self.__name = name
        self.__age = age
        self.__adress = adress
        self.__phone = phone
        self.__email = email
        self.__social_network = social_network
        self.__country = country
        self.__doc_ident = doc_ident
        self.__nif = nif
        self.__nacionality = nacionality
        self.__height = height
        self.__weight = weight

    #def __str__(self):
     #   return '%s =>\n Name: %s, Age: %i, Adress: %s, Phone: %i, Email: %s, Country: %s, ID: %i, NIF: %i, Nationality: %s, Height: %.2f, Weight: %.2f' % (self.__class__.__name__,self.name,self.age,self.adress,self.phone,self.email,self.country,self.doc_ident,self.nif,self.nacionality,self.height,self.weight)


    
    def get_name(self):
        return self.__name
    
    def set_name(self, name): 
        self.__name = name

    
    def get_age(self):
        return self.__age
    
    def set_age(self, age):
        self.__age = age

    
    def get_adress(self):
        return self.__adress

    def set_adress(self, adress):
        self.__adress = adress

    
    def get_social_network(self):
        return self.__social_network
    
    def set_social_network(self, social_network):
        self.__social_network = social_network

    
    def get_phone(self):
        return self.__phone
    
    def set_Phone(self, phone):
        self.__phone = phone
    

    def get_email(self):
        return self.__email
    
    def set_email(self, email):
        self.__email = email

    
    def get_coutry(self):
        return self.__country
    
    def set_coutry(self, country):
        self.__country = country

    
    def get_id(self):
        return self.__doc_ident
    
    def set_ID(self, id):
        self.__doc_ident = id

    
    def get_nif(self):
        return self.__nif
    
    def set_nif(self, nif):
        self.__nif = nif


    def get_nacionality(self):
        return self.__nacionality
    
    def set_nacionality(self, nacionality):
        self.__nacionality = nacionality

    
    def get_height(self):
        return self.__height
    
    def set_height(self, height):
        self.__height = height


    def get_weight(self):
        return self.__weight
    
    def set_weight(self, weight):
        self.__weight = weight

    
    def get_class_type(self):
        return self.__class__.__name__

    
    def get_atribute_names(self):
        private_attributes = [att for att in dir(self) if '_' not in att]
        a = []
        for i in private_attributes:
            #print(i)
            #s = i.split('_Person')
            a.append(i)
        return a

    

if __name__ == '__main__':
    pessoa = Person('Fabio',43,"Aljustrel",123456789,'fabio@mail.pt','facebook','Portugal',123456,987654,'Portugal',1.74,70.4)
    #print(pessoa.__name)
    pessoa.set_name('luid')
    print(pessoa.get_name())
    print(pessoa.get_name())
    c = pessoa.name = 'davi'
    print(pessoa.get_name())

    print(pessoa.get_age())
    pessoa.set_age(50)
    print(pessoa.get_age())
    x = pessoa.age = 60
    print(pessoa.age)
 

    print(pessoa)

    a = pessoa.get_name()

    print(a)
    print(x)
    print(c)

    b = pessoa.get_class_type()
    print(b)
    print(type(b))
    
    print('################get_atributes_names#####################')
    print(pessoa.get_atribute_names())
    
    

