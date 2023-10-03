num1=int(input("Enter the 1st number: "))
num2=int(input("Enter the 2nd number: "))
Operator=input("Choose the operator for the calculation: {+ , - , * , / , % } : ")
if Operator=="+":
    sum=num1+num2
    print("The sum of the number is: ", sum)
elif Operator=="-":
    sub=num1-num2
    print("The substraction of the number is: ", sub)
elif Operator=="*":
    multi=num1*num2
    print("The multiplication of the number is: ", multi)
elif Operator=="/":
    div=num1/num2
    print("The division of the number is: ", div)
elif Operator=="%":
    rem=num1%num2
    print("The remainder of the number is: ", rem)
else:
    print("invalid operator")