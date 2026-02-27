#make a recursive fxn that is able to add incrementing numbers X times, where X is the user input, retunr the sum
    #ex say IP = 3, then it be 1+2+3 = 6, return 6
def sum_incrementing(n):
    #Base case: if n is 1 or less, return that since we dont want to add the negatives (it'll loop forever)
    if n <= 1:
        return n

    #Recursive case
    return n + sum_incrementing(n - 1)

#make a recursive fxn that can identify if a string is a palindrome (attempt first w/out notes :)
    #ex "racecar" is backwards for "racecar" 
def is_palindrome(s):
    #Base case: empty string or single character
    if len(s) <= 1:
        return True

    #if first and last characters don't match
    if s[0] != s[-1]:
        return False

    # Recursive case: check the substring w/out first and last char
    return is_palindrome(s[1:-1])

#make a recursive fxn for the fibonacci sequence (same here, attempt first w/out notes
    #ex 0+1+1+2+3+5+8 (the next number is the sum of the previous two)
def fibonacci(n):
    #Base cases: we reached the base case where the final two left are 0 and 1 which are the start 
        #of the fibonacci sequence 
    if n == 0:
        return 0
    if n == 1:
        return 1

    #Recursive case: here we're looping backwards
    return fibonacci(n - 1) + fibonacci(n - 2)

#make a recursive fxn that is able to print out the factors of a user inputted number
  #ex IP = 20, then it prints: 1, 2 , 4 , 5, 10, 20
def print_factors(n, divisor=1):
    #the (n, divisor=1) is the same as (n) with initilizing the divisor below
    #Base case: divisor can't be greater than n (not a factor at that point)
    if divisor > n:
        return

    #if divisor is a factor, print it
        #recall % opperation = the remainder 
    if n % divisor == 0:
        print(f"{divisor} ")

    #Recursive call
    print_factors(n, divisor + 1)


def main():
    #1. Sum incrementing numbers
    x = int(input("Enter a number to sum up to: "))
    print("Sum:", sum_incrementing(x))

    #2. Palindrome check
    word = input("Enter a string to check palindrome: ")
    print("Is palindrome:", is_palindrome(word))

    #3. Fibonacci
    n = int(input("Enter Fibonacci position: "))
    print("Fibonacci number:", fibonacci(n))

    #4. Print factors
    num = int(input("Enter number to print factors: "))
    print("Factors:")
    print_factors(num)


if __name__ == "__main__":
    main()
