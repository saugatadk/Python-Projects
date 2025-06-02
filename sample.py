#wap to add only positive numbers from user if negative skip and if zero exit the loop

sum = 0;
while True:
    num = int(input("Enter a number: "));
    
    if num < 0:
        print("Negative number entered. Enter a positive number");
        continue
    elif num == 0:
        print("Zero entered. Exiting the program");
        break;
    else:
        sum += num;
        print("Current sum:", sum);
print("Final sum of positive numbers:", sum);