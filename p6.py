ans='y'


while(ans=='y'or ans=='Y'):
    x= 0.0
    rt=input('What is your running time: ')
    lenn=len(rt)
    if rt.isspace():
        print('this space cannot have blanks')
    elif lenn==0:
        print('must enter time')
    elif rt=='':
        print('this space cannot have blanks')
    elif rt.isalpha():
        print('you can only put number')
    else:
        rt1=float(rt)
    if rt1<5:
        print('time must be at least 5')
    else:
        while (x<rt1):
            x= x+5
            calmin=4.9*x
            print('minutes: ',x,'burned calories', calmin,'calories')
        ans=input('run again? y/n')
            
            
        
    
