import numpy as np

def fib_sequence (n):
    """
    Calculates the fibonacci terms to a specific (nth) term using Binet's formula.

    Argument n: requires a positive integer argument

    return: returns a numpy array of fibonacci term till the provided nth term
    """
    # a list of numbers to represent the first n fibonacci terms
    terms = np.arange(1,n+1)
    sqrt5 = np.sqrt(5)
    phi = np.divide(np.add(1,sqrt5) , 2)
    fib = np.rint(((phi**terms)-((-phi)**(-terms)))/sqrt5)
    return fib

if __name__ == '__main__': # Usage sample and testing
    improper_input = True
    while(improper_input):
        user_input = input("Enter the nth term: ")
        try:
            term_number = int(user_input)
            if (term_number>0):
                improper_input=False
                print(fib_sequence(term_number)) # can be replaced with your code that uses the function
            else:
                print("make sure to input a term number that is greater than 0")
        except:
            print("Invalid Input!")
    