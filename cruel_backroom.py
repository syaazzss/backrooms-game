#               INTRO

print("        WELCOME TO")
print("  C   U   L     B   C   R   O")
print("    R   E         A   K   O    M")


#--------      LOGIN ----------
while True:

button = input("click: login/make account")

if button == "login":
  username = input("username/id")
  email = input("your email")
  pin = input("your pin")
break

elif button == "make account":
  name = input("your name")
  username = input("make your username")
  email = input("your email")
  age = int(input("your age"))
  pin = input("fix your pin")
  if age <= 20 :
    print("sorry,your age isnt enough")
  else: 
    print("we sent the account activate to your email. Check it!")
  if "@" in email :
    print("valid")
  else:
    print("write your email")
  break


#------- Button works ------
while True:

button = input("click: start game/option/setting/exit game")


if button == "start game" :
  print("loading...")
  print("started game")
  break

if button == "option":
  print("select your option")
  player_option = input("select: single player/multiplayer")
  player_mode = input("select mode: noob/standard/pro/nightmare")
  
  if player_option == "single player" and player_mode == "noob" :
    print("easy mode")
  
  elif player_option == "single player" and player_mode == "standard" :
    print("medium mode")
  
  elif player_option == "single player" and player_mode == "pro":
    print("pro player")

  elif player_option == "single player" and player_mode == "nightmare" :
    print("Let's go,hero")

  elif player_option == "multiplayer" and player_mode == "noob" :
    print("create your own world")
    for_multiplayer = "create your own world"
    name_world = input("write your world here: ")
    invitation = input("write your friends id here: ")

  elif player_option == "multiplayer" and player_mode == "standard" :
    print("create your own world")
    for_multiplayer = "create your own world"
    name_world = input("write your world here: ")
    invitation = input("write your friends id here: ")

  elif player_option == "multiplayer" and player_mode == "pro":
    print("create your own world")
    for_multiplayer = "create your own world" 
    name_world = input("write your world here: ")
    invitation = input("write your friends id here: ")

  elif player_option == "multiplayer" and player_mode == "nightmare":
    print("create your own world")
    for_multiplayer = "create your own world" 
    name_world = input("write your world here: ")
    invitation = input("write your friends id here: ")
  break


if button == "settings" :
  volume = input("volume 0-100: ")
  print(f"volume {volume}")
  sensitivity = input("low/standard/ high: ")
  print(f"sensitivity {sensitivity}")
  head_boobing = input("low/standard/high: ")
  print(f"head_boobing {head_boobing}")
  forward_button = input("W: ")
  print(f"forward {forward_button}")
  step_back_button = input("S: ")
  print(f"step back {step_back_button}")
  right_button = input("D: ")
  print(f"right {right_button}")
  left_button = input("A: ")
  print(f"left {left_button}")
  break

else:
  exit_pop_up = input("are u sure you want to exit the game? Yes/No: ")
  if exit_pop_up = "Yes":
    print("closing the game")
  else:
    print("back to the game")
  break
     
  
  
  

