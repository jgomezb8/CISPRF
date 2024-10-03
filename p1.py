#Juan Gomez
fname=input('Type your first name')
lname=input('Type your last name')
address=input('Type address')
city=input('Type city')
state=input('Type State')
zipcode=input('Type zip code')

wname=fname+lname
loc=(city+state+zipcode)

print('\n'*3)
print(wname)
print(address)
print(loc)
