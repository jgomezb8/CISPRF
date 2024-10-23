mydict={1:'I',7:'VII',13:'XIII',19:'XIX',2:'II',8:'VIII',
            14:'XIV',20:'XX',3:'III',9:'IX',15:'XV',21:'XXI',
            4:'IV',10:'X',16:'XVI',22:'XXII',5:'V',11:'XI',
            17:'XVII',23:'XXIII',6:'VI',12:'XII',18:'XVIII',24:'XXIV'}

def main():
    
    print(mydict)

    aa=int(input('which number do you want to know in roman -> '))
    if aa=='':
        print ('this space cannot be in blank')
    elif aa in mydict:
        print('your number in roman is -> ',mydict[aa])
    elif aa not in mydict:
        ad=input('would you like this new number to mydict? y/n -> ')
        if ad=='y' or ad=='Y':
            cc=input('Whats the roman value of the new number -> ')
            if cc.isalpha():
               Nmydict=mydict[aa]=cc
               print('Your value has been added')
               print(Nmydict)
            else:
                print('must be a roman number')
    else:
        print('end of the program')
            
    
    

    ans=input('Run again? y/n -> ')
    while ans=='y' or ans=='Y':
        main()
    else:
        print('End of the program')

main()
        


