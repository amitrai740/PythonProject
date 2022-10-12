n = int(input())

lst = list()
for i in range(n):
    query = input()
    items = query.split()

    cmd = items[0]
    arg = items[1:]

    if cmd != 'print':
        cmd = cmd + '(' + ','.join(arg) + ')'
        eval('lst.' + cmd)
    else:
        print(lst)


"""
List operation using if else

    if items[0] == 'insert':
        lst.insert(int(items[1]), int(items[2]))
    elif items[0] == 'print':
        print(lst)
     elif items[0] == 'remove':
        lst.remove(int(items[1]))
    elif items[0] == 'sort':
        lst.sort()
    elif items[0] == 'pop':
        lst.pop()
    elif items[0] == 'reverse':
        lst.reverse()
    elif items[0] == 'append':
        lst.append(int(items[1]))
"""


