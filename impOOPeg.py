# Using objects as Arguments
# creating the Test class

class Test:


   def __init__(self, a):

       self.attr1 = a


   def call_me(self, obj):

       print(self.attr1)   # 1

       print(obj.attr1)   # 100


# object t1 of the Test class

t1 = Test(1)

t2 = Test(100)


t1.call_me(t2)

#Inside the call_me() method, self takes the t1 object and obj takes the t2 object.








# Return Objects From Methods

# creating the Test class

class Test:


   def __init__(self, a):

       self.attr1 = a


   def call_me(self):

       # creating a new object

       t2 = Test(1000)

       return t2


# object t1 of the Test class

t1 = Test(1)


result = t1.call_me()

print(result.attr1)   # 1000

#Inside the call_me() method, we have created a new object t2. The attr1 attribute of this object is 1000.
# Then, we have returned the t2 object which is assigned to the result variable (outside of the class).