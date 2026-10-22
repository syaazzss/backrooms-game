#               INTRO

print("        WELCOME TO")
print("  C   U   L     B   C   R   O")
print("    R   E         A   K   O    M")


#------- Button works ------

button = input("write: start game/option/settings/exit game")


if button == "start game" :
  print("loading...")
  print("started game")

elif button == "option":
  print("select the option")
  option_button = input("write: single player/multiplayer")
  levels_option = input("write: noob/standard/pro/nightmare")
  
  if option_button == "single player" and levels_option in ["noob","standard","pro","nightmare" ] :
    print("let's go")
  
  elif option_button == "multiplayer" and levels_option in ["noob","standard","pro","nightmare"] :
    print("Crete your world")
if button == "settings" :
  volume = input(volume 0-100: )
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
  

