from typing import Generic, TypeVar
from abc import ABC, abstractmethod

class Animals:
  Spc: str
  Noise: str

  def __init__(self, spc: str, sound: str) -> None:
    self.Spc = spc
    self.Noise = str

  @abstractmethod
  def noise(self) -> None:
    pass

#child classes here


class Zoo:
  _Animals: list[Animals] 

  def __init__(self) -> None:
    self._Animals = []

  def print_zoo(self) -> None:
    for i in self._Animals:
      i.noise()

  #add the method to be able to append a new animal to the Zoo's list

def main() -> None:
  Portland_zoo = Zoo()
  #make a class for the following
    #lion
    #Turtle
    #Monkey

  #print the info out using the Zoo class method
  

if __name__ == '__main__':
    main()
