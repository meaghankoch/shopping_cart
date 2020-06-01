
#i = 1
#while i < 21:
 # print(i)


#for p in products:
 #   my_price = p["price"]
  #  print(f" + {p['name']} (${my_price})")







#products ["id"] = 1
#while products["id"] == 1 :  # This constructs an infinite loop
 #  num = raw_input("Enter a product identifier  :")
 #  print("You entered: ", num)
 #


 
matching_product = [p for p in products if str(p["id"]) == str(selected_id)]
print(matching_product)
print(type(matching_product)

#