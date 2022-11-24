class PersonDAO:
  conexao = None
  cursor = None

  def __init__(self, con, cur):
    self.connection = con
    self.cursor = cur

  def getAll(self):
    sql = "SELECT id, name FROM person "

    try:
      self.cursor.execute(sql)
      resultado = self.cursor.fetchall()

      pessoas = []
      for linha in resultado:
        pess = Person(linha[0], linha[1])
        people.append(person)

      return pessoas
    except Exception as e:
      return e
