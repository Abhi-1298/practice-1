# 3) python program which will accept list of numbers and sort them in both asc and desc order.
def fun():
    n = int(input("Enter number of elements : "))  # n=5
    if(n<=0):
        print("{} is invalid input:".format(n))
    else:
        list=[]
        for i in range(0,n):  
            new_list=int(input())
            list.append(new_list)
        print('After appending the list in new : {}'.format(list))
        list.sort()     
        print('the list in asc order : {}'.format(list)) 
        list.sort(reverse=True)   
        print('The list in desc order:{}'.format(list))
fun()