def binarysearchstr (array,find):
       for i in range(len(array)):
           array[i] = ord(array[i][0])
           print(array)
       find = ord(find[0])
       found = False
       mid = 0
       index = -1
       low = 0
       high = len(array) -1
       while low <= high and not found:
           mid = (high + low)//2
           if array[mid] == find:
               return mid
           elif array[mid] < find:
               low = mid + 1
           elif array[mid] > find:
               high = mid - 1
       return index
