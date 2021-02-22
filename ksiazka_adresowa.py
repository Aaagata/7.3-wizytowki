class Person:
    def __init__(self, name, surname, private_mail, company, job_title, company_mail):
       self.name = name
       self.surname = surname
       self.private_mail = private_mail
       self.company = company
       self.job_title = job_title
       self.company_mail = company_mail
    def __str__(self):
        return f"{self.name} {self.surname}, {self.private_mail}, {self.company}: {self.job_title}, {self.company_mail}"
p1 = Person("Alicja", "Walczak", "aa@o2.pl", "Budimex", "Dyrektor Finansowy", "a.w@wp.pl")
p2 = Person("Olga", "Lipińska", "oo@o2.pl", "TVP", "Reżyser", "o.l@wp.pl")
p3 = Person("Roman","Bratny", "rr@o2.pl", "PGE","Główny Księgowy","r.b@wp.pl")
p4 = Person("Marek","Waszczuk", "mm@o2.pl", "SztormGrupa","CEO", "m.w@wp.pl")
p5 = Person("Bjork", "Johansson", "bb@o2.pl", "IKEA", "Account Manager", "b.j@wp.pl")
people_list = [p1, p2, p3, p4, p5]
def fake_data():
    from faker import Faker
    fake = Faker()
    name, surname = fake.name().split()
    return Person(name=name, surname=surname, company=fake.company(), job_title=fake.job(), private_mail=fake.email(), company_mail=fake.email())
people_list.append(fake_data())
for i in people_list:
    print(i)