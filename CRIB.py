from collections import deque

graph = {
    "you":
        ["alice", "bob", "claire"],
    "bob":
        ["anuj", "peggy", 'dima'],
    "alice":
        ["peggy"],
    "peggy":
        [],
    "claire":
        [],
    "anuj":
        [],
    "dima":
        []
}


def person_is_seller(name):
    return name[-1] == 'r' #func for searching for elem


def search(name):
    search_queue = deque()  # creating doubleside queue (двухсторонняя очередь)
    search_queue += graph[name]  # all childes of 'you' adding to que (serch queue)
    searched = []
    while search_queue:  # Пока очередь не пуста
        person = search_queue.popleft()  # из очереди извлекается первый человек
        if not person in searched:
            if person_is_seller(person):  # Проверяем, является ли этот человек
                print(person + " is а mango seller ! ")  # Да, это продавец манго
                return True
            else:
                search_queue += graph[person] #adding childes of "person" to queue
                searched.append(person) # adding person to searched arr
    return False


print(search("you"))



#######################################ПУЗЫРЬКОМ########################################################################


arr = []
n = int(input())

for i in range(0,n):
    q = int(input())
    arr.append(q)
for i in range(0,n-1):
    for j in range(0,n-i-1):
        if arr[j] > arr[j+1]:
            arr[j],arr[j+1] = arr[j+1],arr[j]
    print(arr)



##########################################FAST#SORT#####################################################################


def sort(arr):
    n = len(arr)
    if n < 2:
        return arr
    else:
        mid = arr[0]
        less = [i for i in arr[1:] if i < mid]   # List generator
        higher = [i for i in arr[1:] if i > mid]
        return sort(less) + [mid] + sort(higher)


# (values) = [ (expression) for (value) in (collection) ]
#  cars    = [ person.get('car','') for person in users ] Создание списка, который заполняется значениями ключей car из списка users


###############################################FIBO#####################################################################

fib1 = fib2 = 1

n = int(input())

if n < 2:
    quit()

print(fib1, end=' ')
print(fib2, end=' ')
for i in range(1, n-1):
    fib1, fib2 = fib2, fib1 + fib2
    print(fib2, end=' ')

print()

############################################OUTPUT&CONNECTION###########################################################

import pymysql
from contextlib import closing
from pymysql.cursors import DictCursor

connection = pymysql.connect(
    host='localhost',
    user='root',
    password='25Mm14dd09nn',
    db='carsshop',
    charset='utf8mb4',
    cursorclass=DictCursor
)
with closing(pymysql.connect(host='localhost',
                             user='root',
                             password='25Mm14dd09nn',
                             db='carsshop',
                             charset='utf8mb4',
                             cursorclass=DictCursor)) as connection:
    with connection.cursor() as cursor:
        query = """


        """
        cursor.execute(query)
        for row in cursor:
            print(row)


############################################OOP#########################################################################

class Person:  # Main Class

    def __init__(self, name, age):  # Construct of the class which is called when creating an object
        self.name = name
        self.age = age
        print(name, age)

    def set(self, name, age):
        self.name = name
        self.age = age
        print(name, age)

    def _incapsul(self, arg):  # _ Says that this method shouldnt be used in another classes(childes)
        self.arg = arg


John = Person('Jonh', 32)  # Child Class


class Student(Person):  # Inheritance(nasledovanie) from Class Person
    course = 1


Igor = Student('Igor', 18)  # Child Class that has Person and Student methods
print(Igor.course)



#########################################DECORATOR######################################################################


def decorator(func): # Decorator
    def wrapper ():
        print('Code before func')
        func()
        print('Code after func')
    return wrapper

@decorator    #Saying that this func decorated by func "decorator"
def show():
    print('I am default func')

show()

########################################FACTORIAL#######################################################################

n = int(input())
b=1
for i in range(1,n+1):
    b*=i

print(b)


####################################SIMPLE####PARSE#####################################################################
from urllib import request,parse
import sys

google =  "https://www.google.com/search?"
value = {'q':'python'}


try:
    mydata = parse.urlencode(value)
    print(mydata)
    google = google + mydata
    req = request.Request(google)
    otvet = request.urlopen(req)
    otvet = otvet.readlines()
    for line in otvet:
        print(line)
except Exception:
    print('Error occured')
    print(sys.exc_info()[1])



###################SOCKETS############################################################SERVER############################
import socket

sock = socket.socket()  #new socket
sock.bind(('', 9090))   #host and port for server
sock.listen(1)          #how many users can be connected
conn, addr = sock.accept()   #getting connection with user and saving to tuple his adress and new socket

print('connected:', addr)

while True:
    data = conn.recv(1024)      #setting how mush data usser can send
    if not data:
        break
    conn.send(data.upper())     # making client's data uppercase

conn.close()                    # closing conn



###################SOCKETS############################################################CLIENT############################

sock = socket.socket()  #new socket
sock.connect(('localhost', 9090)) #connecting to server
sock.send('hello, world!') # sending data to server

data = sock.recv(1024)  # receiving data from server
sock.close()              # closing conn

print(data)



######################################FIRST###DUBLICATE#################################################################

def find_first_duplicate(something:list):
    for s in set(something):
        something.remove(s)
    return something[0]

print(find_first_duplicate([1,2,7,5,7,8]))
