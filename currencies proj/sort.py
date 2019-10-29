import numpy as nump

'''

arr = []
l = int(input('Enter length of the array:'))

for i in range(0,l):
    p = int(input('Enter the number:',))
    arr.append(p)
print('Your array:',arr)

for i in range(0,l-1):
    for j in range(0,l-i-1):
        if arr[j] > arr[j+1]:
            arr[j],arr[j+1] = arr[j+1],arr[j]
    print("Array on iterations:",arr)
print('Sorted array:',arr)

'''

'''
arr = []
index = 0
try:
    l = int(input('Enter length of the array:'))

    for i in range(0,l):
        p = int(input('Enter the number:',))
        arr.append(p)
    print('Your array:',arr)
    for i in range(0, l):
        if arr[i] > arr[index]:
            index = i
    print(arr[index])
except Exception:
    print('Invalid value')


'''

'''
a = []
l = int(input('Enter length of the array:'))
for i in range(0,l):
    p = int(input('Enter the number:',))
    a.append(p)
print('Your array:',a)
print(l)
a.sort()
print('sorted array:',a)
value = int(input('Value u are looking for:'))
mid = l // 2
low = 0
high = l - 1

while a[mid] != value and low <= high:
    if value > a[mid]:
        low = mid + 1
    else:
        high = mid - 1
    mid = (low + high) // 2

if low > high:
    print("No element")
else:
    print("Element's id = ", mid)
    b = str(a[mid])
    c = str(a)
    с = c.count(b)
    print('Num of enters:', с)


'''

'''
a = str(input('Input str:'))
l = len(a)
print('U have inputed:',a)
print('Length of str: ',l,'chars')
n = l // 2
print('Half of length:',n)
for i in range(0,n):
    if a[i] == a[-1-i]:
        print("It's palindrome!")
    else:
        print("Your str isn't palindrome")

'''

'''
class vector(object):
    def __init__(self, r, c): # при создании указываем номер строки и столбца, в который помещаем
        self.r = r # Номер сторки в двумерном списке.
        self.c = c # Номер столбца ...

    def matrixmult(self):
'''

