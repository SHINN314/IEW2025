from chomp import Chomp
from chomp_bot import ChompBot

def main():
  print("""\
 _______               _______    _________ .__                           
 \      \    /\|\/\    \      \   \_   ___ \|  |__   ____   _____ ______  
 /   |   \  _)    (__  /   |   \  /    \  \/|  |  \ /  _ \ /     \\____ \ 
/    |    \ \_     _/ /    |    \ \     \___|   Y  (  <_> )  Y Y  \  |_> >
\____|__  /   )    \  \____|__  /  \______  /___|  /\____/|__|_|  /   __/ 
        \/    \/\|\/          \/          \/     \/             \/|__|    """)
  print("-" * 100)
  print("Welcome to Chomp!")
  print("Select number what you do next.")
  print("1. Start game")
  print("2. Check rules")
  print("3. Exit")
  selection = input("Select number: ")
  print("-" * 100)

  if selection == "1":
    # first player is bot
    print("Input the size of the board.")
    n = input("Input n: ")
    chomp = Chomp(int(n), int(n))
    chomp_bot = ChompBot()

    # first turn
    print("-" * 100)
    print("Bot's turn")
    print(f'Bot delete up-ritgt space ({chomp.row-2}, 1)')
    chomp_bot.delete_space(chomp, chomp.row-2, 1)
    chomp.print_board()

    while chomp.is_finished == False:
      print("-" * 100)
      print("Your turn")
      input("Input row and column to delete up-right space (row, column): ")
      row, col = map(int, input().split(","))
      chomp.delete_space(row, col)
      chomp.print_board()
    
if __name__ == "__main__":
  main()