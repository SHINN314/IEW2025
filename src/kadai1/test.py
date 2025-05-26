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

  if selection == "1":
    print("Start game!")
    # square chomp
    # init variables
    bot_name = "bot"
    player_name = "you"
    n = int(input("Input size of square board: "))

    bot = SquareChompBot()
    chomp = Chomp(row=n, col=n, next_player=bot_name, prev_player=player_name)

    while(not chomp.is_finished):
      if chomp.next_player == bot_name:
        # bot operate
        bot.delete_space(chomp=chomp)

      else:
        # player operate
        row_delete = input("Input row of delete space: ")
        col_delete = input("Input column of delete space: ")
        chomp.delete_space(row=row_delete, col=col_delete)

    
if __name__ == "__main__":
  main()