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
      break
      else: 
        print("we sent the account activate to your email. Check it!")
      if "@" in email :
        print("valid")
      break
      else:
        print("write your email")
 


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
        for_multiplayer = ("create your own world")
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
      print(f"/nsensitivity {sensitivity}")
      head_boobing = input("low/standard/high: ")
      print(f"/nhead_boobing {head_boobing}")
      forward_button = input("W: ")
      print(f"/nforward {forward_button}")
      step_back_button = input("S: ")
      print(f"/nstep back {step_back_button}")
      right_button = input("D: ")
      print(f"/nright {right_button}")
      left_button = input("A: ")
      print(f"/nleft {left_button}")
      lean_right_button = input("E: ")
      print(f"/nlean_right {lean_right_button}")
      lean_left_button = input("Q: ")
      print(f"/nlean_left {lean_left_button}")
      use_button = input("R: )
      print(f"/nuse {use_button}")
      break

    else:
      exit_pop_up = input("are u sure you want to exit the game? Yes/No: ")
        if exit_pop_up = "Yes":
          print("closing the game")
          break
        else:
          print("back to the game")
          break
     
  
  
  

