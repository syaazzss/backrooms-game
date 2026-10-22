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

