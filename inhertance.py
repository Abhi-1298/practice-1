'''You are given two classes, Person and Student, where Person is the base class and Student is the derived class. Completed code for Person and a declaration for Student are provided for you in the editor. Observe that Student inherits all the properties of Person.

Complete the Student class by writing the following:

A Student class constructor, which has 4 parameters
1)A string, firstname.
2)A string, lastname.
3)An integer, idnumber.
4)An integer array (or vector) of test scores,scores .
5)A char calculate() method that calculates a Student object's average and returns the grade character representative of their calculated average:

Grading table:-
=========================
Letter | Average(a)
--------------------
O      |    90<=a<=100
E      |    80<=a<90
A      |    70<=a<80
P      |    55<=a<=70
D      |    40<=a<=55
T      |    a<40

'''
class Person:
    def __init__(self,firstName,lastName,idNumber): # setting the value
        self.firstName=firstName
        self.lastName=lastName
        self.idNumber=idNumber

    def printPerson(self):  # getting the values
        print("Name:",self.lastName + ",",self.firstName)
        print("ID:",self.idNumber)

class Student(Person):
    def __init__(self, firstName, lastName, idNumber,scores):
        Person.__init__(firstName, lastName, idNumber)
        self.scores=scores
    
    def calculate(self):

        average=(scores+scores)/2

        if average>=90 and average<=100:
            average='O'
        elif average>=80 and average<90:
            average='E'
        elif average>=70 and average<80:
            average='A'
        elif average>=55 and average<70:
            average="P"
        elif average>=40 and average<55:
            average="D"
        else:
            average="T"
        return average
        
line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input()) # not needed for Python
scores = list( map(int, input().split()) )
s = Student()
s.printPerson()
print("Grade:", s.calculate())