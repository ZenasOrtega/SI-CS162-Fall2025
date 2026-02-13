def change_list_values(list_from_main: list[int]) -> None:
    list_from_main[0] = 12

def main() -> None:
    #answer the following comments:
    x = 5
        #whats x to 5?:

    y = x
    print(id(x))
    print(id(y))
    print("\n")
    x = 1
    print(id(x))
    print(id(y))
    print("\n")
        #what do you notice about the ID's? 
    
    my_list = [1, 2, 3, 4]
    for i in my_list:
        print(i)

    print("\n")
    change_list_values(my_list)
    for i in my_list:
        print(i)

    #what do you notice about index 1 of list?
  
    #make a Food class with the follwoing
        #meal of the day = string
        #a constructor 
    
    #make the follwing, and print the results after each step
        #pancakes, breakfast
        #steak, Dinner

    #whats the difference between y = x and Steak = Pancakes

if __name__ == '__main__':
    main()

