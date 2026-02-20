#perameter names should be called X and Y

#meanings of each parts of the function
    #def: this means define (we are defining a function)
    #addition: this is the function name (we'll use this to call the function)
    #within the () are parameter variables 
        #(during the function call what ever variables the call sent, will copy into these
        #parameters, in the order they were given)
    # -> int: this defines the functions retrun type

#a new function has to be defined above main so that the program knows what the function is
    #as it runs main
def addition(X: int, Y: int) -> int:
    return X+Y
    #instead of doing the following steps:
        #New_variable = X + Y
        #return New_variable
    #return X+Y: will return the int value, which the function is set up to return a int value 

def main() -> None:
    #make a function that is able to take two user intiger inputs, and add them together, print the results
    #in the given comment lines answer the small prompts 
    X = int(input('what is the first number you want to add?'))
    Y = int(input('what is the second number you want to add?'))

    #start here
    #were printing the return value
        #addition(X,Y)
            #were calling the function called 'addition' which will send
            #main's X and Y values
    print(addition(X,Y))

    #are X and Y in main the same variables as X and Y in your function?: no
    #what happens if you use None as the return type?: 

    #make a loop that adds A by X, Y times
    A = int(input('What number should we add to? '))

    #for varible i (i is defined in the for loop) in range of Y
        #i is going to be added by 1 until its >= Y
        #[0, 1, 2, 3]
    for i in range(Y):
        A = A+X    
    print(A)


    #same concept but with the other type of loop
  
    A = int(input('What number should we add to? '))

    #this is similar to the for loop above
    #here we make a variable i which = 0
        #this is our iterator
    i = 0
    #while the statement of (i < Y) is still true
        #do the following code
    while i < Y:
        A = A+X
        i = i+1
        #once to the bottom go back to the top
    print(A)

    #When do we use either loop?
        #theyre techincally interchangeable, however; best to use for loops when you have a set amount of times youll be iterating

if __name__ == '__main__':
    main()
