n = int(input("enter the number : "))

s = 0
while s < n//10:
    r = n % 10
    s = s*10+r
    n = n//10

if s == n or s == n//10:
    print("Palindrome !!!")
else:
    print("Not Palindrome !!!")
