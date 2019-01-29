#Codewars Stepan Zhuk
#Given a string, you have to return a string in which each character (case-sensitive) is repeated once.


#Variant 1 
def double_char(s):
    return ''.join(i*2 for i in s)
    
#Variant 1     
def double_char(s):
    out=""
    for i in s:
        out+=i*2
    return out
