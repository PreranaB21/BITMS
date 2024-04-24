n=str(input("Enter name"))
for i in range(len(n)):
    for j in range(len(n)):
        if(i==j and i<len(n)/2 or i+j==len(n)-1):
            print(n[i],end=' ')
        else:
            print(" ",end=' ')
    print()
