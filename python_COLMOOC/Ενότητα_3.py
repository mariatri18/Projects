def reverse(s):
    return s[::-1]

def isPalindrome(s):
    rev= reverse(s)
    if (s == rev):
        return True
    return False



s = str (input ('Δώστε ένα αλφαριθμητικό: '))

alist = list(s)
adict = {s ,len(alist)}



if len(alist) == 1:
    print('Mήκος 1')
   


ans = isPalindrome(s)

if ans == 1:
    print(alist)
    print(adict)
    
else:
    print('Δεν ειναι παλίνδρομο')
