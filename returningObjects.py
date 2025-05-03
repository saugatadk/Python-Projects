class Person:

    def __init__(self, name, age):

        self.name = name

        self.age = age


    def return_another_person(self):


        # creating an object of the Person class

        person = Person('Sara', 20)

        

        # returning the object

        return person


# create an object

person1 = Person('Ana', 21)


another_person = person1.return_another_person()

print(another_person.name)    # Sara

print(another_person.age)    # 20