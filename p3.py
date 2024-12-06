import math
NP=float(input('How many pounds of screw would you like to buy; '))
Dis=0
if(Np>=10)and(Np<=99.99):
    Dis=(GS*0.10)
elif(Np>=100)and(Np<=999.99):
    Dis=(GS*0.20)
elif(Np>=1000)and(Np<=9999.99):
    Dis=(GS*0.30)
elif(Np>=10000):
    Dis=(GS*0.40)
else:
    Dis=0


FinA= (GS-Dis)

print('Number of pounds: ',Np)
print('Gross sales: ',GS)
print('Discount: ',Dis)
print('Final amount : ',FinA)
