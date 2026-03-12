#basic slices
from array import array
arr=array('i',[10,20,30,40,50])
print(arr[1:4])#index 1 to 3
print(arr[:3])#start to index 2
print(arr[2:])#index 2 to end
print(arr[:])#entire array
#2
from array import array
arr=array('i',[10,20,30,40,50,60,70,80])
print(arr[::2])
print(arr[1::2])
print(arr[::3])
#3
from array import array
arr=array('i',[10,20,30,40,50,])
print(arr[-4:-1])
print(arr[-3::3])
print(arr[:2])
#4
from array import array
arr=array('i',[10,20,30,40,50,])
print(arr[::-1])
#5
from array import array
arr=array('i',[10,20,30,40,50,])
arr[1:4]=array('i',[25,35,45])
print(arr)