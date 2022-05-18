def binarysearchint (array,find):
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
print(binarysearchint([2,31,40,44,52,56,57,60],60))
