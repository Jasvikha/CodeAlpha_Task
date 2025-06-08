def bot():
  print("WELCOME!!")
  while True:
    uinput=input("me: ").upper()
    if uinput=="HELLO":
      print("BOT: HI!")
  
    elif uinput == "HOW ARE YOU":
      print("BOT: I'M FINE , THANKS!")
    elif uinput == "BYE":
      print("BOT: GOODBYE!")
      break 
    else:
      print("BOT: I DON'T UNDERSTAND.")

bot()