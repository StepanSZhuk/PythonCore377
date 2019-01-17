number = str(input("Enter the number:")) 
prod=1
for i in number:
    prod*=int(i) 
print("The product of the entered number:",prod)

rev=number[::-1]
print("Number in reverse order:",rev)
print("Sorted in ascending order:",sorted(number))
