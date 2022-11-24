from model.Person import Person 


class PersonDAO:
  connection = None
  cursor = None

  def __init__(self, con, cur):
    self.connection = con
    self.cursor = cur

  def getAll(self):
    sql = "SELECT id, name FROM person "

    try:
      self.cursor.execute(sql)
      result = self.cursor.fetchall()

      pessoas = []
      for line in result:
        person = Person(line[0], line[1])
        people.append(person)

      return people
    except Exception as e:
      return e
