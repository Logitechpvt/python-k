class Car:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model
  def move(self):
    print("Drive!")
class Boat:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model
  def move(self):
    print("Sail!")
class Plane:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model
  def move(self):
    print("Fly!")
Car1=Car("Ford", "Mustang")       #Create a Car class
boat1=Boat("Ibiza", "Touring 20") #Create a Boat class
plane1=Plane("Boeing", "747")     #Create a Plane class

for x in (Car1, boat1, plane1):
  x.move()
\
\









