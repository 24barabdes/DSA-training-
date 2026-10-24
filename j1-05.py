#Ques-1
'''Name="Prashant"
#     01234567
newname =""
#WAP to remove duplicates
for i in Name:
    if i not in newname:
        newname += i
print(newname)   '''     


#Ques-2
#WAP to accept three paper marks like M1, M2, M3 and calculate total, percentage and check if user is passed in all subjects so print pass else print fail and check if percentage is greater than 65 and user is having one projet so print he/she eligible for placement drive else print not eligible.
'''m1 = int(input("enter the marks of m1:"))
m2 = int(input("enter the marks of m2:"))
m3 = int(input("enter the marks of m3:"))
total =m1+m2+m3
percentage = total/3.0
print("Total=",total)
print("Percentage=",percentage)
if m1>=40 and m2>=40 and m3>=40:
    print("Pass")
else:
    print("Fail") 
Projects = input("he/she having atleast one project?",)    
if percentage>65 and Projects:
    print("Eligible for placement.")
else:
    print("Not Eligible.")    '''
    
    
    

#Ques-3
'''a=[1,2,3,4,5,6,7,8,9,10]
a[::2]=10,20,30,40,50,60
print(a)        
     '''  
 
     
#Ques-4
'''a=[1,2,3,4,5]
#  0 1 2 3 4 (agr 0 diya ho toh ek digit peeche ho jata hai)
print(a[3:0:-1])'''     



#Ques-5
'''def func(value, values): # (3,[1,2,3])
    var = 1              # (3,[44,2,3])
    values[0] = 44       # (3,(v[0],v[1],v[2]))
t=3
v=[1,2,3]
func(t,v)
print(t,v[0])'''    


#Ques-6
'''arr=[[1,2,3,4],    #single loop = outer loop(row)  , nested loop outer loop= row, inner loop= column
     [4,5,6,7],       #pop=LIFO
     [8,9,10,11],
     [12,13,14,15]]
for i in range(0,4):     
    print(arr[i].pop())'''
    
    
#Ques-7
'''def f(i, values= []):
    values.append(i)
    print (values)  #[1],[1,2],[1,2,3]
f(1)
f(2)
f(3)'''


#Ques-8
'''arr = [1,2,3,4,5,6]
for i in range(1,6):
    arr[i-1] = arr[i]
for i in range(0,6):
    print(arr[i],end = "")'''


        
    
#Ques-9
'''a={(1,2):1,(2,3):2,(4,5):3}
print(a[4,5]) '''


#Ques-10
'''a={'a':1,'b':2,'c':3}
print(a['a','b'])'''


#Ques-11
'''fruit ={}
def addone(index):
    if index in fruit:
        fruit[index] += 1 
    else:
        fruit[index] = 1           #{'Apple':1,'banana':1,'apple':1}
addone("Apple")
addone("Banana")              
addone("apple")
print(len(fruit))'''


#Ques-12
'''arr = {}   #{1:2,'1':2}
arr[1] =1
arr['1'] =2
arr[1] += 1
print(arr)
sum = 0
for k in arr:   #'1'
    sum += arr[k]
print(sum) '''


#Ques-13
'''my_dict = {}   #{1:4,'1':2}
my_dict[1] = 1
my_dict['1'] = 2
my_dict[1.0] = 4 
print(my_dict)
sum = 0
for k in my_dict:    #k='1'
    sum += my_dict[k]
print(sum) '''   


#Ques-14  
'''my_dict = {}
my_dict[(1,2,4)] = 8
my_dict[(4,2,1)] = 10
my_dict[(1,2)] = 12
sum = 0
for k in my_dict:
    sum += my_dict[k]
print(sum)
print(my_dict)'''


#Ques-15
'''box = {}
jars = {}
crates = {}
box['cakes'] = 3
box['biscuit'] = 1
jars['jam'] = 4
crates['box'] = box
crates['jars'] = jars
print(len(crates[box])) '''

#Ques-16
'''dict = {'c':97,'a':96,'b':98}
for _ in sorted(dict):
    print(dict[_])'''
    
#Ques-17
#id function - to compare address
'''rec = {"Name": "Python", "Age":"20"}
r = rec.copy()
print(id(r) == id(rec))
print(id(rec))
print(id(r))'''

#Ques-18
'''arr = [0,1,0,3,12]     #[1,3,12,0,0]   
for i in arr: #i=2
    if i==0:
        arr.remove(i)
        arr.append(i)
print(arr)'''


#Ques-19
#find second largest element
'''arr = [7,3,9,2,8]
arr.sort()
print(arr)    
print(arr[-2])'''


#Ques-20
#Product of array except self
'''arr = [1,2,3,4]
print(len(arr))
for i in arr:'''

#Ques-21
#find intersection of three elements
'''A=[1,2,3]
B=[2,3,5]
C=[3,4,5]
for i in A:
    if i in B and i in C:
        print(i)'''
        
        
#Ques-22
#Maximum Consecutive Ones
'''arr = [1,1,0,1,1,1,0,1,1,1,1]
for i in arr:
    if i == 1:
        '''
        
    
#Ques-23
# WAP to accept any single chr and check the entered chr is in upper case, lower case, digit or special symbol and according to that print message.
'''ch = ord(input("Enter any single chr:"))
if ch>= 65 and ch<=90:
    print("upper case")
elif ch>=97 and ch<=122:
    print("Lower case")
elif ch>=48 and ch<=57:
    print("Digit")
else:
    print("Special chr")   '''                     
    
    
    
#Ques-24
'''arr = ["helpforaarshabh"]
for i in arr:'''


#Ques-25
'''class Stack:
    def __init__(self, value):
        self.data = value
        self.myStack = []'''
         #Constructor is never called it automaticalley gets called when we create an object, it creates memory and assigns the address to the object, it is a special function.
         # for one object only one constructor can be called.
         
          
'''class Student:     #Class Name First letter should always be in Capital
    rollno = 101 #data member
    def __init__(self):             #Construtor
        print("I'm a constructor")
        
    def msg(self):
        print("Hello World")             
obj = Student()
print(obj)
obj.msg()
obj2 = Student()    
print(obj.rollno)'''

 #Ques-26
'''class Hod:
     def __init__(self): #Constructor
         self.name='XYZ' #2 byte
         self.age=32     #3 byte
         self.empid=1001 #1 byte
     def info(self):                  
         print("My name is:",self.name)
         print("My age is:",self.age)
         print("My emp id:",self.empid)
obj=Hod()  #object create
obj.info()              
     '''

#Ques-27
# paranthesis ke andar jo bhi declare krte hai usse parameter kehte hai.
'''class Hod:
     def __init__(self,name,age,rollno): # Parametrize Constructor
         self.name=name #2 byte
         self.age=age    #3 byte
         self.rollno=rollno #1 byte
     def show(self):                  
         print("name :",self.name)
         print("age :",self.age)
         print("rollno:",self.rollno)
obj=Hod('Arjun',20,25)  #object create
obj.show() '''  
     
#Ques-28
#Create class name of students and accept personal info like name, mobileno and emailid and create method display the personal info
'''class Student:
    def __init__(self,name,mobileno,emailid):
        self.name = name
        self.mobileno = mobileno
        self.emailid = emailid
    def display(self):
        print("name:",self.name)
        print("Mobile No:",self.mobileno)
        print("Email Id:",self.emailid)
obj = Student('Raj',9556734098,'master@gmail.com')
obj.display() '''

#Ques-29
'''class Student:
    def __init__(self):
        self.s_name = "prashant"
        self.l_name = 'jha'
        self.rollno = 101
        self.branch ="CS"
        self.mb = 00000000000
obj = Student()
print(obj.__dict__)  '''      #presents all values in dictionary way
        
        
#Ques-30
'''class Stack:
    def __init__(self, size):
        self.stackSize = size
        self.myStack = [] #empty list
    
    def isFull(self):
        if len(self.myStack) == self.stackSize:
            return True
        else:
            return False
             
    def isEmpty(self):
        if self.myStack == []:
            return True
        else:
            return False  
        
    def push(self, data):
        if self.isFull():
            print("Stack is Full")   
        else:
            self.myStack.append(data)
            print("Element pushed")    
            
    def pop(self):
        if self.isEmpty():
            print("Stack is empty")
        else:
            print(self.myStack.pop())    
            
    def peek(self):
        if self.isEmpty():
            print("Stack is empty")
        else:
            print("Top Element =  ",self.myStack[-1])                                                          
                        
                  
size = int(input("Enter the size of Stack:")) #execution starts from here(outside the class)

while True: #While loop is used when no. of iterations are not known
    obj = Stack(size)
    print("1. Push Operation:")
    print("2. Pop Operation:")
    print("3. Peek Operation:")
    print("4. isEmpty Operation:")
    print("5. isFull Operation:")
    print("6. Delete Complete Stack:")
    print("7. Display Stack:")
    print("8. Exit:")
    
    choice = int(input("Enter your choice:"))
    if choice == 1:
        value = int(input("Enter the value to push in Stack:"))
        obj.push(value)
                '''
                
'''def __init__(self, value, localMax):
        self.value = value
        self.localMax = localMax


class Stack:
    def __init__(self, size):

        # Setting size of stack and
        # initial value of top
        self.stack = [None] * size
        self.size = size
        self.top = -1

    # Function to push an element
    # to the stack
    def push(self, value):

        # Don't allow pushing elements
        # if stack is full
        if self.top == self.size - 1:
            print("Stack is full")
        else:
            self.top += 1

            # If the inserted element is the first element
            # then it is the maximum element, since no other
            # elements is in the stack, so the localMax
            # of the first element is the element itself
            if self.top == 0:
                self.stack[self.top] = Block(value, value)

            else:

                # If the newly pushed element is less
                # than the localMax of element below it,
                # Then the over all maximum doesn't change
                # and hence, the localMax of the newly inserted
                # element is same as element below it
                if self.stack[self.top - 1].localMax > value:
                    self.stack[self.top] = Block(
                        value, self.stack[self.top - 1].localMax)

                # Newly inserted element is greater than
                # the localMax below it, hence the localMax
                # of new element is the element itself
                else:
                    self.stack
                    self.stack[self.top] = Block(value, value)

            print(value, "inserted in the stack")

    # Function to remove an element
    # from the top of the stack
    def pop(self):

        # If stack is empty
        if self.top == -1:
            print("Stack is empty")

        # Remove the element if the stack
        # is not empty
        else:
            self.top -= 1
            print("Element popped")

    # Function to find the maximum
    # element from the stack
    def getMax(self):

        # If stack is empty
        if self.top == -1:
            print("Stack is empty")
        else:

            # The overall maximum is the local maximum
            # of the top element
            print("Maximum value in the stack:",
                  self.stack[self.top].localMax)'''
         
         
         
         
         
#Ques-31         
'''Perormiong the same operstions multipletimes with diff inputs
             
             in every step we try smaller inputs to make  the problem smaller
             
             base condition is needed to stop the recursion
             
             if you can dividethe problem into simillar sub problems
             
             Design an algorithm to compute nth 
             
             write a code to list the n
             
             implement a method to compute all
             
             Recursion uses stack memory'''
             
'''def factorial(num):
    if num <=1:
        return 1
    return num*factorial(num-1)
print(factorial(4))
def power(bsae, exponent):
    if exponent == 0:
        return 1
 return base * power(base,exponent-1)
print(power(2,0))
print(power(2,2))
print(power(2,4))

def reverse(strng):
    if len(strng)<=1:
        return strng
    return strng[len(strng)-1] + reverse(strng[0:len(strng)-1])
print(reverse('python'))
'''



#Ques-32
'''n = int(input("Enter number of values:"))
mylist = list(map(int, input().split()))   #[10,11,7,12,14]   space separted value using split
sum=0
for i in range(n-1):#i=0
    sum += abs(mylist[i]-mylist[i+1])  #10  - 11 = -1  =1(position)   abs- absolute function is used to convert negative values into positive values
                                    #11 - 7 = 4
print('Sum=', sum)'''


#Ques-33
# rollno = [3,5,7,1,11,4,5,2]
# for x in rollno:   #x=1:3
#     if x==2 or x==4 or x==6 or x==8 or x==10:
#         print("even no is found", x)
#         break


#Ques-34
'''for i in range(1,4): #outer loop (row)
    for j in range(1,4): #inner loop (column)
        print(i, end=" ")  #end=" " gives as much space you want
        
    print()    
        '''
        
#Ques-35
# n= int(input("Enter the number of rows:"))
# for i in range(1, n+1):  
#     for j in range(1, n+1):
#         print(chr(64+i),end=" ") #ASCII code of 64+i=65 is A(i)
#     print()            


#Ques-36
# n= int(input("Enter the number of rows"))
# for i in range(1, n+1): 
#     for j in range(1, n+1):
#         print(n+1-i, end=" ")
#     print()    

#Ques-37
# n = int(input("enter no of rows"))
# for i in range(1,n+1):
#     for j in range(1,1+i):
#         print(i,end=" ")
#     print()    


#Ques-38
# name = "Prashant*is*a*good*programmer"
# newname = ""
# val = ""
# for i in name:
#     if i !="*":
#         newname += i
#     else:
#         val+=i
       
# print(newname)
# print(str(val+newname))            


#Ques-39
# mylist = [[100,198,333,323],[122,232,221,111],[223, 565,245,764]]
# newlist = []
# for i in range(3):
#     j=0
#     max = mylist[i][j]
#     for j in range(4):
#         c_max = mylist[i][j]
#         if max < c_max:
#             max = c_max
#     newlist.append(max)
# print(newlist)            


#Ques-40
# pizza = 100
# burger = 50
# colddrink = 20
# val1 = int(input("Enter te number of pizza bought:"))
# val2 = int(input("Enter te number of burger bought:"))
# val3 = int(input("Enter te number of colddrink bought:"))
# pizza_total = pizza*val1 
# burger_total = burger*val2
# colddrink_total = colddrink*val3 
# print("---------------------------------------------")
# print("Bill Details:")
# print("Total Price of PIzza:",pizza_total)
# print("Total Price of burger:",burger_total)
# print("Total Price of colddrink:",colddrink_total)
# print("Total Bill:",pizza_total+burger_total+colddrink_total)


#Ques-41
# a=[]
# b=[]
# n1= int(input("Enter the size of array"))
# for i in range(n1):
#     a.append(input())
# n2 = int(input("Enter the size of array:"))
# for i in range(n2):
#     b.append(input())
# if len(a) == len(b):
#     print("Compatible")
# else:
#     print("Not Compatible")            


#Ques-42
# n = int(input("Enter number of values:"))
# mylist = list(map(int, input().split())) 
# sum = 0
# for i in range(n):
#     val = int(input("Enter the value"))
#     mylist.append(val)
# print(mylist)
# a=[]
# b=[]
# for i in range(len(mylist)):
#     if mylist[i]%2==0:
#         a.append(mylist[i])
#     else:
#         b.append(mylist[i]) 
# print()               
    
    

#Ques-43
# import sys
# class CRUD:
#     def __init__(self):
#         print("Student management System")
#         self.studentID=[]
#         self.studentName=[]
#         self.studentRollno=[]
#         self.studentCity=[]
        
#     def addStudent(self):
#         self.studentID.append(input("Enter Student ID:")) 
#         self.studentName.append(input("Enter Student Name:"))
#         self.studentRollno.append(input("Enter Student Rollno:"))
#         self.studentCity.append(input("Enter Student City:"))  
        
#     def showStudent(self):
#         print("stuent details are:\n")
#         print("StudentID\tStudentRollNo\tStudentname\tStuentCity")
#         for x in range(60):
#             print("-",end=" ")
#         print()
#         for i in range(len(self.studentID)):
#             print(self,studentID[i],"\t\t", self.StudentRollNo[i],"\t\t", self.StudentName[i],"\t\t", self.StudentCity[i])      
#             for x in range(60):print("-",end="")
#             print()
                       
#     def start(self):
#         while True:
#             print("\n1. Add Student")
#             print("\n2. Show Student")
#             print("\n3. Update Student")
#             ch=int(input("Select any choice"))
#             if ch==1:
#                 self.addStudent()
#             elif ch==2:
#                 self.showStudent()
#             elif ch==5:
#                 sys.exit()
#             else:
#                 print("Please select correct option..")            
            
# if __name__ == "__main__":
#     obj=CRUD()
#     obj.start()            
                          
                          

#FIFO example- point sale system of restaurant, printer queue system, call centre phone system, 
# whenever we have a huge amt of data we use linkedlist 
 # timecomplexity     space 
#   O(1)                O(1)    Push
#   SAME                same       Pop , peek, isempty, delete.



# class Queue:
#     def __init__(self,size):
#         self.queueSize = size
#         self.myQueue = []
#     def isFull(self):
#         if len(self.myQueue) == self.queueSize:
#             return True
#         else:
#             return False
#     def isEmpty(self):
#         if self.myQueue == []:
#             return True
#         else:
#             return False        
#     def enQueue(self,value):
#         if self.isFull():
#             print("queue is full")
#         else:
#             self.myQueue.append(value)
#     def deQueue(self,value):
#         if self.isEmpty():
#             print("queue is empty")
#         else:
#             print(self.myQueue.pop(0))      
#     def peekFrontElement(self):
#         if self.isEmpty():
#             print("Queue is empty")
#         else:
#             print(self.myQueue[0])            
#     def deleteQueue(self):
#         self.myQueue = None 
#         print("Entire Queue has deleted")
#     def displayQueue(self):
#         if self.isEmpty():
#             print("Queue is empty")
#         else:
#             print(self.myQueue)     
            
# size = int(input("Enter the size of Queue:"))
# obj = Queue(size)#constructor will be called and size also passed
# while True:
#     print("1. Enqueue Operation:")
#     print("2. dequeue Operation:")  
#     print("3. Peek Front Operation:")  
#     print("4. isEmpty Operation:")  
#     print("5. isFull Operation:")  
#     print("6. Delete entire queue Operation:")  
#     print("7. display Operation:")  
#     print("8. Exit Operation:")  
    
#     ch = int(input("enter your choice"))
#     if ch == 1:
#         value = int(input("Enter the value to add in Queue:"))
#         obj.enQueue(value)
#     elif ch == 2:
#         obj.deQueue(value)
#     elif ch == 3:
#         obj.peekFrontElement()
#     elif ch == 4:
#         print(obj.isEmpty())
#     elif ch == 5:
#         print(obj.isFull())
#     elif ch == 6:
#         obj.deleteQueue()
#     elif ch == 7:
#         obj.displayQueue()
#     else:
#         sys.exit()                          
                                   
                
        
            
# #FILE HANDLING
# #file handling used to store the data permanently for future purpose
# import csv
# f = open("student.csv", "a",newline="")
# a = csv.writer(f)
# a.writerow(["studentID","rollno","name","mobileno"])
# studentid = int(input("Enter student id:"))
# rollno = int(input("Enter student rollno:"))
# name = input("Enter your name:")
# mobileno = int(input("Enter mobile no."))
# a.writerow([studentid,rollno,name,mobileno])
# print("student record has saveed successfully")      


#Ques-45
#Write a program to accept = "rollno","name","mobileno","p1","p2","p3","email"
#calculate = "total_percentage"
#condition: check if user is passed in all the subjects so store"pass in result column else store fail and passing marks are 40.

# import csv
# f = open("info.csv","a", newline="")
# a = csv.writer(f)
# a.writerow(["Name","rollno","mobileno","p1","p2","p3","email","result"])
# studentname = int(input("Enter name:"))
# Rollno = int(input("Enter rollno:"))
# mobileno = int(input("Enter mobileno:"))
# p1 = int(input("Enter paper 1 marks"))
# p2 = int(input("Enter paper 2 marks"))
# p3 = int(input("Enter paper 3 marks"))
# email = input("Enter email")
# if p1>=40 and p2>=40 and p3>=40:
#     result ="pass"
#     print("passed")
# else:
#     result ="fail"
# total = p1+p2+p3
# per= total/3.0        
            
            
            
# #Ques-46
# product = int(input("enter the product type:"))
# numK = int(input("Enter the number:"))

#QUes-47
# class Node:
#     def __init__(self,value):
#         self.data = value
#         self.next = None
                
# class LinkedList:
#       def __init__(self):
#           self.head = None
          
# linkedListObj = LinkedList()    

# linkedListObj.head = Node(10)
# second = Node(20)
# third = Node(30)
# fourth = Node(40)
# fifth = Node(50)
# linkedListObj.head.next=second
# second.next=third                

# while linkedListObj.head != None:
#     print("|",linkedListObj.head.data,"|","->",end=" ")
#     linkedListObj.head = linkedListObj.head.next
    
    
    
# #Ques-48
# class Node:
#     def __init__(self,value):
#         self.data = value
#         self.next = None
        
# class Linkedlist:
#     def __init__(self):
#         self.head = None
#         self.tail = None   
        
#     def addNodeEnd(self,value):
#         newNode = Node(value)
#         if self.head is None:
#             self.head = newNode
#             self.tail = newNode
#         else:
#             self.head.next = newNode
#             self.tail = newNode    
    
#     def displayLinkedlist(self):
#         current = self.head
#         while current != None:
#             print("|", current.data,"|",end=" ")
#             current = current.next
    
# linkedObj = Linkedlist()
# linkedObj.addNodeEnd(10)
# linkedObj.addNodeEnd(20)
# linkedObj.addNodeEnd(30)
        
        
#A tree is a nonlinear data structure with hierarchical relationship between its elements without having any cycle, it is basically reversed from a real life tree.
# Example- quicker and easier access to the data , store hierarchical data, like folder structure, organization structure, XML/HTML data.
# file system, folder system is a real life example to tree data structure.
# Binary search tree, AVL, Red Black Tree, Trie
# Root = top node without parent
#edge = a link between parent and child
# leaf = a node which does not have children
#sibling = childen of same parent
#ancestor = parent, grandparent and great grand parent of node
# depth of node = a length of the path from root to node
#height of node = a length of path from the node to the deepest node
#Tree- liked list , Python list(how many ways to implement tree?)


class Tree:
    def __init__(self, data):
        self.data = data
        self.child = []
    
    def __str__(self, level=0):
        ret =" "* level+str(self.data)+"\n"
        for child in self.child:
            ret+=child.__str__(level+1)
        return ret    
        
    def addChild(self, value):
        self.child.append(value)
           
rootNode = Tree('Drinks')
hot = Tree('hot')
cold = Tree('cold')
tea = Tree('tea')
coffee = Tree('coffee')
nonAlcoholic=Tree('nonAlcoholic')
Alcoholic=Tree('Alcoholic')


rootNode.addChild(hot)
rootNode.addChild(cold)

hot.addChild(tea)
hot.addChild(coffee)
        
cold.addChild(nonAlcoholic)
cold.addChild(Alcoholic)

print(rootNode)                                                      