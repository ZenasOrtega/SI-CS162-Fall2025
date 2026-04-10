import car 

def main() -> None:
  #prompting the user
  user_wage = float(input('whats your monthly payment\n'))

  #creating a object "McQueen" that is a "car" object
  McQueen = car.Car("Corvette", 4, 20000)
  McQueen.print_info()

  #inside the "car" file, there are 2 functions we can access
    #(name of the file).(functions you want to access)---
  car.monthly(user_wage, McQueen)
  car.tire_condtions(McQueen)



if __name__ == '__main__':
  main()
