
from ast import Name


def writestudent ():
    with open('student Py.txt', 'a') as file :
        c = 'y'
        while c== 'y' :
            Id = input ('Enter The student id : ')
            Name = input ('Enter The student name :')
            Age = input ('Enter The student age :')   
            Phone=input("Enter the student Phone :\n")
            Grade=input("Enter the student Grade :\n")
            file.write(Id + '\t' + Name + '\t' + Age + '\t' + Phone +'\t' + Grade +'\t' +'\n')
            c=input('Do you want to enter records again (y/n) ?')
        print('File saved successfully') 
def readstudent ():
    with open('Student Py.txt', 'r') as file :
        print ('ID\tName\tAge\tPhone\t Grade') 
        print('----------------')
        for line in file:
            print (line, end='')
def searchstudent():
    id =input('Enter the id of the student to search for: ')
    with open('Student Py.txt', 'r') as file :
        found = False
        for line in file:
            fields = line.split('\t')
            if fields [0] == id:
                found = True
                print ('ID\tName\tAge\tPhone\t Grade') 
                print('---------------')
                print(line)
        if not found:
            print ('student not found')
            print ('student list now is')
            readstudent ()
def deletestudent ():
    import os
    id = input ('Enter the id of the student to delete: ')            
    file = open('student Py.txt', 'r')
    tempFile = open('Tempstudent Py.txt', 'w')
    flag = False
    for line in file:
        fields = line.split('\t')
        if fields [0] == id:
            flag = True
        else:           
            tempFile.write(line)
    file.close()
    tempFile.close()
    os.remove('student Py.txt')
    os.rename('Tempstudent Py.txt', 'student py.txt')
    if not flag:
        print ('student not found')
    else:
         print ('Student deleted successfully')      
def updatestudent ():
    import os
    id=input("Enter the id of record you want to update: ")
    file = open ("student Py.txt", "r")
    tempFile = open("tempStudentsPy.txt", "w")
    found = False
    for line in file:
        feilds = line.split("\t")
        if feilds[0] == id:
            found = True
            Age= input('Enter the new Age : ')
            Age = input('Enter the new Name:  ')
            Phone=input("Enter the student Phone :\n")
            Grade=input("Enter the student Grade :\n")
            line = feilds[0] + Name + '\t' + Age + '\t' + Phone + '\t' +  Grade  + '\t'
        tempFile.write(line)
    file.close()
    tempFile.close()
    os.remove ("student Py.txt")
    os.rename ("tempStudentsPy.txt", "student Py.txt") 
    if found:
        print ("Record successfully updated")
    else:
         print("No students are matched!")
def all_functions():
    test = 'y'
    while test== 'y' :
       print("to record inf in the file press  (1)") 
       print("to read inf from the file press  (2)") 
       print("to search about a name press     (3)")
       print("delete a record from the file    (4)")
       print("update the file                  (5)\n\n")

       choise=input("chose what do you want to do: ")
       match choise :
           case '1':
               writestudent ()
           case '2':
               readstudent ()
           case '3':
               searchstudent()
           case '4':
               deletestudent()
           case '5':
               updatestudent()
  
       test=input('Do you want to do another somthing in the file(y/n) ?')

all_functions()       



