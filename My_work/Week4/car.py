class Car:
    make: str
    num_wheels: int
    price: float

    def __init__(self, name: str, num_wheels: int, price: float)-> None:
        self.make = name
        self.num_wheels = num_wheels
        self.price = price

    def print_info(self) -> None:
        print(self.make)
        print(self.num_wheels)
        print(self.price)




def monthly(wage: int, car: Car) -> None:
    if wage <= 0:
        print("cant afford a car")
    else:
        monthly = (car.price)/(wage * 20)
        print(f"your monthly is {monthly}")
    
    #with try and catches
    #try:
     #   monthly = (car.price)/(wage * 20)
    #except ZeroDivisionError as e:
     #   print(f"error, we have a {e}")
        

#fxn to check the conditions of tires
  #the user will inpuit each individual tires condition, if in 'bad' call some fxn
def tire_condtions(car: Car) -> None: 
    for i in range(car.num_wheels):
        cond = input(f'Whats the condition of tire {i +1} \n')

        if cond == "bad":
            print('called mechanic')
