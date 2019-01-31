#CodeWars Stepan Zhuk
#Create a method is_uppercase() to see whether the string is ALL CAPS. For example:


def is_uppercase(inp):
    for i in range(len(list(inp))):
        if inp.isupper():
            return True
        else:
            return False
