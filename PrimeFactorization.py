"""
The program will look for all prime factors of a given number. 
"""

if __name__ == '__main__':
    p = 2 # first prime number
    f_list = [] #factors list initialization
   
    # Error handling validating if user entered integer.
    while True: 
        try:
            n = int(input('Enter number that you want to factorized: '))
            if n>1:
                break
            else:
                print('Please try again enter integer greater than 1.')
        except ValueError:
            print('Please try again enter integer greater than 1.')
   
   # Algorithm searching for prime factors      
    while n>= p**2:
        if n%p ==0:
            f_list.append(p)
            n=n/p
        else:
            p+=1
    f_list.append(int(n))
    print(f_list)
    
    