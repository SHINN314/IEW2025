class Chomp():
  """
  Chomp game class.
  Board index starts from (0, 0) at the top left corner.
  
  Attributes
  ----------
  row : int
      Number of rows in the board, not max row index.
  col : int
      Number of columns in the board, not max col index.
  board : list
      The game board represented as a 2D list.
      If the space element is 1, it means the space is not deleted.
      If the space element is 0, it means the space is deleted.
      If the space element is 2, it means the space is poison chocolate.
  is_finished : bool
      Flag to indicate if the game is finished.
  next_player : object
      A player who operate next.
  prev_player : object
      A player who operate prev.
  """
  def __init__(self, row: int, col: int, next_player: object, prev_player: object):
    self.row = row
    self.col = col
    self.next_player = next_player
    self.prev_player = prev_player
    self.board = [[1 for _ in range(self.col)] for _ in range(self.row)] # initialize board with 1
    self.board[self.row-1][0] = 2 # set poison chocolate
    self.is_finished = False

  def swap_prev_next(self):
    """
    A function that swap next_player and prev_player.

    Parameters
    -------
    prev_player : object
        A player who prev_player before call this function.
    next_player : object
        A player who next_player before call this function.
    """

    print("swap prev and next player")
    tmp_player = self.prev_player
    self.prev_player = self.next_player
    self.next_player = tmp_player

  def print_board(self):
    """
    Print the current state of the board.
    """
    for i in range(self.row):
      for j in range(self.row):
        if self.board[i][j] == 1:
          print("■", end=" ")
        elif self.board[i][j] == 2:
          print("□", end=" ")
        else:
          print(" ", end=" ")
      print()
    print()

  def get_board(self) -> list:
    """
    Get the current state of the board.
    
    Returns
    -------
    list
        The current state of the board.
    """
    return self.board

  def check_game_over(self) -> bool:
    """
    Check if the game is over.
    
    Returns
    -------
    bool
        True if the game is over, False otherwise.
    """
    if (
      self.board[self.row-2][0] == 0 and
      self.board[self.row-2][1] == 0 and
      self.board[self.row-1][1] == 0
    ):
      self.is_finished = True
      return True

  def delete_space(self, row: int, col: int):
    """
    Delete the space from the board.
    After delete space, this method switch next_player and prev_player.
    
    Parameters
    ----------
    row : int
        The row index of the space to delete.
    col : int
        The column index of the space to delete.
    """
    if (row < 0 or row >= self.row or col < 0 or col >= self.row):
      # call warning if player select a space which is out of board
      print("Invalid move")
      return
    
    elif (self.board[row][col] == 0):
      # call warning if player select a space which is deleted
      print("This space is already deleted")
      return
    
    elif (self.board[row][col] == 2):
      # call warning if player select a poison space
      print("Choose another space")
      return
    
    else:
      # delete spaces
      print("delete space")
      for i in range(0, row+1):
        for j in range(col, self.col):
          self.board[i][j] = 0

      self.print_board()

      if (self.check_game_over()):
        print(f'{self.next_player} win!')
      else:
        self.swap_prev_next()
