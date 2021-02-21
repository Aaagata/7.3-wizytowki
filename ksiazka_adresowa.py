class Person:
    def __init__(self, name, surname, company, job_title, mail):
       self.name = name
       self.surname = surname
       self.company = company
       self.job_title = job_title
       self.mail = mail
    def __str__(self):
        return f"{self.name} {self.surname}, {self.mail}, {self.company}: {self.job_title}"
p1 = Person("Alicja", "Walczak", "Budimex", "Dyrektor Finansowy", "a.w@wp.pl")
p2 = Person("Olga", "Lipińska","TVP", "Reżyser", "o.l@wp.pl")
p3 = Person("Roman","Bratny","PGE","Główny Księgowy","r.b@wp.pl")
p4 = Person("Marek","Waszczuk","SztormGrupa","CEO", "m.w@wp.pl")
p5 = Person("Bjork", "Johansson", "IKEA", "Account Manager", "b.j@wp.pl")
people_list = [p1, p2, p3, p4, p5]
def fake_data():
    from faker import Faker
    fake = Faker()
    name, surname = fake.name().split()
    return Person(name=name, surname=surname, company=fake.company(), job_title=fake.job(), mail=fake.email())
people_list.append(fake_data())
for i in people_list:
    print(i)