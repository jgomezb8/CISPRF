def sumxx(n):

    if n == 1:

        return 1

    else:

        return n + sumxx(n - 1)

 

def adittion(n):

    return '+'.join(str(i) for i in range(n, 0, -1))

 

def main():

    ans= 0
    while(ans ==0):

        try:

            numb = input("Enter number: ")

            if not numb.strip():
                

                print("Input cannot be blank.")

            numb = int(numb)

            if numb < 0:

                print("Number cannot be negative.")
                break

           

          

            addition_sequence = adittion(numb)

            result = sumxx(numb)

            print(f"{addition_sequence} = {result}")

       

        except ValueError as e:

            print(e)

       

       

        agn = input("Another number (y/n): ").lower()

        if agn != 'y':

            break

main()
