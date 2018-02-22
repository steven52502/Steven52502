print "Bike Selector"
print ("\n")
def introduction():
  print "Welcome to your Bike Selector"
  print ("\n")
  print "Let's try and find a bike that's right for you"
  print ("\n")
  select_bike()
  
def select_bike():
  print "Are you looking for Gears, suspension, speed or tires in a bike"
  print ("\n")
  print "Type g for gears, s for suspension, e for speed, or t for tires"
  answer = raw_input()
  if answer == "g":
      print "gears"
      bike_gears()
  if answer == "s":
      print "suspension"
      bike_suspension()
  if answer == "e":
      print "speed"
      bike_speed()
  else:
    print "tires"
    bike_tires()
    
def bike_gears():
  print ("\n")
  print "Based on your selection a road bike or a mountain bike seems right for you."

def bike_suspension():
  print ("\n")
  print "Based on your selection a mountain bike seems right for you."
  
def bike_speed():
  print ("\n")
  print "Based on you slection a aluminum trek bike seems right for you."
    
def bike_tires():
  print ("\n")
  print "Based on your selection a mountain bike, cruiser bike seems right for you."
    
introduction()
