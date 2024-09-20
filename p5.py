print('--program start')
print('table code: A=add , S= Subtract, M=multiply, D=divide')
cd=input('enter code')
nmbr=float(input('enter a number'))
if cd=='A' or cd=='a':
    for x in rane (1,11,1):
           answ=nmbr + x
           print(answ,'=',nmbr,'+',x)

else:
    if cd=='S' or cd=='s':
        for x in range (1,11,1):
            answ=nmbr - x
            print(answ,'=',nmbr,'=',x)

    else:
        if cd== 'M' or cd=='m':
            for x in range (1,11,1):
                answ=nmbr * x
                print(answ,'=',nmbr,'*',x)

            else:
                if cd=='D' or cd=='d':
                    for x in range (1,11,1):
                        answ=nmbr / x
                        print(answ,'=',nmbr,'/',x)

print('proram done')
