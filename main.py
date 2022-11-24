#Importing Person file in the Model directory

from model.Person import Person

#Importing Data file in the Database directory

from database.Database import Database

#Usage
Human = Person(1, "Holden Caulfield")
print(Human)
print(Human.name)

#Database usage

DB = Database()


