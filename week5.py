class Vehicle:
    num_of_wheels : int
    doors : int
    manu : str
    _owner : str
    def __init__(self, num_of_wheels : int, num_doors : int, manu_name : str, _owner : str) -> None:
        self.num_of_wheels = num_of_wheels
        self.doors = num_doors
        self.manu = manu_name
        self._owner = _owner

    def Honk(self) -> None:
        print("Beep Beep")
    
    #make any other fxns neccessary here
        #default specialty that all vehicles can do
        #a getter for the owners name
        

#make the child classes here
 #the car class needs to consist of
    #a "special" string attribute that says what it's specifically good at 

    #a fxn that overwrites the honk fxn to the cars special type of honking sound
    #print what that specific car can do that the others cant
    #a getter fxn that gets the owner's name

def main() -> None:
    #mkae the following child classes
        #your favorite car
        #semi truck
        #fisher price car
        #dirtbike

    #make a fxn that passes all over your different vehicles into one fxn that prints all their neccessary info in a loop
    pass


if __name__ == '__main__':
    main()
