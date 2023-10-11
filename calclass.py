class Calculator:
    def calculator(self,ch,n1,n2):
            if ch=='1':
                result=n1+n2
                print(f'Sum:{result}')
                return 1
            elif ch=='2':
                result=n1-n2
                print(f'Difference:{result}')
                return 1
            elif ch=='3':
                result=n1*n2
                print(f'Product:{result}')
                return 1
            elif ch=='4':
                result=n1/n2
                print(f'Quotient:{result}')
                return 1
            elif ch=='5':
                result=n1%n2
                print(f':Remainder:{result}')
                return 1
            elif ch=='6':
                return 0
            else:
                print("Invalid opyion")
n1=int(input("Enter first no:"))
n2=int(input("Enter second no:"))
f=1
while f:
    print("Press 1-Add 2-Subtract 3-multiply 4-division 5- modulus 6-Exit")
    ch=input("Enter choice:")
    calc=Calculator()
    f=calc.calculator(ch,n1,n2)
