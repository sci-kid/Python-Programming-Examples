#1)The program takes the elements of the list one by one and displays the average of the elements of the list:
n=int(input("enter the number of elements:"))
a=[]
for i in range(0,n):
    elem=int(input("enter the element:"))
    a.append(elem)
avg=sum(a)/n
print("average number is:",round(avg,2))

#2)The program takes both the values from the user and swaps them without using temporary variable:
a=int(input("enter the number of a:"))
b=int(input("enter the number of b:"))
a=a+b
b=a-b
a=a-b
print("a:",a,"b:",b)

#3)This is a Python Program to read a number n and compute n+nn+nnn:
n=int(input("enter the number:"))
temp=str(n)
temp1=temp+temp
temp2=temp+temp+temp
comp=n+int(temp1)+int(temp2)
print("n+nn+nnn:",comp)

#4)The program takes a number and reverses it:
n=int(input("enter the number:"))
rev=0
while (n>0):
    dig=n%10
    rev=rev*10 + dig
    n=n//10
print("reverse number is:",rev)

#5)The program takes a number and checks whether it is positive or negative:
n=int(input("enter the number:"))
if (n>0):
    print("the number is positive")
else:
    print("the number is negative")
    
#6)The program takes in the marks of several subjects and displays the grade:
m=int(input("enter the number of subjects:"))
a=[]
for i in range(0,m):
    n=int(input("enter the mark of the subject:"))
    a.append(n)
avg=int(sum(a)/m)
if (avg>=90):
    print("grade is A")
elif (avg<90&avg>=80):
    print("B")
elif (avg<80&avg>=70):
    print("C")
elif (avg<70&avg>=60):
    print("D")
else:
    print("E")
    
#7)The program prints all numbers in a range divisible by a given number:
lower=int(input("enter the lower limit:"))
upper=int(input("enter the upper limit:"))
n=int(input("enter the number, to be divided by:"))
for i in range(lower, upper+1):
    if (i%n==0):
        print(i)
        
#8)Python Program to read two numbers and print their quotient and remainder:
a=int(input("number one:"))
b=int(input("number two:"))
quotient=a//b
remainder=a%b
print("quotient:",quotient,"remainder:",remainder)

#9)The program takes several distinct numbers and prints all possible combinations from the digits:
n=int(input("enter the number of digits:"))
a=[]
for i in range(0,n):
    elem=int(input("enter the digit:"))
    a.append(elem)
for i in range (0, n):
    for j in range(0, n):
        for k in range(0,n):
            if (i!=j&j!=k&k!=i):
                print(a[i],a[j],a[k])
                
#10)The program takes the upper and lower limit and prints all odd numbers within a given range:
lower=int(input("lower limit:"))
upper=int(input("upper limit:"))
for i in range(lower, upper+1):
    if (i%2!=0):
        print(i)
        
#11)The program takes in a number and finds the sum of digits in a number:
n=int(input("enter the number:"))
tot=0
while (n>0):
    dig=n%10
    tot=tot+dig
    n=n//10
print("sum of the digits of number is:",tot)

#12)The program takes in an integer and prints the smallest divisor of the integer:
n=int(input("enter the number, which will be divisible:"))
a=[]
for i in range (2,n+1):
    if (n%i==0):
        a.append(i)
a.sort()
print("the smallest number, which is divisible, is:",a[0])

#13)The program takes the number and prints the number of digits in the number:
n=int(input("enter the number:"))
count=0
while (n>0):
    count = count + 1
    n = n//10
print("the number of digits in number is:", count)

#14)The program takes a number and checks whether it is a palindrome or not:
n=int(input("enter the number:"))
temp=n
rev=0
while (n>0):
    dig=n%10
    rev=rev*10+dig
    n=n//10
if (temp==rev):
    print("the number is a palindrome")
else:
    print("the number isn't a palindrome")

#15)The program prints all integers that aren’t divisible by either 2 or 3 and lies between 1 and 50:
for i in range(0,51):
    if(i%2!=0&i%3!=0):
        print(i)

#16)The program takes a number and generates all the divisors of the number:
n=int(input("enter the integer:"))
print("the divisors of the integer are:")
for i in range(1, n+1):
	if (n%i==0):
		print(i)

#17)The program takes a number n and prints and computes the series “1+2+…+n=”:
n=int(input("enter the number:"))
a=[]
for i in range(1,n+1):
    print(i,sep='',end='')
    if (i<n):
        print("+",sep='',end='')
    a.append(i)
print("=",sum(a))

#18)The program takes a number n and prints the natural numbers summation pattern:
n=int(input('enter a number:'))
for j in range(1,n+1):
    a=[]
    for i in range(1,j+1):
        print(i,sep='',end='')
        if (i<j):
            print('+',sep='',end='')
        a.append(i)
    print('=',sum(a), sep='',end='\n')

#19)The program takes a number n and prints an identity matrix of the desired size:
n=int(input('enter a number:'))
for i in range(1,n+1):
    for j in range(1,n+1):
        if (i==j):
            print('1', sep='',end=' ')
        else:
            print('0', sep='',end=' ')
    print()
