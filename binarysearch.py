def types(array):
   array = list(map(type,array))
   if len(array) == array.count(array[0]):
      return True
   else:
      return False

class arrays:
   def __init__(self, length,array,typey):
          self.length = length
          self.type = typey
          if types(array) == True:
            self.actarray = array
          else:
            print("Type error, input values do not match")
            exit()

   def appends(self,item):
         if len(self.actarray) < self.length and isinstance(item,self.type):
             self.actarray.append(item)

   def array(self):
       print(self.actarray)


p1 = arrays(3,[1,2],int)
p1.appends("cheese")
p1.array()
