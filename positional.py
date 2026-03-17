#basicpositional
def add(a,b):
   print("a=",a)
   print("b=",b)
   return a+b
result=add(2,5)
print("sum=",result)
#student information
def studentinfo(name,roll,marks):
    print("Name:",name)
    print("Roll No:",roll)
    print("Marks:",marks)
studentinfo("Ravi",101,85)
#simple interest
def simple_interest(p,r,n):
    si=(p*r*n)/100
    print("simple interest:",si)
simple_interest(10000,2,2)
simple_interest(50000,1.2,3)    
#check number
def check_value(no):
    if(no>0):
        print("positive")
    elif(no<0):
        print("negative")
    else:
        print("Zero")
check_value(0)
check_value(90)
check_value(-15)
#odd or even
def odd_even(no):
    if(no%2==0):
        print(f"value {no} is even")
    else:
        print(f"value{no} is odd")
odd_even(50)
odd_even(15)
#arithmatic operation
def addition(a,b):
 add=a+b
 print("Addition od teo values",add)
addition(50,10.5)
addition(100,200)