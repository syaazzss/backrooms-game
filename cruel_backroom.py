#               INTRO

print("        WELCOME TO")
print("  C   U   L     B   C   R   O")
print("    R   E         A   K   O    M")


#------- Button works ------
while True:

button = "start game" 
print("start game")

if button == "start game" :
  print("loading...")
  print("started game")

button = "option" 
print("option")

if button == "option":
  print("select the option")
  option_button = "single player" 
  print("single player")
  option_button = "multiplayer" 
  print("multiplayer")
  levels_option = "noob" 
  print("noob")
  levels_option = "standard" 
  print("standard")
  levels_option = "pro" 
  print("pro")
  levels_option = "nightmare"
  print("nightmare")
  
  if option_button == "single player" and "noob" in levels_option :
    print("let's go")
  
  elif option_button == "single player" and "standard" in levels_option :
    print("Let's go")
  
  elif option_button == "single player" and "pro" in levels_option :
    print("Let's go")

  elif option_button == "single player" and "nightmare" in levels_option :
    print("Let's go,hero")

  elif option_button == "multiplayer" and "noob" in levels_option :
    print("create your own world")


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
  

