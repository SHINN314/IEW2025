from chomp import Chomp
from chomp_bot import SquareChompBot

def main():
  # main menu
  print("""\
_________ .__                           
\_   ___ \|  |__   ____   _____ ______  
/    \  \/|  |  \ /  _ \ /     \\____ \ 
\     \___|   Y  (  <_> )  Y Y  \  |_> >
 \______  /___|  /\____/|__|_|  /   __/ 
        \/     \/             \/|__|    """)
  print("-" * 100)
  print("Welcome to Chomp!")
  print("Select number what you do next.")
  print("1. Start game")
  print("2. Check rules")
  print("3. Exit")
  selection = input("Select number: ")
  print("-" * 100)

  if selection == 1:
    # square chomp
    row = input("Input row of the board: ")
    col = input("Input col of the board: ")
    next_player = "bot"
    prev_player = "you"
    chomp = Chomp()
    
if __name__ == "__main__":
  main()