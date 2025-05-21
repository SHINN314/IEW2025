from chomp import chomp

chomp_game = chomp(3, 3)
chomp_game.print_board()
chomp_game.delete_space(1, 1)
chomp_game.delete_space(0, 0)
chomp_game.delete_space(1, 0)
chomp_game.delete_space(2, 1)