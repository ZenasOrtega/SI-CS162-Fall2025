from typing import Generic, TypeVar
from abc import ABC, abstractmethod

class Animal:
  Spc: str
  Noise: str

  def __init__(self, spc: str, sound: str) -> None:
    self.Spc = spc
    self.Noise = sound

  @abstractmethod #method must be made in the child classes
  def noise(self) -> None:
    pass

#child classes here
class Lion(Animal):
  def __init__(self) -> None:
    super().__init__("Feline", "ROAR")

  def noise(self) -> None:
    print(self.Noise)

class Monkey(Animal):
  def __init__(self) -> None:
    super().__init__("Sapien", "OO OO")

  def noise(self) -> None:
    print(self.Noise)

class Turtle(Animal):
  def __init__(self) -> None:
    super().__init__("Testudines", "eep")
  
  def noise(self) -> None:
    print(self.Noise)

class Zoo:
  _Animals: list[Animal] 

  def __init__(self) -> None:
    self._Animals = []
  
  def append_to_zoo(self, New_friend: Animal) -> None:
    self._Animals.append(New_friend)q

  def print_zoo(self) -> None:
    for i in self._Animals:
      i.noise()

def main() -> None:
  Portland_zoo = Zoo()
  Alex = Lion()
  Curious_George = Monkey()
  Leonardo = Turtle()
  Portland_zoo.append_to_zoo(Alex)
  Portland_zoo.append_to_zoo(Curious_George)
  Portland_zoo.append_to_zoo(Leonardo)
  #make a class for the following
    #lion
    #Turtle
    #Monkey

  #print the info out using the Zoo class method
  Portland_zoo.print_zoo()
  

if __name__ == '__main__':
    main()
