n=str(input("Enter name"))
for i in range(len(n)):
    for j in range(len(n*2)):
        if i==j or i+j==len(n)*2-1:
            print(n[i],end=' ')
        else:
            print(' ',end=' ') 
    print()