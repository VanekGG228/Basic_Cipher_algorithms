def is_russian_letter(char)->bool:
    return ('а' <= char <= 'я') or ('А' <= char <= 'Я') or (char=='ё') or (char=='Ё')


def word_processing(s:str)->str:
    result=''
    for i in s:
        if is_russian_letter(i):
           result = result + i 
    return result 