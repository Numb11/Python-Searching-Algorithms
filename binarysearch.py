def binarysearchint (array,find):
       found = False
       index = 0
       while found != True:
           if array[(len(array))//2] == find:
               found = True
           elif array[(len(array))//2] > find:
               array = array[:len(array)//2]
               index = index + 1
           elif array[(len(array))//2] < find:
               array = array[len(array)//2:]
           print(array)
