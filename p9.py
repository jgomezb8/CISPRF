


def distance():
    try:
        M=float(input('miles that you want to convert-> '))
        K=M * 1.609344
        print(M,'miles to kilometers-> ',K)
    except:
        print('data error')
def temp():
    try:
        F=float(input('fahrenheits that you want to convert-> '))
        C=(F-32)*5/9
        print(F,'fahrenheit to celsius-> ',C)
    except:
        print('data error')
def weight():
    try:
        P=float(input('pounds that you want to convert-> '))
        K=P * 0.45359237
        print(P,'pounds to kilograms-> ',K)
    except:
        print('data error')
def main():
    ans='y'
    while (ans=='y')or(ans=='Y'):
        distance()
        temp()
        weight()

        ans=input('Run again? type yes or no')
        
main()





