class BaseContact:
    def __init__(self, name, surname, private_mail):
       self.name = name
       self.surname = surname
       self.private_mail = private_mail  
    def __str__(self):
        return f"Kontaktuję się z {self.name} {self.surname} i piszę e-mail na adres: {self.private_mail}"
p1 = BaseContact("Alicja", "Walczak", "aa@o2.pl")
p2 = BaseContact("Olga", "Lipińska", "oo@o2.pl")
p3 = BaseContact("Roman","Bratny", "rr@o2.pl")
p4 = BaseContact("Marek","Waszczuk", "mm@o2.pl")
p5 = BaseContact("Bjork", "Johansson", "bb@o2.pl")
people_list = [p1, p2, p3, p4, p5]
def fake_data():
    from faker import Faker
    fake = Faker()
    name, surname = fake.name().split()
    return BaseContact(name=name, surname=surname, private_mail=fake.email())
people_list.append(fake_data())
#dane podstawowe
for i in people_list:
    print(i)
class BusinessContact(BaseContact):
    def __init__(self, company, job_title, company_phone, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.company = company
        self.job_title = job_title
        self.company_phone = company_phone
# p1 = BaseContact("Alicja", "Walczak", "aa@o2.pl", "Budimex", "Dyrektor Finansowy", "+48221231212")
# p2 = BaseContact("Olga", "Lipińska", "oo@o2.pl", "TVP", "Reżyser", "+48226424242")
# p3 = BaseContact("Roman","Bratny", "rr@o2.pl", "PGE","Główny Księgowy", "+48228832211")
# p4 = BaseContact("Marek","Waszczuk", "mm@o2.pl", "SztormGrupa","CEO", "+48606332211")
# p5 = BaseContact("Bjork", "Johansson", "bb@o2.pl", "IKEA", "Account Manager", "+4672323456")
def fake_data():
    from faker import Faker
    fake = Faker()
    name, surname = fake.name().split()
    return BusinessContact(name=name, surname=surname, private_mail=fake.email(), company=fake.company(), job_title=fake.job(), company_phone=fake.ssn())
def contact(self):
    return(f"Dzwonię do {self.name}{self.surname} z firmy {self.company} pod numer {self.company_phone}")
people_list.append(fake_data())
#dane służbowe
for i in people_list:
    print(contact)
