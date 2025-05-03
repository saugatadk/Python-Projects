class Student:
    
    def __init__(self, name, score):
        self.name = name
        self.score = score
    
    def check_pass_fail(self):
        if self.score >= 40:
             return True
        else:
            return False

student1 = Student("Harry", 90)
did_pass = student1.check_pass_fail()
print(f"Did {student1.name} pass?", did_pass)

student2 = Student("Jaby", 8)
did_pass = student2.check_pass_fail()
print(f"Did {student2.name} pass?", did_pass)
