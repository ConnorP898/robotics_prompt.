tvShow = input("What is your favourite tv show? ")
if tvShow == "peppa pig":
  print("Ugh, why?")
  faveCharacter = input("Who is your favourite character? ")
  if faveCharacter == "daddy pig":
    print("Right answer")
  else:
    print("Nah, Daddy Pig's the greatest")
elif tvShow == "paw patrol":
  print("Aww, sad times")
else:
  print("Yeah, that's cool and all…")
  
# "Fix my code" the spacing of the if/else, and #elif statements where wrong.#

order = input("What would you like to order: pizza or hamburger? ")
if order == "hamburger":
  print("Thank you.")
  cheese = input("Do you want cheese?")
  if cheese == "yes":
    print("You got it.")
  else: 
    print("No cheese it is.")
elif order == "pizza":
  print("Pizza coming up.")
  toppings = input("Do you want pepperoni on that?")
  if toppings == "yes"
    print("We will add pepperoni.")
  else:
    print("Your pizza will not have pepperoni.")

# Day 7 Challenge #
print("Fake Fan Finder")
print("----------------")
print( )
favouriteArtist = input("What is your favourite show? ")
if favouriteArtist == "kendrick" or "K.dot":
  print("Oh really?")
  favouriteSong = input("Name me any of his songs? ")
  if favouriteSong == "how much a dollar cost" or "alright" or "blacker the berry":
    print("cool")
  else:
    print ("okay")
    favouriteAlbum = input("What is his best album? ")
    if favouriteAlbum == "To Pimp a Butterfly" or "TPAB":
      print("You are a true fan.")
    else:
      print("You are a fake fan.")
elif favouriteArtist == "kanye" or "ye":
  print("Oh really?")
  favouriteSong = input("Name me any of his songs? ")
  if favouriteSong == "devil in a new dress" or "no more parties in LA":
    print("cool")
  else:
    print ("okay")
    firstAlbum = input("What was first album? ")
    if firstAlbum == "the college dropout" or "TCD":
      print("You are a true fan.")
    else:
      print("You are a fake fan.")
