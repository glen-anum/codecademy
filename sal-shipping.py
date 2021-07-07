weight= 41.5
# Ground Shipping.
if weight==0:
  print("no weight")
if weight <=2:
  cost=weight * 1.50 + 20
elif weight <=6:
  cost=weight * 3.00 + 20
elif weight <=10:
  cost=weight * 4.00 + 20
else:
  cost=weight * 4.75 + 20
print("Price of Ground Shipping:", cost)

# Ground Shipping Premium
ground_charge = weight + 125
print("Price of Ground Charge :",ground_charge )


#Drone Shipping
if weight==0:
  print("no weight")
if weight <=2:
  cost=weight * 4.50 
elif weight <=6:
  cost=weight * 9.00 
elif weight <=10:
  cost=weight * 12.00 
else:
  cost=weight * 14.25 
print("price of Drone Shipping:", cost)

