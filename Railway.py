from proc import *

def Railway( s: str, key) -> str:
    if(key  < 2):
        return s
    if key>=len(s):
        return s
    arr = ['' for i in range(key)]
    direction = 'down'
    row = 0
    for i in s:
        arr[row] += i
        if row == key-1:
            direction = 'up'
        elif row == 0:
            direction = 'down'
        if(direction == 'down'):
            row += 1
        else:
            row -= 1
    return(''.join(arr))




def decipher(cipher:str,key)->str:
    if key < 2:
        return cipher
    if key>=len(cipher):
        return cipher
    result = cipher
    length = len(cipher)
    row = 0
    kol = 1
    number =0
    for i in range(1,length):
        if kol % 2 == 1:
            number = number + key*2 - 2 * (row + 1)
        else:
            if (row!=0):
                number = number + 2*row
            else:
                number = number + key*2-2  
        kol += 1    
        if number >= length:
            row += 1 
            kol = 1
            number = row 
            if (row + 1) % key == 0:
                row=0
        result = result[:number] + cipher[i] + result[(number+1):]         
    return result



def tests(s:str,key:int)->bool:
    return s==decipher(Railway(s,key),key)
