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

#4)
