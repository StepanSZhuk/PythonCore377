a=int(input("Input the number a="))
b=int(input("Input the number b="))
if a <= b:
    min, max = a, b
    print("The number a={0} is minimal number,the number b={1} is maximum number".format(min, max))
else:
    min, max = b, a
    print("The number b={0} is minimal number,the number a={1} is maximum number".format(min, max))
