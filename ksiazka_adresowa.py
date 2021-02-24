class BaseContact:
    def __init__(self, name, surname, private_mail):
       self.name = name
       self.surname = surname
       self.private_mail = private_mail  
    def __str__(self):
        return f"Kontaktuję się z {self.name} {self.surname} i piszę e-mail na adres: {self.private_mail}"
    @property
    def label_lenght(self):
        self.label_lenght = len(self.name) + len(self.surname)
        return self.label_lenght    
def fake_data():
    from faker import Faker
    fake = Faker()
    name, surname = fake.name().split()
    return BaseContact(name=name, surname=surname, private_mail=fake.email())

p1 = BaseContact("Alicja", "Walczak", "aa@o2.pl")
p2 = BaseContact("Olga", "Lipińska", "oo@o2.pl")
p3 = BaseContact("Roman","Bratny", "rr@o2.pl")
p4 = BaseContact("Marek","Waszczuk", "mm@o2.pl")
p5 = BaseContact("Bjork", "Johansson", "bb@o2.pl")
people_list = [p1, p2, p3, p4, p5]
people_list.append(fake_data())

class BusinessContact(BaseContact):
    def __init__(self, company, job_title, company_phone, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.company = company
        self.job_title = job_title
        self.company_phone = company_phone
    def contact():
        print(f"Dzwonię do {self.name} {self.surname} z firmy {self.company} pod numer telefonu: {self.company_phone}")
def fake_data2():
    from faker import Faker
    fake = Faker()
    name, surname = fake.name().split()
    return BusinessContact(name=name, surname=surname, private_mail=fake.email(), company=fake.company(), job_title=fake.job(), company_phone=fake.ssn())
p1 = BusinessContact("Alicja", "Walczak", "aa@o2.pl", "Budimex", "Dyrektor Finansowy", "+48221231212")
p2 = BusinessContact("Olga", "Lipińska", "oo@o2.pl", "TVP", "Reżyser", "+48226424242")
p3 = BusinessContact("Roman","Bratny", "rr@o2.pl", "PGE","Główny Księgowy", "+48228832211")
p4 = BusinessContact("Marek","Waszczuk", "mm@o2.pl", "SztormGrupa","CEO", "+48606332211")
p5 = BusinessContact("Bjork", "Johansson", "bb@o2.pl", "IKEA", "Account Manager", "+4672323456")
people_list = [p1, p2, p3, p4, p5]
people_list.append(fake_data2())
for i in people_list:
    print(i)
