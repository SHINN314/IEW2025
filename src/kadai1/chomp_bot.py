from chomp import Chomp 

class SquareChompBot:
  """
  A bot which optimized for square chomp board.
  This class is usefull if this bot is a first player of the geme.
  """
  def __init__(self):
    pass

  @staticmethod
  def is_symmetric_board(chomp: Chomp) -> bool:
    """
    Check current board is symmetrical.
    If given board is symmetric, it mean that the board is square board.

    Parameters
    -------
    chomp : Chomp
        Chomp instance which have current board information.

    Returns
    -------
    bool
    """
    board = chomp.board
    transposed_board = [list(x) for x in zip(*board)]

    if board == transposed_board:
      return True
    
    return False

  def delete_space(self, chomp: Chomp):
    """
    Set the space on the board.
    
    Parameters
    ----------
    chomp : Chomp
        The chomp object.
    row : int
        The row index of the space to set.
    col : int
        The column index of the space to set.
    """
    if self.is_symmetric_board(chomp):
      # case square board
      row_space = chomp.row-2
      col_space = 1
      chomp.delete_space(row=row_space, col=col_space)

    else:
      # case unsymmetrical l board
      row_space = chomp.row-1
      col_space = 0
      board = chomp.board

      for i in range(0, chomp.row):
        if board[chomp.row-1-i][0] > board[chomp.row-1][i]:
          # case if vertical edge is longer than horizon edge
          chomp.delete_space(row=row_space, col=0)
          break

        elif board[chomp.row-1][i] > board[chomp.row-1-i][0]: 
          # case if horizon edge is longer than vertical edge
          chomp.delete_space(row=chomp.row-1, col=col_space)
          break

        else:
          # update row_space and col_space
          row_space += 1
          col_space += 1
    