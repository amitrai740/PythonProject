import string
import random
length=int(input("enter the length of the password you want to generate"))
lower=string.ascii_lowercase
upper=string.ascii_uppercase
digit=string.digits
symbol=string.punctuation
combine=lower+upper+digit+symbol
x=random.sample(combine,length)
password="".join(x)
print(password)
