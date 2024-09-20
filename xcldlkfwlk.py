def distance():
    M=float(input('miles that you want to convert-> '))
    K=M * 1.609344
    print(M,'miles to kilometers-> ',K)

def temp():
    F=float(input('fahrenheits that you want to convert-> '))
    C=(F-32)*5/9
    print(F,'fahrenheit to celsius-> ',C)

def weight():
    P=float(input('pounds that you want to convert-> '))
    K=P * 0.45359237
    print(P,'pounds to kilograms-> ',K)

def main():
    distance()
    temp()
    weight()
main()
    


