def linear(items,item):
     for i in items:
         if i == item:
            return (f"Item found at index {items.index(item)}")
     return (f"Item was not found in {items}")
print(linear(input("Enter the items to be searched:").split(),input("What item is being searched for:")))
