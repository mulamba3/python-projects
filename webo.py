class Person():
    def __init__(self, first, middle, last, age, sex, occupation, nation):
        self.f_name = first
        self.m_name = middle
        self.l_name = last
        self.full_name = first+" "+middle+" "+last
        self.age = age
        self.sex = sex
        self.occupation = occupation
        self.nation = nation
        
    def make_email(self):
        email = self.f_name+self.l_name+"@gmail.com"
        return email
    
    def name(self):
        name = self.f_name+" "+self.m_name+" "+self.l_name
        return name

    def nationality(self):
        nationality = self.nation
        return nationality

    def work(self):
        work = self.occupation
        return work
    
    def gendar(self):
        gendar = self.sex
        return gendar

P1 = Person("alex", "mugo", "wahome", 18, "male", "reciptionist", "kenya")
P2 =Person("brian", "john", "canter", 30, "male", "songwriter", "american")
P3 = Person("ann", "alex", "dragovick", 26, "female","hacker", "russian")  

print(P1.make_email())
print(P1.name())
print(P1.nationality())
print(P1.work())
print(P1.gendar())