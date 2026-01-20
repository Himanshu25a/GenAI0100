# Q1
# for i in range(51):
#     if i%3==0 and i%5==0:
#         print("FizzBuzz")
#     elif i%3==0:
#         print("Fizz")
#     elif i%5==0:
#         print("Buzz")
#     else:
#         print(i)


# Q2
# for i in range(2,101):
#     prime=True
#     for j in range(2,i):
#         if i%j==0:
#             prime=False
#             break
#     if prime:
#             print(i)

# Q3
# score=int(input("Enter Your Score:"))
# if score>100:
#     print("Invalid Score")
# elif score>=90:
#     print("A Grade")
# elif score>=80 and score<=89:
#     print("B Grade")
# elif score>=70 and score<=79:
#     print("C Grade")
# elif score>=60 and score<=69:
#     print("D Grade")
# else:
#     print("Fail")

# Q4
# n=int(input("Enter Number:"))
# for i in range(1,11):
#     print(n,"X",i,"=",n*i)
    
# Q5
# l1=[i*i for i in range(1,20) if i%2==0 ]
# print(l1)

# Q6
# n1=int(input("Enter the Year:"))
# if n1%4==0 or n1%400==0:
#     print("A leap Year")
# elif n1%4!=0 or n1%100!=0:
#     print("Not a leap Year ")
# else:
#     print("invalid")


# Q7
# a=int(input("Enter 1st Side of Triangle:"))
# b=int(input("Enter 2nd Side of Triangle:"))
# c=int(input("Enter 3rd Side of Triangle:"))
# if (a*a+b*b==c*c) or (b*b+c*c==a*a) or (a*a+c*c==b*b):
#     print("Right Angle Triangle")
# elif (a==b==c):
#     print("Equilateral Triangle")
# elif (a==b) or (b==c) or (c==a):
#     print("Isosceles Triangle")
# else:
#     print("Scalen Triangle")




# # Q8
# n3=int(input("Enter Number:"))
# if n3==0:
#     print("Zero")
# elif n3>0:
#     print("Positive")
# elif n3<0:
#     print("Negative")
# else:
#     print("Invalid Number")


# Q9
# w=int(input("Enter the Weight in Kgs:"))
# h=float(input("Enter Height in Meters:"))
# bmi=w/(h**2)
# print(bmi)
# if bmi<18.5:
#     print("Underweight")
# elif bmi>=18.5 and bmi<=24.9:
#     print("Normal Weight")
# elif bmi>=25 and bmi<=29.9:
#     print("Overweight")
# else:
#     print("Obesity")

# Q10
# n4=int(input("Enter The Day:"))
# if n4==1:
#     print("Monday")
# elif n4==2:
#     print("Tuesday")
# elif n4==3:
#     print("Wednesday")
# elif n4==4:
#     print("Thursday")
# elif n4==5:
#     print("Friday")
# elif n4==6:
#     print("Saturday")
# elif n4==7:
#     print("Sunday")
# else:
#     print("Invalid")

# Q11
# price=int(input("Enter The Price:"))
# discount_price=0
# discount=0
# if price>=1000:
#     discount="10%"
#     discount_price=(price*10)/100
# elif 500<=price<1000:
#     discount="5%"
#     discount_price=(price*5)/100
# else:
#     discount="No Discount"
# total_price=price-discount_price
# print("Price:",price)
# print("Discount:",discount)
# print("Total Price",total_price)

# Q12
# n=int(input("Enter Number:"))
# sum=0
# for i in range(1,n+1):
#         sum+=i
#         print(sum)

# Q14
# n=input("Enter Your String:")
# vowels="aeiouAEIOU"
# count=0
# for i in n:
#     if i in vowels:
#         count+=1
# print(count)

# Q15
# n1=int(input("Enter 1st Number:"))
# n2=int(input("Enter 2nd Number:"))
# print(n1+n2)


# Q16
# n=5
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print("*",end="")
   
#     print()


# Q17
# n=int(input("Enter Number:"))
# l1=[i for i in range(0,n) if i%2==0 ]
# print("Even Numbers are:",l1)


