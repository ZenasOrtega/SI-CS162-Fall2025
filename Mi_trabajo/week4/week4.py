import car 

def main() -> None:
  user_wage = float(input('whats your monthly payment\n'))

  #creando un nuevo objecto "car" que se llama "McQueen"
    #lo vamos a pasar 3 valuares:
      #Corvette
      #4
      #20000
  McQueen = car.Car("Corvette", 4, 20000)

  #vamos a llamar los funciones que un objecto "car" tiene
  McQueen.print_info()

  #Adentro de el archivo "car" hay 2 funciones, lo vamos a llamar
    #(nombre del archivo).(funcion que quieres accesar)---
  car.monthly(user_wage, McQueen)
  car.tire_condtions(McQueen)

if __name__ == '__main__':
  main()
