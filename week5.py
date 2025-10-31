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

#make the child classes here

def main() -> None:
    #make the classes that is able to take two user intiger inputs, and add them together, print the results
    pass


if __name__ == '__main__':
    main()
