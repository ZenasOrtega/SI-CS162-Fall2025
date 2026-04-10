from typing import TextIO

def line_reader(line: str) -> str:
    #.strip elimina espacios en blanco al inicio y el \n
        #\n: le dice al programa que es el final de una línea (como presionar 'Enter')
        #también elimina los [] y '' alrededor de las palabras
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
    
  #crea un archivo .csv y copia y pega esto dentro (quita los #'s):
    #Name, Media Type 
    #Black clover, Show 
    #Pokemon, Game
    #Happy Gilmore, Movie
    #Starlight, Song
    
    #lee cada línea del csv y la imprime
    try:
        with open('week3.csv', 'r') as f:
            first_line = True
            #leyendo cada línea
            #cada línea del .csv es una iteración
            for line in f:
                #saltando el encabezado
                if first_line:
                    first_line = False
                else:
                    #pasando la línea actual a la función 'line_reader'
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
