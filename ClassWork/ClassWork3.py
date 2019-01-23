#1. Створити список цілих чисел, які вводяться з терміналу та визначити серед них максимальне та мінімальне число.
nums = []
k=int(input("Please enter the count of the elements of sequence: "))
for i in range(k):
     n = int(input("Please enter the element: "))
     nums.append(n)
print(nums)
print("Max number is:", max(nums))
print("Min number is:", min(nums))


#2. В інтервалі від 1 до 10 визначити числа 
#•  парні, які діляться на 2,
#•  непарні, які діляться на 3, 
#•  числа, які не діляться на 2 та 3.

a=[x for x in range(1,11,1) if x%2==0]
print("Even numbers divisible by 2",a)
a1=[x for x in range(1,11,1) if x%3==0 and x%2!=0]
print("Odd numbers that are divided by 3",a1)
a2=[x for x in range(1,11,1) if x%3!=0 and x%2!=0]
print("Odd numbers that are divided by 3 and 2",a2)



#3. Написати програму, яка обчислює факторіал числа, яке користувач вводить.(не використовувати рекурсивного виклику функції)
number=int(input("Enter a whole positive number:   "))
factorial=1
for i in range(1,number+1):
    factorial*=i  
print("Factorial number {} equals {}".format(number,factorial))


#4.Напишіть скрипт, який перевіряє логін, який вводить користувач. 
# Якщо логін вірний (First), то привітайте користувача. 
# Якщо ні, то виведіть повідомлення про помилку. 
# (використайте цикл while)

login=(input("Enter your login:"))
while login=="First":
    print("Welcome you!")
    break
else:
    print("You are not registered user")
