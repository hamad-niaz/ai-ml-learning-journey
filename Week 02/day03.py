# class Student:
#     def __init__ (self, name, age):
#         self.name = name
#         self.age = age   
#     def greet(self):
#         print(f'Hi, I am {self.name}')
# s1 = Student("Ali", 20)
# s1.greet()



# # class car:
# #     def __init__(self, brand, year):
# #         self.brand = brand
# #         self.year = year
# #     def discription (self.):
# #         print(self.brand)
# # c1 = car("BMW")




#### Instance vs Class Variales and Methods



# class Student:
#     school = "Navttc"
#     def __init__(self, name):
#         self.name = name
# s1 = Student('Ali')
# s2 = Student('Sara')
# print(s1.name, s2.name)
# print(s1.school, s2. school)



\

###### #### Task

# class employee:
#     company ="Saad"
#     def __init__(self, name):
#         self.name = name
        
# c1 = employee("Ahsan")
# c2 = employee("\nAli")
# c3 = employee("\nSaim")

# print(c1.name,c2.name, c3.name)










######### Constructors  Destructors

# class Student:
#     def __init__(self, name):
#         self.name = name
#         print(f'{self.name} created')
#     def __del__(self):
#         print(f'{self.name} destoyed')
# s1 = Student('Ali')
# del s1


#####
##### Task


# class Book:
#     def __init__(self, Title):
#         self.Title = Title
#         print(f'{self.Title} created')
#     def __del__(self):
#         print(f'{self.Title} destoyed')
# B01 = Book ('abc')
# del B01


#### Inheritance (Single, Multilevel, Hierarchical)


# class Animal:
#     def eat (self):
#         print('Eating...')
# class dog(Animal):
#     def bark (self):
#         print('Barking....')
# d = dog()
# d.eat()
# d.bark()

# #####Task....

# class Vehic:
#     def start (self):
#         print('vehic...')
# class BMW(Vehic):
#     def honk (self):
#         print('  add Honk....')
# h = BMW()
# h.start()
# h.honk()


#####Task....


class Shape:
    
    def draw(self):
        print('Shape...')

class Circle(Shape):

    def area(self):
        print('Circle area...')

class Square(Shape):

    def area(self):
        print('Square area...')

c = Circle()
s = Square()

c.draw()
c.area()

s.draw()
s.area()