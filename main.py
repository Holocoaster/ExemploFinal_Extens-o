#Importing Person file in the Model directory

from model.Person import Person

#Importing Data file in the Database directory

from database.Database import Database

#Importing DAO file in the dao directory

from dao.PersonDAO import PersonDAO

#Usage
Human = Person()
print(Human)
print(Human.name)

#Database usage

DB = Database()

#DAO usage

personDAO = PersonDAO(db.connection, db.cursor)
people = personDAO.getAll()

for person in people:
  print(person)


