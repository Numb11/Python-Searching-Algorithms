def bubblesort(sorteds):
  while not sorted(sorteds) == sorteds:
   for i in range(len(sorteds)):
    if i > 0:
     print(i)
     if sorteds[i] < sorteds[i-1]:
        print(sorteds[i], sorteds[i-1])
        cache = sorteds[i]
        sorteds[i] = (sorteds[i-1])
        sorteds[i-1] = (cache)
  return sorteds
print(bubblesort([9,5,4,15,3,8,11]))
