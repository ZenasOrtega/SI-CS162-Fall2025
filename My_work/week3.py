from typing import TextIO

def line_reader(line: str) -> str:
    #.strip removes whitespace (spaces) at the start and \n,
        #\n: it tells the progam that it is then end of a line (like your 'enter' key)
        #but also removes the [] and '' surrounding the words
    current_line = line.strip()
    return current_line
    

def main() -> None:
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
