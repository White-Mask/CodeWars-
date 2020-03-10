from solution import *

def create_phone_number(n):
    number = '('
    for i,num in enumerate(n):
        if i < 3:
            number += str(num)
            if i == 2:
                number += ') '
        else:
            number += str(num)
            if i == 5:
                number += '-'
    return number