#3.program to check validity of passwords
#atleast 1 letter between[a-z] & 1 letter b/w [A-Z].
#atleast 1 num b/w[0-9]
#atleast 1 character from[#$@]
#mim 6 char
#max 16 char
import re
p = input("Input your password")
x=True
if (len(p) < 6 or len(p) > 12):
    pass
elif not re.search("[a-z]", p):
    pass
elif not re.search("[0-9]", p):
    pass
elif not re.search("[A-Z]", p):
    pass
elif not re.search("[$#@]", p):
    pass
elif re.search("\s", p):
    pass
else:
    print("Valid Password")
    x = False
    pass
if x:
    print("Not a Valid Password")'''
