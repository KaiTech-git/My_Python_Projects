for i in range(1,101): # Iterate over numbers from 1 to 100
    if i%3==0 and i%5==0: # Check if the number devides by 3 and 5 
        print('FizzBuzz')
    elif i%5==0: # Check if number divides by 5 
        print('Buzz') 
    elif i%3==0:# Check if the number devides by 3
        print('Fizz')
    else: # For all other numbers print number 
        print(i)
