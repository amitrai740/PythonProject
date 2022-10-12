n=int(input("enter the number"))
temp=n
s=0
while(temp!=0):
    r=temp%10
    s=s*10+r
    temp=temp//10

if(s==n):
    print("pallindrome")
else:
    print("not pallindrome")


