#definiendo un nuevo clase que se llama "Vehicle"
class Vehicle:
    #aqui son lose differentes variables, estos variables llamamos los atributos de las clase "Vehicle"
    num_of_wheels : int
    doors : int
    manu : str
    _owner : str
    
    #aqui es un funcion definido abajo de la clase "Vehicle"
        #mira especificamente a este funcion, se llama "__init__"
    def __init__(self, num_of_wheels : int, num_doors : int, manu_name : str, _owner : str) -> None:
        #lo que este funcion hace, es recibe los parametros y lo aplica a los atributos de "Vehicle"
            #recibe: el objecto que llamo, y 4 variables
            #en este caso, "self" es el objecto de clase "Vehicle" que llamo al funcion "__init__()"
        self.num_of_wheels = num_of_wheels
        self.doors = num_doors
        self.manu = manu_name
        self._owner = _owner

    #estos son otros funciones que un "Vehicle" puede llamar
    def Honk(self) -> None:
        print("Beep Beep")

    def Special_feat(self) -> None:
        print("Drive on road")

    def get_owner(self) -> None:
        print(self._owner)

#make the child clases here
    #aqui estamos diciendo que "Semi_truck", es un clase que tambien tiene todos los atributos y funcions que un "Vehicle" tendra
    #estos tipos de clases llamamos los clases "hijos"
class Semi_truck(Vehicle):
    #esto es un nuevo atributo abajo de la clase "Semi_truck", que solamente los clases "Semi_truck" tienen acceso
    Special: str


    #la mimso idea 
    def __init__(self, num_of_wheels : int, num_doors : int, manu_name : str, _owner : str) -> None:
        #aqui "super()" hace que accese un atributo de la clase padre "Vehicle", en este caso, la funcion para iniciar los attributos 
        super().__init__(num_of_wheels, num_doors, manu_name, _owner)
        self.Special = "Haul cargo"
    
    #la funcion de "Honk" que viene de las clase padre, está sobrescrita solamente para esta clase hijo
        #por ejemplo, si la clase hijo no tendra la funcion "honk", endeves llama la funcion de la clase padre
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
    
    def Honk(self) -> None:
        print("FAAAAAAAAAAAAAACK")

    def Special_feat(self) -> None:
        print(self.Special)

    def owner_name(self):
        super().get_owner()
    
#aqui es el funcion para primir la information (lo llamamos en "main")
def print_all_vehicles(lov: list[Vehicle])-> None:
    #porque una lista de "Vehicles"?
        #porque una "Semi_truck" no es un "DirtBike" o "F1"
            #cada clase hijos, son differentes
        #PERO todo los clases hijos son "Vehicles"
            #"una troca no es un moto, pero un moto y troca son autos!"
    #esto nos deja a manadar todos los differentes clases de hijos sin hacer mucho trabajo

    #aqui vamos a primir la informacion de cada "Vehicle"
    for i in lov:
        #"i" va a iterar cada objecto en la lista
            #en main la lista se ve haci
                #[RedBull, DB, Semi]
        i.Honk()
        i.Special_feat()
        print() #para que se vea bien en el terminal
        #aqui se var repitir otra ves pero para la proxima objecto en la lista

def main() -> None:
    #vamos hacer una lista de objectos "Vehicle"
    list_of_vehicles = []

    #aqui estamos diciendo esto
        #estamos construyendo un variable "Semi" que va ser un objecto de tipo "Semi_truck"
            #los "semi_truck" tambien son de clase "Vehicle"
        #al mismo tiempo de constuir el objecto "Semi", llamaos al funcion "__init__" de la clase "Semi_truck", no de la clase "Vehicle"
            #pasamos los 4 valores al funcion 
                #nota que no pasamos nada para "self", automáticamente un objecto se pasa solito si un funcion tiene self en sus parametros
    Semi = Semi_truck(8,2,"ford","Mack")
    list_of_vehicles.append(Semi) #lista: frente [Semi] atras

    DB =  DirtBike(2,0,"Kawasaki","Kenivel")
    list_of_vehicles.append(DB) #lista: [DB, Semi]

    RedBull_f1 = F1(4,0,"RedBull","Verstappen")
    list_of_vehicles.append(RedBull_f1) #lista: [RedBull, DB, F1]
    
    #llamamos a un function que var a primir information de cada objecto en la lista
    print_all_vehicles(list_of_vehicles)

    

if __name__ == '__main__':
    main()
