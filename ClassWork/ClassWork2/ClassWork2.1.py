#Роздрукувати всі парні числа менші 100 (написати два варіанти коду: один використовуючи цикл while, а інший з використанням циклу for).

i=0
while i<100:
    i+=2
    print(i)


for i in range(2,100,2):
    print(i)
