
# program for checking even odd from a given list by filter function and programmer defined function
lst=[12,23,23,34,90,100]

def even(n):

    if(n%2==0):
        # print('Even number :{}'.format(n))
        return True
    else:
        # print('Odd number:{}'.format(n))
        return False
def Odd(n):
    if(not n%2==0):
        # print('Even number :{}'.format(n))
        return True
    else:
        # print('Odd number:{}'.format(n))
        return False
# psl=filter(even,lst)
print(list(filter(even,lst)))
# print(tuple(psl))
# nsl=filter(Odd,lst)
print(list(filter(Odd,lst)))   

