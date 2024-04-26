n=int(input("Enter number"))
if n % 2 != 0:
    print("werid")
    pass
elif n % 2 == 0 and range(2,5):
        print("Not werid")
        pass
elif n % 2 == 0 and range(6,21) :
    print("werid")
    pass
elif n % 2 == 0 and n>20:
    print("Not werid")
    pass
else:
    print("Enter a valid number")
