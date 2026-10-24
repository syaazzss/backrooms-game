#               INTRO

print("        WELCOME TO")
print("  C   U   L     B   C   R   O")
print("    R   E         A   K   O    M")


#--------      LOGIN ----------

while True:
  
    button = input("click: login/make account").lower().strip()

    if button == "login":
      username = input("username/id: ") 
      email = input("your email: ")
      pin = input("your pin: ")
      break
    elif button == "make account": 
      name = input("your name: ")
      username = input("make your username: ")
      your_age = int(input("your age: "))
      if your_age <= 19 :
        print("sorry, your age isnt enough")
        break
      else:
        while True:
            your_email = input("your email: ")
            if "@gmail.com" in your_email :
              print("valid")
              break
            else:
              print("write your email!")

        pin = input("fix your pin: ")
        print("we sent OTP code to your email. check it!")
        OTP = 1234
        while True:    
            OTP_code = int(input("OTP: "))
            if OTP_code == OTP :
              print("right")
              break
            else:
              print("wrong")
        break
        



#------- Button works ------
while True:

    button = input("click: start game/option/setting/exit game").lower().strip()


    if button == "start game" :
      print("loading...")
      print("started game") 
      continue 
    elif button == "option":
      print("select your option")
      player_option = input("select: single player/multiplayer").lower().strip()
      player_mode = input("select mode: noob/standard/pro/nightmare").lower().strip()
      if player_option == "single player" :
          if player_mode == "noob" :
            print("easy mode")
          elif player_mode == "standard" :
            print("medium mode")
          elif player_mode == "pro" :
            print("hard mode")
          elif player_mode == "nightmare" :
            print("good luck")
      elif player_option == "multiplayer" :
          if player_mode == "noob" :
            print("create your world")
            world = input("name world: ")
            invitation = input("write your friends id")
            print(f"inviting {invitation} to {world}")
          elif player_mode == "standard" :
            print("create your world")
            world = input("name world: ")
            invitation = input("write your friends id")
            print(f"inviting {invitation} to {world}")
          elif player_mode == "pro" :
            print("create your world")
            world = input("name world: ")
            invitation = input("write your friends id")
            print(f"inviting {invitation} to {world}")
          elif player_mode == "nightmare" :
            print("create your world")
            world = input("name world: ")
            invitation = input("write your friends id")
            print(f"inviting {invitation} to {world}")
            continue         
    if button == "setting" :
      settings = input("volume/sensitivity/head bobbing/keyboard button").lower().strip()
      if settings == "volume" :
        volume_setting = int(input("0-100"))
        print(f"your volume {volume_setting}")
      elif settings == "sensitivity" :
        sensitivity_setting = input("low/standard/high").lower().strip()
        print(f"your sensitivity {sensitivity_setting}")
      elif settings == "head bobbing" :
        head_bobbing = input("low/standard/high").lower().strip()
        print(f"your head bobbing {head_bobbing}")
      elif settings == "keyboard button" :
        button = input("forward/step back/right/left/lean right/lean left/jump/run/squat/use/inventory").lower().strip()
        if button == "forward" :
          button = input("W: ")
        elif button == "step back" :
          button = input("S: ")
        elif button == "right" :
          button = input("D: ")
        elif button == "left" :
          button = input("A: ")
        elif button == "lean right" :
          button = input("E: ")
        elif button == "lean left" :
          button = input("Q: ")
        elif button == "jump" :
          button = input("space: ")
        elif button == "squat" :
          button = input("enter: ")
        elif button == "use" :
          button = input("R: ")
        elif button == "inventory" :
          button = input("Tab: ")
        continue
    elif button == "exit game" :
      exit_pop_up = input("are u sure you want to exit the game? yes/no: ").lower().strip()
      if exit_pop_up == "yes":
        print("closing the game")
        break
      elif exit_pop_up == "no" :
        print("back to the game")
        continue             
    
