from chomp import Chomp 

class ChompBot:
  """
  This class is a bot for chomp.

  Attributes
  ----------
  board : list
      The current state of the board.
  """
  def __init__(self):
    pass

  def delete_space(Chomp: Chomp, row: int, col: int):
    """
    Set the space on the board.
    
    Parameters
    ----------
    Chomp : Chomp
        The chomp object.
    row : int
        The row index of the space to set.
    col : int
        The column index of the space to set.
    """
    Chomp.delete_space(row, col)
    