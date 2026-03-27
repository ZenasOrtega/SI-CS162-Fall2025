from copy import deepcopy 

class Food:
    Meal_time: str
    
    def __init__(self, x: str) -> None:
        self.Meal_time = x

def change_the_meal_time(x: Food) -> None:
    x.Meal_time = "lunch"

def change_list_values(list_from_main: list[int]) -> None:
    list_from_main[0] = 12

def main() -> None:
    #answer the following comments:
    x = 5
        #whats x to 5?:
            #x is a reference to value 5

    y = x
    print(id(x))
    print(id(y))
    print("\n")
    x = 1
    print(id(x))
    print(id(y))
    print("\n")
        #what do you notice about the ID's? 
            #theyre the same initially buut difference when x = 1
    
    my_list = [1, 2, 3, 4]
    for i in my_list:
        print(i)

    print("\n")
    change_list_values(my_list)
    for i in my_list:
        print(i)

    #what do you notice about index 1 of list?
        #it changed
  
    #make a Food class with the follwoing
        #meal of the day = string
        #a constructor 
    
    #make the follwing, and print the results after each step
        #pancakes, breakfast
        #steak, Dinner
    Pancakes = Food("Breakfast")
    Steak = Food("Dinner")
    print(f"Pancakes = {Pancakes.Meal_time}")
    print(f"Steak = {Steak.Meal_time}")
    
    #remove the comment
    Steak = Pancakes #shallow copy
    print(f"Steak = {Steak.Meal_time}")

    #now make a function that accepts pancake as perameter and changes its meal time to lunch
    change_the_meal_time(Pancakes)
    print(f"Pancakes = {Pancakes.Meal_time}")
    print(f"Steak = {Steak.Meal_time}")

    #whats the difference between y = x and Steak = Pancakes
        #steak is a ref to an object that pancakes is a refrence to
        #since integers are immuntable, y doesn't change with x
        #mutable objects are more complex stuff like classes and lists
    
    #how do i make a copy and not a direct reference
    Steak = deepcopy(Pancakes) #deepcopy

if __name__ == '__main__':
    main()
