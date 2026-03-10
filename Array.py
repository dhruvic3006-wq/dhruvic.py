#Integer Array
from array import array
arr=array('i',[10,20,30,40])
print(arr)
print(type(arr))
#basic array operation
#1 len()
from array import array
arr=array('i',[10,20,30,40,50])
print(len(arr))
#append
from array import array
arr=array('i',[10,20,30])
arr.append(40)
print(arr)
#insert 
from array import array
arr=array('i',[10,20,30,40])
arr.insert(2,30)
print(arr)
#remove
from array import array
arr=array ('i',[10,20,30,20,40])
arr.remove(20)
print(arr)
#pop
from array import array
arr=array('i',[10,20,30,40])
x=arr.pop()
print("Removed:",x)
print(arr)
