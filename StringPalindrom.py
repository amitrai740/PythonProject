str = input('Enter string : ')

l = len(str)
for i in range(l//2):
    if str[i].lower() != str[l - 1 - i].lower():
        print("Not Palindrome")
        exit(0)

print('Palindrome')
