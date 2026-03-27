#los nombres de los parametros tienen que ser X y Y

#que significa cada parte de un funcion
    #def: esto significa 'defenir' (estamos definiendo una funcion)
    #"addition": esto es el nombre de la funcion (lo usemos para llamarlo)
    #adentro de () son los variables parametros
        #(durante la llamada a la funcion, los variables que mandasteis desde main se van a copiar en estos parametros en el orden en que lo mandasteis)
        # -> int: esto define el tipo de valuar que la funcion TIENE que regresar
            #en este ejemplo, es tipo int

#una nueva funcion necesite que se defina arriba de main, para que la programa sepa que function es quando lo corres 
    #una programa se corre como un lee (de izquierda a derecha, de arriba a abajo)
def addition(X: int, Y: int) -> int:
    return X+Y
    #es mas facil, endeves de hacer esto:
        #New_variable = X + Y
        #Return New_Variable
    #return X+Y: va regresar el valor que es tipo int


def main() -> None:
    #make a function that is able to take two user intiger inputs, and add them together, print the results
        #in the given comment lines answer the small prompts
    #crea una funcion que puede tomar dos respuestas enteros, y sumarlas, imprimir los resultados 
        #en las lineas comentarios, responde 

    #nombre_de_un_variable = tipo_de_data_(input('pregunta'))
        #input(): deja que el usor puede dar respuesta a la programa 
            #int(input()): cambia el valor de la respuesta a tipo int
    X = int(input('what is the first number you want to add?'))
    Y = int(input('what is the second number you want to add?'))

    #start here/empieza aqui

    #estamos imprimiendo el valor que la funcion regresa 
        #addition(X,Y) 
            #estamos llamando a la funcion que se llama "addition" donde se va a mandar los valores de X y Y de main
    print(addition(X,Y))

    #are X and Y in main the same variables as X and Y in your function?
    #X y Y de main son los mismos variables como X y Y en tu funcion?
        #Answer/Respuesta: no

    #what happens if you use None as the return type?
    #que pasa si tienes None como el tipo de regresa de tu funcion?
        #Answer/Respuesta: the function should return nothing, return is not needed


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

if __name__ == '__main__':
    main()
