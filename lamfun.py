# by lamda function even odd from a list by a given list

lst=[12,23,23,34,90,100]
var=lambda n : n%2==0
var1=lambda n : n%2!=0
print(list(filter(var,lst)))  #or-
print(list(filter(lambda n : n%2==0,lst)))
print(list(filter(lambda n : not n%2==0,lst)))  # by not operator  
print(list(filter(lambda n : n%2!=0,lst))) # by this also