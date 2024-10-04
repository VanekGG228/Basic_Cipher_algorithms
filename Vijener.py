
def plus_1_letter(char:str):
    if char=='ё':
        return 'ж'
    elif char=='е':
        return 'ё'
    elif char=='я':
        return 'а'
    else:
        return chr((ord(char)+1))



def progress_key(key:str,l)->str:
    n = len(key)
    key = key.lower()
    for i in range(n , l):
        key = key + plus_1_letter(key[i-n])
    #print(key)    
    return key



def Number(char:str)->int:
    if char.lower()=='ё':
        return 6
    x = ord(char.lower()) - ord('а')
    if x>=6:
        x+=1
    return x    



def letter(num):
    if num==6:
        return 'ё'
    elif num>6:
        return chr(num + ord('а')-1)   
    else:
        return chr(num + ord('а'))  



def Vijener(s:str,key:str)->str:
    result=''
    if len(s)!=len(key):
        print('Чёёё')
    for i in range(len(s)):
        lett = letter((Number(s[i]) + Number(key[i])) % 33)
        if s[i].isupper():
           lett =lett.upper()
        result = result + lett
    return result



def decipher_Vijener(s:str,key:str)->str:
    result=''
    for i in range(len(s)):
        lett = letter((Number(s[i]) - Number(key[i])) % 33)
        if s[i].isupper():
           lett =lett.upper()
        result = result + lett
    return result

