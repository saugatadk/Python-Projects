# try:
#     numerator = int(input("Enter numerator: "))
#     denominator = int(input("Enter denominator: "))

#     result = numerator/denominator

#     print(result)
# except:
#     print("Denominator cannot be 0. Try again.")
    
    
    

#In the program, the ZeroDivision exception occurs first because of this code result = 5/0. Hence, the except ZeroDvisionError: block is executed.    

try:
    result = 5/0
    print(result)
    
    my_list = [1, 2, 3]
    print(my_list[20])
except ZeroDivisionError:
    print("Denominator cannot be 0.")
except IndexError:
    print("Index is wrong.")


# A try statement can also have an optional finally block which is executed regardless of whether an exception occurs or not. For example,    
try:
    print(1/0)
except:
    print("Wrong denominator")
finally:
    print("Always printed")