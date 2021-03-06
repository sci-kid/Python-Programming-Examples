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

"""48)Tip Calculator. Complete the function, which calculates how much you need to tip
based on the total amount of the bill and the service. 
"""
import math
def calculate_tip(amount, rating):
    if rating.lower()=="terrible":
        return math.ceil(amount*0)
    elif rating.lower()=="poor":
        return math.ceil(amount*0.05)
    elif rating.lower()=="good":
        return math.ceil(amount*0.1)
    elif rating.lower()=="great":
        return math.ceil(amount*0.15)
    elif rating.lower()=="excellent":
        return math.ceil(amount*0.2)
    else:
        return "Rating not recognised"


"""49)Convert a string to an array. Write a function to split a string and convert it into an array of words.
"""
def string_to_array(s):
    if s=="":
        return [""]
    else:
        return s.split()


"""50)You have to return the digits of this number within an array in reverse order.

Unfortunately, I don't know yet how to pass this test:                     (my output)[8, 7, 7, 7, 5, 0, 1, 1] 
                                                          should equal (needed output)[0, 8, 7, 7, 7, 5, 0, 1, 1]
"""
def digitize(n):
    Reverse=0
    while n>0:
        Reminder=n%10
        Reverse=Reverse*10+Reminder
        n=n//10
    return [int(i) for i in str(Reverse)]


"""51)You will be given an vector of string(s). You must sort it alphabetically (case-sensitive!!)
and then return the first value. The returned value must be a string, 
and have "***" between each of its letters.You should not remove or add elements from/to the array.
Example: two_sort(["Lets", "all", "go", "on", "holiday", "somewhere", "very", "cold"]) should return: 'L***e***t***s'

Unfortunately, I don't know yet how to pass this test:                      (my output:)'J***Ds***D' 
                                                          should equal: (needed output:)'J***D***s***D'
"""
def two_sort(array):
    #array.sort(key=str.casefold) ->(use key for case-insensitive sorting)
    array.sort()
    j=""
    x=array[0]
    y=len(x)
    for i in x:
        if (i!=x[y-1]):
            j+=i+"***"
        else:
            j+=i
    return j
    

"""52)
likes [] // must be "no one likes this"
likes ["Peter"] // must be "Peter likes this"
likes ["Jacob", "Alex"] // must be "Jacob and Alex like this"
likes ["Max", "John", "Mark"] // must be "Max, John and Mark like this"
likes ["Alex", "Jacob", "Mark", "Max"] // must be "Alex, Jacob and 2 others like this"
For 4 or more names, the number in and 2 others simply increases.
"""
def likes(names):
    x=len(names)
    if x==0:
        return 'no one likes this'
    elif x==1:
        return names[0]+' likes this'
    elif x==2:
        return names[0]+' and '+names[1]+' like this'
    elif x==3:
        return names[0]+', '+names[1]+' and '+names[2]+' like this'
    elif x>=4:
        return names[0]+', '+names[1]+' and '+str(x-2)+' others like this'


"""53)valid_parentheses("  (")#,False)
valid_parentheses(")test")#,False)
valid_parentheses("")#,True)
valid_parentheses("hi()()")#,True)
valid_parentheses("hi(hi)()")#,True)
"""
def valid_parentheses(string):
    x=0
    y=0
    for i in string:
        if i=='(':
            x+=1
        elif i==')':
            y+=1
    if x==y:
        print('True')
    else:
        print('False')
	
	
"""54)#Get the number n (n>0) to return the reversed sequence from n to 1.
#Example : n=5 >> [5,4,3,2,1]
"""
def reverse_seq(n):
    a=[]
    while n>=1:
        a.append(n)
        n-=1
    print(a)


"""55)lowercase_count("abcABC123!@€£#$%^&*()_-+=}{[]|\':;?/>.<,~") should return ===> 3
"""
import re
def lowercase_count(strng):
    y=0
    x=re.findall("[a-z]",strng)
    for i in x:
        y+=1
    return y


"""56)array_madness([4, 5, 6], [1, 2, 3]) => True #because 4 ** 2 + 5 ** 2 + 6 ** 2 > 1 ** 3 + 2 ** 3 + 3 ** 3
Unfortunately, I don't know how to pass failed remaining tests:  Passed: 630 tests, Failed: 47 tests.
"""
def array_madness(a,b):
    x=[i**2 for i in a]
    y=[i**3 for i in b]
    if x>y:
        return True
    else:
        return False


"""57)Write a simple regex to validate a username. Allowed characters are:lowercase letters,numbers,underscore.
Length should be between 4 and 16 characters (both included).
validate_usr('asd43_34') should be equal to: True."""
import re
def validate_usr(username):
    username=username.lower()
    l=0
    q = re.findall("\w", username)
    for i in q:
        l+=1
    e=0
    x = re.findall("\s", username)
    for t in x:
        e+=1
    if l>=4 and l<=16 and e==0:
        return True
    else:
        return False


"""58)Create a function with two arguments that will return an array of the first (n) multiples of (x).
Assume both the given number and the number of times to count will be positive numbers greater than 0.
Return the results as an array.

	count_by(1, 5) should return [1, 2, 3, 4, 5]
	count_by(2, 5) should return [2, 4, 6, 8, 10]
	count_by(3, 5) should return [3, 6, 9, 12, 15]
	count_by(50, 5)should return [50, 100, 150, 200, 250]
	count_by(100, 5)should return [100, 200, 300, 400, 500]
"""
def count_by(x, n):
    temp=x
    a=[x]
    while x<temp*n:
        x=x+temp
        a.append(x)
    return a


"""59) Your task is correct the errors in the digitised text. You only have to handle the following mistakes:

    S is misinterpreted as 5
    O is misinterpreted as 0
    I is misinterpreted as 1

"""
def correct(string):
    string=string.replace("5", "S")
    string=string.replace("0", "O")
    string=string.replace("1", "I")
    return string


"""60)Replace all vowel to exclamation mark in the sentence. aeiouAEIOU is vowel.
"""
def replace_exclamation(s):
    x=['a','e','i','o','u','A','E','I','O','U']
    for j in range(0,10):
        for i in s: 
            if i==x[j]:
                s=s.replace(i,"!")
    print(s)


"""61)Get rid of numbers ending with zeros. Only the ending ones.
	no_boring_zeros(1450) should be equal 145
	no_boring_zeros(960000) should be equal 96
	no_boring_zeros(1050) should be equal 105
	no_boring_zeros(-1050) should be equal -105
	no_boring_zeros(0) should be equal 0
"""
def no_boring_zeros(n):
    if n!=0:
        while n%10==0:
            n=n//10
    else:
        n=0
    return n


"""62) find_difference([3, 2, 5], [1, 4, 4]) should be equal to 14
       find_difference([9, 7, 2], [5, 2, 2]) should be equal to 106  (find the difference of the cuboids' volumes)
       """
def find_difference(a, b):
    t1=1
    for i in a:
        t1=t1*i
    t2=1
    for i in b:
        t2=t2*i
    return abs(t1-t2)


"""63)	add_length('apple ban') => ["apple 5", "ban 3"]
        add_length('you will win') => ["you 3", "will 4", "win 3"]
"""
def add_length(str_):
    str_=str_.split()
    a=[]
    for i in str_:
        l=len(i)
        n=i+" "+str(l)
        a.append(n)
    return a


"""64)The first input array contains the correct answers to an exam, like ["a", "a", "b", "d"]. 
The second one is "answers" array and contains student's answers.

The two arrays are not empty and are the same length. Return the score for this array of answers,
giving +4 for each correct answer, -1 for each incorrect answer, and +0 for each blank answer(empty string).

If the score < 0, return 0.

For example:

checkExam(["a", "a", "b", "b"], ["a", "c", "b", "d"]) → 6
checkExam(["a", "a", "c", "b"], ["a", "a", "b",  ""]) → 7
checkExam(["a", "a", "b", "c"], ["a", "a", "b", "c"]) → 16
checkExam(["b", "c", "b", "a"], ["",  "a", "a", "c"]) → 0

"""
def check_exam(arr1,arr2):
    s=0
    for i in range(len(arr1)):
        if arr1[i]==arr2[i]:
            s+=4
        elif arr1[i]!=arr2[i]:
            if arr2[i]=="":
                s+=0
            else:
                s-=1
    if s<0:
        return 0
    else:
        return s


"""65)The number n is Evil if it has an even number of 1's in its binary representation.
The number n is Odious if it has an odd number of 1's in its binary representation.
You have to write a function that determine if a number is Evil or Odious, 
function should return "It's Evil!" in case of evil number and "It's Odious!" in case of odious number.
"""
def evil(n):
    bin_str=bin(n)
    count=0
    for i in str(bin_str):
        if i=="1":
            count+=1
    if count%2==0:
        return "It's Evil!"
    else:
        return "It's Odious!"



"""66) Your task is to remove all duplicate words from a string, leaving only single (first) words entries.

Example:

Input:

'alpha beta beta gamma gamma gamma delta alpha beta beta gamma gamma gamma delta'

Output:

'alpha beta gamma delta'

remove_duplicate_words("my cat is my cat fat") should be equal to "my cat is fat"
"""

def remove_duplicate_words(s):
    x=s.split()
    rep_d=[]
    for num in x:
        if num not in rep_d:
            rep_d.append(num)
    new=" "
    return new.join(rep_d)



"""67) Given two arrays a and b write a function comp(a, b) that checks whether the two arrays have the "same" elements,
with the same multiplicities. "Same" means, here, that the elements in b are the elements in a squared, 
regardless of the order. Valid arrays a = [121, 144, 19, 161, 19, 144, 19, 11] b = [121, 14641, 20736, 361, 25921, 361, 20736,
361] comp(a, b) returns true because in b 121 is the square of 11, 14641 is the square of 121, 20736 the square of 144,
361 the square of 19, 25921 the square of 161, and so on. """

import math
def comp(array1, array2):
    count=0
    if array1!=None and array2!=None:
        array1=list(set(array1))
        array2=list(set(array2))
        for i in range(len(array1)):
            for j in range(len(array2)):
                if array2[j]!=math.pow(array1[i],2):
                    count+=0
                elif array1[i]==math.sqrt(array2[j]):
                    count+=1
        if count==len(array2):
            return True
        else:
            return False
    else:
        return False



"""68)If s is a palindrome, then s==(reversed s)"""

def check_if_palindrome(s):
	#my first answer:
	if (s[::-1]==s):
	    return True
	else:
	    return False
	#my second answer:
	"""str=""
	for i in s:
	    str=i+str
	if (str==s):
	    return True
	else:
	    return False"""
	
	
"""69) I have to find the three largest elements in the given list"""
def three_largest_in_the_list(l):
	l.sort()
	length=len(l)
	if length==2:
	    return [l[length-2],l[length-1]]
	elif length!=0:
	    return [l[length-3],l[length-2],l[length-1]]
	else:
	    return []


"""70) I have an encoded Morse sequence. I have to decode the given sequence into English. Characters are separated by a space.
Incorrect code I have to replace with a '-'.    """
def decode_morse(l):
	m={'.-':'A','-...':'B','-.-.':'C','-..':'D','.':'E','..-.':'F','--.':'G','....':'H','..':'I','.---':'J','-.-':'K','.-..':'L','--':'M','-.':'N','---':'O','.--.':'P','--.-':'Q','.-.':'R','...':'S','-':'T','..-':'U','...-':'V','.--':'W','-..-':'X','-.--':'Y','--..':'Z'}
	res=[]
	for i in l.split(' '):
	    res.append(m.get(i))
	str1=''.join(str(i) for i in res)
	s=str1.lower()
	if l=="":
	    s=s.replace('none','')
	else:
	    s=s.replace('none','-')
	return s



"""
71) The zombies start at range metres, and move at 0.5 metres per second.
Each second, you first shoot one zombie, and then the remaining zombies shamble forwards another 0.5 metres.
If any zombies manage to get to 0 metres, you get eaten. If you run out of ammo before shooting all the zombies,
you'll also get eaten.

zombie_shootout(3, 10, 10) should be equal to "You shot all 3 zombies."
zombie_shootout(100, 8, 200) should be equal to "You shot 16 zombies before being eaten: overwhelmed."
zombie_shootout(50, 10, 8) should be equal to "You shot 8 zombies before being eaten: ran out of ammo."
"""

def zombie_shootout(zombies, distance, ammo):
    temp=zombies
    while zombies>0 and distance>0 and ammo>0:
        zombies-=1
        distance-=0.5
        ammo-=1
    if zombies==0:
        return "You shot all {} zombies.".format(temp)
    elif distance==0:
        return "You shot {} zombies before being eaten: overwhelmed.".format(temp-zombies)
    elif ammo==0:
        return "You shot {} zombies before being eaten: ran out of ammo.".format(temp-zombies)


"""
72) create a method that can determine how many letters and digits are in a given string

"""

def count_letters_and_digits(s):
    count=0
    for i in s:
        if i.isdigit() or i.isalpha():
            count+=1
    return count


"""
73) pattern(5) should be equal to "1\n22\n333\n4444\n55555"

"""

def pattern(n):
    if n>0:
        z=''
        for i in range(n):
            x=i+1
            y=x*str(x)
            if (i+1)!=n:
                z+=y+'\n'
            else:
                z+=y
    else:
        return ''
    return z



"""
74)Because Nathan knows it is important to stay hydrated, he drinks 0.5 litres of water per hour of cycling.
You get given the time in hours and you need to return the number of litres Nathan will drink, rounded to the smallest value.
For example: time = 3 ----> litres = 1; time = 6.7---> litres = 3; time = 11.8--> litres = 5
"""
import math
def litres(time):
    return math.floor(time/2)


"""
75) The exclusive or (xor(a,b)) have to evaluate two booleans. It then returns true if exactly one of the two expressions
are true, false otherwise.
"""
def xor(a,b):
    if a or b:
        if a==b:
            return False
        else:
            return True
    else:
        return False


"""
76) even_chars("") should be equal to ""            (if there're empty string)
    even_chars("abc") should be equal to "ac"       (if there're three characters)
    even_chars("abc abc") should be equal to "acac" (if with spaces)
"""
def even_chars(s):
    """Return only odd characters from substrings"""
    s=list(s.split(" "))
    x=''
    for i in s:
        for j in range(len(i)):
	    if j%2==0:
	        x+=i[j]
    return x


"""
77)

"""
