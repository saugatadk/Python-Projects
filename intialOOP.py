class Student:


    # add a method to check pass/fail

    def check_pass_fail(self):

        if self.score >= 40:

            return True

        else:

            return False


# create object

student1 = Student()


# add attributes

student1.name = 'Harry'

student1.score = 85



# call the check_pass_fail() method

# calling this method using student1 object

did_pass = student1.check_pass_fail()



print(did_pass)