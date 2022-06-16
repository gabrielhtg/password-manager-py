file = open("pwd.txt", 'r')
for i in file.readlines() :
    print(i, end='')
file.close