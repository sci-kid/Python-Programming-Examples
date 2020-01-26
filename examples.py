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

#20)The program takes a number n and prints an inverted star pattern of the desired size:
n=int(input("enter a number:"))
for i in range(n,0,-1):
    print((n-i)*' '+i*'*')

#21)The program takes a range and prints prime numbers in that range using Sieve of Eratosthenes:
n=int(input('enter a number:'))
sieve=set(range(2,n+1))
while sieve:
    prime=min(sieve)
    sieve-=set(range(prime,n+1,prime))
    print(prime,end='\t')

#22)The program takes in a date and checks if it a valid date and prints the incremented date if it is:
date=input('enter a date:')
dd,mm,yy=date.split('/')
dd=int(dd)
mm=int(mm)
yy=int(yy)
if(mm==1 or mm==3 or mm==5 or mm==7 or mm==8 or mm==10 or mm==12):
    max1=31
elif(mm==4 or mm==6 or mm==9 or mm==11):
    max1=30
elif(yy%4==0 and yy%100!=0 or yy%400==0):
    max1=29
else:
    max1=28
if (mm<1 or mm>12):
    print('the date is invalid')
elif (dd<1 or dd>max1):
    print('the date is invalid')
elif (dd==max1 and mm!=12):
    dd=1
    mm=mm+1
    print('the incremented date is:',dd,mm,yy,sep='/')
elif (dd==31 and mm==12):
    dd=1
    mm=1
    yy=yy+1
    print('the incremented date is:',dd,mm,yy,sep='/')
else:
    dd=dd+1
    print('the incremented date is:', dd, mm, yy,sep='/')

#23)The program computes simple interest given the principle amount, rate and time:
principle=float(input('enter amount:'))
yy=int(input('enter years:'))
rate=float(input('rate:'))
interest=(principle*yy*rate)/100
print('interest is:',interest)

#24)The program takes in a year and checks whether it is a leap year or not:
year=int(input('enter a year:'))
if (year%4==0 and year%100!=0 or year%400==0):
    print('leap year')
else:
    print('not leap year')

#25)The program reads the height in centimeters and then converts the height to feet and inches:
cm=int(input('enter the height in centimeters:'))
inches=0.394*cm
feets=0.0328*cm
print('the height in feets is:',round(feets,2))
print('the height in inches is:',round(inches,2))

#25) The program prints the sum of negative numbers, positive even numbers and positive odd numbers in a given list:
n=int(input('enter the number of elements:'))
b=[]
for i in range(0,n):
	x=int(input('enter an element:'))
	b.append(x)
sum1=0
sum2=0
sum3=0
for j in b:
	if (j>0):
		if (j%2==0):
			sum1=sum1+j
		else:
			sum2=sum2+j
	else:
		sum3=sum3+j
print('sum of:elem>0,elem%2==0',sum1)
print('sum of:elem>0,elem%2!=0',sum2)
print('sum of:elem<0',sum3)

#26)The program takes in a list and prints the largest even and largest odd number in a list:
n=int(input('enter the number of elements:'))
b=[]
for i in range(0,n):
    a=int(input('enter an element:'))
    b.append(a)
c=[]
d=[]
for i in b:
    if (i%2==0):
        c.append(i)
    else:
        d.append(i)
c.sort()
d.sort()
count1=0
count2=0
for i in c:
    count1=count1+1
for i in d:
    count2=count2+1
print('the largest even number is:',c[count1-1])
print('the largest odd number is:',d[count2-1])

#27)The program takes an integer and forms a new integer which has the number of digits at the ten’s place and the least significant digit in the one’s place:
n=int(input('enter the number:'))
temp=n
k=0
while (n>0):
    k=k+1
    n=n//10
b=str(temp)
c=str(k)
d=c+b[k-1]
print('new number is:',int(d))

#28)The program takes a number and checks if it is an Armstrong number:
n=int(input('enter the number:'))
a=list(map(int,str(n)))
b=list(map(lambda x:x**3,a))
if (sum(b)==n):
    print('It is armstrong number.')
else:
    print('It is not an armstrong number.')

#29)The program takes a number and checks if it is a Perfect number:
n=int(input('enter a number:'))
sum1=0
for i in range (1,n):
    if (n%i==0):
        sum1=sum1+i
if (sum1==n):
    print('it is perfect number!')
else:
    print('it is not a perfect number!')

#30)The program takes in a number and checks if it is a prime number:
n=int(input("enter a number:"))
k=0
for i in range(2,n//2+1):
    if (n%i==0):
        k=k+1
if (k<=0):
    print(n,'is a prime number!')
else:
    print(n,'isn\'t a prime number!')

#31)The program takes a list and removes the duplicate items from the list:
n=int(input('enter the number of elements:'))
a=[]
for i in range (0,n):
    m=int(input('enter the element '+str(i+1)+':'))
    a.append(m)
b=set()
unique=[]
for i in a:
    if i not in b:
        unique.append(i)
        b.add(i)
print('Non-duplicate list:',unique)

#32)The program takes a string and checks if a substring is present in the given string:
string=input('enter a string:')
sub_string=input('enter a sub-string:')
if (string.find(sub_string)==-1):
    print('there is no sub-string in string!')
else:
    print('there is a sub-string in a string!')

#33)The program takes a dictionary and removes a given key from the dictionary:
d={'a':1,'b':2,'c':3,'d':4}
key=input('enter the key to be deleted(a,b,c or d):')
if key in d:
    del d[key]
else:
    print('the key doesn\'t exist!')
print('updated dictionary:',d)

#----------------------https://www.codewars.com/users/Artem%20Kravchenko/completed----------------below:-->------------

#34)Count of positives / sum of negatives
"""Return an array, where the first element is the count of positives numbers 
and the second element is sum of negative numbers.
If the input array is empty or null, return an empty array."""
def count_positives_sum_negatives(arr):
    a=[]
    x=0
    for i in arr:
        if i>0:
            x+=1
        elif i<0:
            a.append(i)
    if len(arr)==0:
        return arr
    else:
        return [x,sum(a)]

"""35)If there are one or two good ideas("good"), return 'Publish!', 
if there are more than 2 return 'I smell a series!'.
If there are no good ideas(only elements. named "bad" in list), as is often the case, return 'Fail!'."""
def well(x):
    m=0
    for i in x:
        if len(i)==4:
            m+=1
    if m==0:
        return 'Fail!'
    elif m==1 or m==2:
        return 'Publish!'
    elif m>2:
        return 'I smell a series!'

#36)Find the smallest integer in the array
def find_smallest_int(arr):
    arr.sort()
    return arr[0]

"""37)Invert values (Given a set of numbers, return the additive inverse of each.
Each positive becomes negatives, and the negatives become positives.)"""
def invert(lst):
    return [-i for i in lst]

#38)Given an array of integers, return a new array with each value doubled.
def maps(a):
    return [i*2 for i in a]

"""39)Count the Monkeys! Given the number (n), populate an array with all numbers up to and including that number,
but excluding zero.
For example:
monkeyCount(10) # --> [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
monkeyCount(1) # --> [1]   """
def monkey_count(n):
    a=[]
    for i in range(1,n+1):
        a.append(i)
    return a

"""40)Century From Year(The first century spans from the year 1 up to and including the year 100, 
The second - from the year 101 up to and including the year 200, etc.)"""
def century(year):
    if year%100==0:
        return year//100
    else:
        return ((year//100)+1)

"""41)Personalized greeting
Create a function that gives a personalized greeting. This function takes two parameters: name and owner.
Use conditionals to return the proper message:
case 	                return
name equals owner 	'Hello boss'
otherwise 	        'Hello guest'         """
def greet(name, owner):
    if (name==owner):
        return 'Hello boss'
    else:
        return 'Hello guest'

#42)Abbreviate a Two Word Name
"""Write a function to convert a name into initials. This kata strictly takes two words with one space in between them.
The output should be two capital letters with a dot separating them.
It should look like this:
Sam Harris => S.H
Patrick Feeney => P.F
"""
def abbrevName(name):
    a,b=name.split(" ")
    return (a[0]+"."+b[0]).upper()

"""43)Return the Nth Even Number
nthEven(1) //=> 0, the first even number is 0
nthEven(3) //=> 4, the 3rd even number is 4 (0, 2, 4)
nthEven(100) //=> 198
nthEven(1298734) //=> 2597466
"""
def nth_even(n):
    i=2
    for i in range(0,n):
        i-=1
        n+i
    return n+i

"""44)Simple, remove the spaces from the string, then return the resultant string.
"""
def no_space(x):
    return x.replace(" ", "")

"""45)Your goal is to create a function that removes the first and last characters of a string.
You're given one parameter, the original string. You don't have to worry with strings with less than two characters.
"""
def remove_char(s):
    x=len(s)
    return s[1:x-1]

#46)Reversed Strings
def solution(string):
   return string[::-1]

#47)Find numbers which are divisible by given number
def divisible_by(numbers, divisor):
    a=[]
    for i in numbers:
        if i%divisor==0:
            a.append(i)
    return a

