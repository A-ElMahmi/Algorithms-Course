import random

class Percolation:

  nodes = []
  nodeSize = []

  def __init__(self, nodesLength):
    if nodesLength <= 0:
      raise ValueError
    self.nodes = [[0 for y in range(nodesLength)] for x in range(nodesLength)]

  def __repr__(self):
    return "\n".join([str(row) for row in self.nodes])

  def union(self, p, q):
    print("Successful union of:", p, q)

  def open(self, row, col):
    if self.isOpen(row, col):
      return

    if row > 0 and self.nodes[row-1][col] != 0:
        self.union((row-1, col), (row, col))
    elif row < len(self.nodes)-1 and self.nodes[row+1][col] != 0:
        self.union((row+1, col), (row, col))
    elif col > 0 and self.nodes[row][col-1] != 0:
        self.union((row, col-1), (row, col))
    elif col < len(self.nodes)-1 and self.nodes[row][col+1] != 0:
        self.union((row, col+1), (row, col))
    else:
      self.nodes[row][col] = (row*len(self.nodes)) + col + 1

  def isOpen(self, row, col):
    return self.nodes[row][col] != 0

  def numberOfOpenSites(self):
    return sum([len(row)-row.count(0) for row in self.nodes])

  def percolates(self):
    # Returns boolean
    pass


p = Percolation(4)
