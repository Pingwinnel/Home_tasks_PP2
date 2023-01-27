fruits = {"apple", "banana", "cherry"}
if "apple" in fruits:
  print("Yes, apple is a fruit!")   #Yes, apple is a fruit!
  

fruits = {"apple", "banana", "cherry"}
fruits.add("orange")     #apple", "banana", "cherry"  "orange"

fruits = {"apple", "banana", "cherry"}
more_fruits = ["orange", "mango", "grapes"]
fruits.update(more_fruits)     #"apple", "banana", "cherry" "orange", "mango", "grapes"

fruits = {"apple", "banana", "cherry"}
fruits.remove("banana")   #"apple"  "cherry"
 
fruits = {"apple", "banana", "cherry"}
fruits.discard("banana")  #"apple"  "cherry"

 
  