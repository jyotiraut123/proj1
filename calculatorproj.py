def add(a,b):
    ans=a+b
    print("Addition=",ans)
def sub(a,b):
    ans=a-b
    print("Sub=",ans)
def mul(a,b):
    ans=a*b
    print("mul=",ans)
def div(a,b):
    ans=(a/b)
    print("Div=",ans)

while True:
    choice = int(input("\nEnter Choice:\n1.Addition\n2.Substraction\n3.Multiplication\n4.Division\n5.Exit"))
    match choice:
        case 1:
            print("Addition")
            fn = int(input("Enter First Number = "))
            sn = int(input("Enter Second Number = "))
            add(fn,sn)
        case 2:
            print("Substraction")
            fn = int(input("Enter First Number = "))
            sn = int(input("Enter Second Number = "))
            sub(fn,sn)
        case 3:
            print("Multiplication")
            fn = int(input("Enter First Number = "))
            sn = int(input("Enter Second Number = "))
            mul(fn,sn)
        case 4:
            print("Division")
            fn = int(input("Enter First Number = "))
            sn = int(input("Enter Second Number = "))
            div(fn,sn)
        case 5:
            print("Exiting")
            break
