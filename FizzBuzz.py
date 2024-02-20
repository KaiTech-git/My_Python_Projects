"""
This program will print th number from 1 to 100.
For multipliers of 3 the program will print Fizz instead of number and Buzz if number is multiples of 5.
For multiples of both 3 and 5 program will print FizzBuzz
"""

if __name__ == '__main__':
    for i in range(1,101): # Iterate over numbers from 1 to 100
        if i%3==0 and i%5==0: # Check if the number divides by 3 and 5 
            print('FizzBuzz')
        elif i%5==0: # Check if number divides by 5 
            print('Buzz') 
        elif i%3==0:# Check if the number divides by 3
            print('Fizz')
        else: # For all other numbers print number 
            print(i)
