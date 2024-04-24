n=str(input("Enter name"))
for i in range(len(n)):
    for j in range(len(n)):
        if i==0 or i==len(n) or i==len(n)-2 or i+j==len(n)-1:
            print(n[j],end=' ')
        else:
            print(' ',end=' ')
    print()
if(((i==0 or i==len(n)) and j>=0 and j<=len(n)) or i+j==len(n)-1):
    print(n)
            