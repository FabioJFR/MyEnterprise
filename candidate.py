from person import Person
from manager import Manager

class Candidate(Person):
    def __init__(self, name='?', age='?',aplying_job='?' ,phone=0, email='?',social_network='?', resume='?', adress='?', country='?', date='?', status='?', doc_ident=0, nif=0, nacionality='?', height=0, weight=0):
        self.__resume = resume
        self.__date = date
        self.__status = status
        self.__aplying_job = aplying_job
        super().__init__(name, age, adress, phone, email,social_network, country, doc_ident, nif, nacionality, height, weight)

    def get_resume(self):
        return self.__resume
        
    def set_resume(self, resume):
        resume = open(resume, 'r', encoding='utf-8')
        resume1= resume.read()
        path = f'/Volumes/Programing/VSCode_Projects/programing_python_book/5_step_Adding_GUI/pratica_conhecimento/MyEnterprise/resumes/{self.get_name()}_resume.pdf'
        resume2 = open(path, 'x')
        resume2.write(resume1)
        self.__resume = path
        resume.close()
        resume2.close()

    def set_aplying_job(self, aplying_job):
        self.__aplying_job = aplying_job
    
    def get_aplying_job(self):
        return self.__aplying_job

        
    def get_date(self):
        return self.__date
        
    def set_date(self, date):
        self.__date = date
        

    def get_status(self):
        return self.__status
        
    def set_status(self, status):
        self.__status = status

    
    def get_class_type(self):
        return self.__class__.__name__

        

if __name__ == '__main__':
    candidate1 = Candidate(name='Ivo',age=35,aplying_job='operations',phone=23456,email='mail.pt',social_network='facebook',resume=None,adress='Aljustrel',country='portugal', date='12-03-2020', status='pending',doc_ident=12345,nif=746582,nacionality='portuguesa',height=1.56, weight=70)
    candidate1.set_resume('/Volumes/Programing/VSCode_Projects/programing_python_book/5_step_Adding_GUI/pratica_conhecimento/MyEnterprise/resume.pdf')
    print(candidate1.get_resume())
    print(candidate1.get_date())
    print(candidate1.get_status())
    print(candidate1.get_name())
    print(candidate1)

    f = open('/Volumes/Programing/VSCode_Projects/programing_python_book/5_step_Adding_GUI/pratica_conhecimento/MyEnterprise/resume.pdf', 'r', encoding='utf-8')
    print(f.read())
   

    
    
    
    
