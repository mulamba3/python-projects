class Students():
    def __init__(self, name, id_num, age):
        self.name = name
        self.id_num = id_num
        self.age = age

x = Students("jacob owino", 102, 26)
print(x.name)
print(x.id_num)
print(x.age)


#we are creating another code different from the top code
#2
print("")
print("")
class Scores():
    def __init__(self, a, b):
        self.a = a
        self.b = b 


    def Total_sum(self):
        sum = self.a+self.b
        return sum

marks = Scores(100, 200)

print(marks.Total_sum())
