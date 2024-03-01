"""
This program will print numbers from 1 to 100.
For numbers devisable by 3 the program will print Crackle instead of number and Pop if number is devisable by 5.
For numbers devisable both by 3 and 5 program will print CracklePop.

"""

if __name__ == '__main__':
    for i in range(1,101): # Iterate over numbers from 1 to 100
        if i%3==0 and i%5==0: # Check if the number divides by 3 and 5 
            print('CracklePop')
        elif i%5==0: # Check if number divides by 5 
            print('Pop') 
        elif i%3==0:# Check if the number divides by 3
            print('Crackle')
        else: # For all other numbers print number 
            print(i)
