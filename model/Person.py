class Person():

  #Attributes

 id = None
 name = None

  #Constructor method

def __init__(self, id, name):
  self.id = id
  self.name = name

  #Exhibition 

  def __str__(self):
   return f"{self.name} ({self.id})"
  
  