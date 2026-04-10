from typing import TextIO

def line_reader(line: str) -> str:
    #.strip removes whitespace (spaces) at the start and \n,
        #\n: it tells the progam that it is then end of a line (like your 'enter' key)
        #but also removes the [] and '' surrounding the words
    current_line = line.strip()
    return current_line
    

def main() -> None:
    #Occurs when attempting to access a file that does not exist.
        #FileNotFoundException
    #Occurs when attempting to cast an object to a type that it is not compatible with.
        #ClassCastException
    #Occurs when a function receives an argument of the correct type but an inappropriate value.
        #ValueError (Python)
    #Occurs during invalid arithmetic operations, such as division by zero.
        #ArithmeticException
    #Occurs when attempting to access an array element using an index that is outside the valid range.
        #ArrayIndexOutOfBoundsException
    #Occurs when an operation is performed on a value of the wrong data type.
        #TypeError (Python)
    #Occurs when attempting to convert a string that does not represent a valid number into a numerical type.
        #NumberFormatException

  #make a .csv file and copy and paste this into it (remove the #'s):
    #Name, Media Type 
    #Black clover, Show, 
    #Pokemon, Game
    #Happy Gilmore, Movie
    #Starlight, Song
    
    #read each line from the csv and print it 
    try:
        with open('week3.csv', 'r') as f:
            first_line = True
            #reading each line
            #each line of the .csv is a iteration 
            for line in f:
                #skipping the header
                if first_line:
                    first_line = False
                else:
                    #passing the current line into the function 'line_reader'
                    line_read = line_reader(line)
                    print(line_read)

                    with open('W_file.csv', 'w') as f2:
                        f2.write(f"{line}")
                    with open('A_file.csv', 'a') as f3:
                        f3.write(f"{line}")
    except FileNotFoundError as e:
        print("file does not exist :(")    

if __name__ == '__main__':
  main()
