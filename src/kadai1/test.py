from chomp import Chomp
from chomp_bot import SquareChompBot

import time # debug

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

  if selection == "1":
    print("Start game!")
    # square chomp
    # init variables
    bot_name = "bot"
    player_name = "you"
    n = int(input("Input size of square board: "))
    bot = SquareChompBot()
    chomp = Chomp(row=n, col=n, next_player=bot_name, prev_player=player_name)

    print("Game start!")
    chomp.print_board()

    time.sleep(1)

    while(not chomp.is_finished):
      if chomp.next_player == bot_name:
        # bot operate
        print(bot_name + " turn")
        bot.delete_space(chomp=chomp)
        time.sleep(1) # debug

      else:
        # player operate
        row_delete = int(input("Input row of delete space: "))
        row_delete -= 1
        col_delete = int(input("Input column of delete space: "))
        col_delete -= 1
        chomp.delete_space(row=row_delete, col=col_delete)
    
if __name__ == "__main__":
  main()