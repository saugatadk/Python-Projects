class Person:
    __slots__ = ['name', 'age']  # restricts attributes

    def __init__(self, name, age):
        self.name = name
        self.age = age

# Normal use
p = Person("Alice", 30)
print(p.name, p.age)

# Try to add a new attribute (will raise AttributeError) but this can be avoided by using __dict__ in the slots
# p.city = "Paris"  # This will fail!
