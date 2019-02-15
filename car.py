# Basics of classes and objects. 


# A class is a blue print for the creation of an object 

# A class has 2 things 
# Properties / Attrubutes 
# methods / 
class Car:
  def __init__(self, name, fuel_type, color, mileage, price ):
    self.name = name
    self.fuel_type = fuel_type
    self.color = color 
    self.mileage = mileage
    self.price = price 

  def get_details(self):
    print("Car name: " + self.name)
    print("Fuel type: " + self.fuel_type)
    print("Color: " + self.color)
    print("Mileage: " + str(self.mileage)) 
    print("Price: " + str(self.price ))

  def minimum_details(self):
      print('Car name: ' + self.name)
      print('Car Color: '+ self.color ) 

  def setColor(self, color ):
      self.color = color 

# these are objects 
# object 1
c1 = Car('BMW', 'Diesel', 'Red', 20, 2000000 ) 
# object 2
c2 = Car('Maruti', 'Petrol', 'Granite', 20, 2000000 ) 
# object 3 
c3 = Car("Nano", "Diesel", 'Purple', 32, 100000)

c3.setColor('yellow')

# Objects are created using a blue print defined by a class 

list_of_cars = [ c1, c2, c3 ] 

name_of_car = input('Please enter car name: ')

for i in range( len(list_of_cars) ):
    if list_of_cars[i].name == name_of_car:
        list_of_cars[i].get_details()