#defining the class called "Vehicle"
class Vehicle:
    #here are the different variables, these are called attributes of the "Vehicle" class
    num_of_wheels : int
    doors : int
    manu : str
    _owner : str
    
    #here is a function defined under the "Vehicle" class
        #look specifically on the name of the function, its called "__init__"
    def __init__(self, num_of_wheels : int, num_doors : int, manu_name : str, _owner : str) -> None:
        #what this function does, is it recieves parameter and sets them to the variables of this specific "Vehicle" object
            #recieves: the object that the function was called from, and 4 paramters
            #in this case, "self" is the object of the "Vehicle" class that called the "__init__()" function
        self.num_of_wheels = num_of_wheels
        self.doors = num_doors
        self.manu = manu_name
        self._owner = _owner

    #these are other functions a "Vehicle" can call
    def Honk(self) -> None:
        print("Beep Beep")

    def Special_feat(self) -> None:
        print("Drive on road")

    def get_owner(self) -> None:
        print(self._owner)

#make the child clases here
    #here were saying that "Semi_truck" is a class that also has the attributes and functions of a "Vehicle" class
      #these are called child classes
class Semi_truck(Vehicle):
    #this is a new attribute under the "Semi_truck" class, only the "Semi_truck" class objects have access to
    Special: str

    #same idea 
    def __init__(self, num_of_wheels : int, num_doors : int, manu_name : str, _owner : str) -> None:
        #here "super()" allows access to a parent object/"go up one level" to access something, in this case, the init function of a "Vehicle" class 
        super().__init__(num_of_wheels, num_doors, manu_name, _owner)
        self.Special = "Haul cargo"
    
    #the "Honk" function that comes from the parent class, is overwritten just for this child class
        #for example, if the child class didn't have a "Honk" function, it would instead call the parent's
    def Honk(self) -> None:
        print("HONK HONK")

    def Special_feat(self) -> None:
        print(self.Special)

    def owner_name(self):
        super().get_owner()

class DirtBike(Vehicle):
    Special: str

    def __init__(self, num_of_wheels : int, num_doors : int, manu_name : str, _owner : str) -> None:
        super().__init__(num_of_wheels, num_doors, manu_name, _owner)
        self.Special = "Do a flip!"
    
    def Honk(self) -> None:
        print("meep meep")

    def Special_feat(self) -> None:
        print(self.Special)

    def owner_name(self):
        super().get_owner()

class F1(Vehicle):
    Special: str

    def __init__(self, num_of_wheels : int, num_doors : int, manu_name : str, _owner : str) -> None:
        super().__init__(num_of_wheels, num_doors, manu_name, _owner)
        self.Special = "tu tu tutu MAX VERSTAPPEN"
    
    @override
    def Honk(self) -> None:
        print("FAAAAAAAAAAAAAACK")

    def Special_feat(self) -> None:
        print(self.Special)

    def owner_name(self):
        super().get_owner()
    
#hre is the print function, called from main
def print_all_vehicles(lov: list[Vehicle])-> None:
    #why does it accept a "Vehicles" list?
        #because a "Semi_truck" is not a "Dirtbike" or "F1"
            #each child class is different
        #BUT all the child classes are "Vehicles"
            #"a truck is NOT a bike, BUT a bike and a truck are vehicles!"
    #this allows us to send a variety of different child classes without doing more work

    #here were printing the info of each "Vehicle"
    for i in lov:
        #"i" iterates each object in the list
            #in main the list goes like this
                #[RedBull, DB, Semi]
        i.Honk()
        i.Special_feat()
        print() #to make the terminal look clean
        #here its going to repeat again, but for the next object in the list

def main() -> None:
    #lets make a list of "Vehicle" objects
    list_of_vehicles = []

    #here we are saying this
        #we are creating a variable "Semi" that will be an object of type "Semi_truck"
            #"Semi_truck" is also a "Vehicle"
        #at the same time we construct the object "Semi", we call the "__init__" function of the "Semi_truck" class, not "Vehicle"
            #we pass 4 values into the function
                #note that we don’t pass anything for "self"; a object automatically passes itself when a function has "self"
    Semi = Semi_truck(8,2,"ford","Mack")
    list_of_vehicles.append(Semi) #list: front [Semi] back

    DB =  DirtBike(2,0,"Kawasaki","Kenivel")
    list_of_vehicles.append(DB) #list: [DB, Semi]

    RedBull_f1 = F1(4,0,"RedBull","Verstappen")
    list_of_vehicles.append(RedBull_f1) #list: [RedBull, DB, F1]
    
    #calling a function that will print all the info of each object in the list
    print_all_vehicles(list_of_vehicles)

    

if __name__ == '__main__':
    main()
