print("Welcome to Calculator")
print("Enter:")
print("1 to add")
print("2 to subtract")
print("3 to multiply")
print("4 to divide")

while True:
    choice = input("enter your choice(1/2/3/4): ")
    num1 = input("enter number 1: ")
    num2 = input("enter  number 2: ")

    num1 = int(num1)
    num2 = int(num2)

    if choice == "1":
        a = num1+num2
        a = str(a)

        num1 = str(num1)
        num2 = str(num2)
        print(num1 ,'+', num2 ,"=",a)

    if choice == '2':
        a = num1 - num2
        a = str(a)

        num1 = str(num1)
        num2 = str(num2)
        print(num1 ,"-", num2+"=",a)

    if choice == "3":
        a = num1*num2
        try:
            a = str(a)
        except Exception as e:
            print(e)
        num1 = str(num1)
        num2 = str(num2)
        print(num1,"*",num2+"=",a)

    if choice == "4":
        a = num1/num2
        try:
            a = str(a)
        except Exception as e:
            print(e)
        num1 = str(num1)
        num2 = str(num2)
        print(num1,"/",num2,"=",a)

    again = input("Do u want to use calculator once more(yes or no): ")
    if again == "no":
            break
    if again == "yes":
            continue
