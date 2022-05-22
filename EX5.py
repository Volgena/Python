#Дано натуральное четырехзначное число n. Верно ли, что все его цифры различны?
mas=[]

x = int(input("Введите четырехзначное число:\n"))
print("Вы ввели:"+str(x))
if (x % 4 == 0) and (x % 100 != 0) or (x % 400 == 0):
    print('YES')
else:
    print('NO')
myArray = []

for x in range(100000,999999):
    myStr = str(x)
    temp = 0
    for i in range(len(myStr)):
        temp+=int(myStr[i])
    if(temp % 7 == 0):
        myArray.append(x)

for x in range(1,len(myArray)):
    if(myArray[x]-myArray[x-1]==1):
        resualt = True
        print("Результат задания: " + str(resualt))
        print("\n" + str(myArray[x-1]) +" "+ str(myArray[x]))
