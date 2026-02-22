# menetapkan nama dan umur dengan __init__()
class Person:       
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("Emil", 36) 

print(p1.name)
print(p1.age)

# tanpa __init__() maka harus membuat secara manual
class Person:       
  pass

p1 = Person()
p1.name = "Tobias"
p1.age = 25

print(p1.name)
print(p1.age)

# metode __init__() dapat mengatur nilai untuk parameter
class Person:       
  def __init__(self, name, age=18):
    self.name = name
    self.age = age

p1 = Person("Emil")
p2 = Person("Tobias", 25)

print(p1.name, p1.age)
print(p2.name, p2.age)

# metode __init__() dapat memiliki pameter sebanyak yang dibutuhkan
class Person:       
  def __init__(self, name, age, city, country):
    self.name = name
    self.age = age
    self.city = city
    self.country = country

p1 = Person("Linus", 30, "Oslo", "Norway")

print(p1.name)
print(p1.age)
print(p1.city)
print(p1.country)