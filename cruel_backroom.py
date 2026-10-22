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
  age = input("your age")
  pin = input("fix your pin")
  if age <= 20 :
    print("sorry,your age isnt enough")
  print("we sent the account activate to your email. Check it!")



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
  
  if option_button == "single player" and player_mode == "noob" :
    print("easy mode")
  
  elif option_button == "single player" and and player_mode == "standard" :
    print("medium mode")
  
  elif option_button == "single player" and player_mode == "pro":
    print("pro player")

  elif option_button == "single player" and player_mode == "nightmare" :
    print("Let's go,hero")

  elif option_button == "multiplayer" and player_mode == "noob" :
    print("create your own world")
    for_multiplayer = create your own world
    name_world = input("write your world here: ")
    invitation = input("write your friends id here: ")

  elif option_button == "multiplayer" and player_mode == "standard" :
    print("create your own world")
    for_multiplayer = create your own world
    name_world = input("write your world here: ")
    invitation = input("write your friends id here: ")

  elif option_button == "multiplayer" and player_mode == "pro":
    print("create your own world")
    for_multiplayer = create your own world
    name_world = input("write your world here: ")
    invitation = input("write your friends id here: ")

  elif option_button == "multiplayer" and player_mode == "nightmare":
    print("create your own world")
    for_multiplayer = create your own world
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
  

