import random

class Percolation:

  nodes = []
  nodeSize = []

  def __init__(self, nodesLength):
    self.nodes = [[y + (x*nodesLength) for y in range(nodesLength)]                   for x in range(nodesLength)]

  def __repr__(self):
    return "\n".join([str(row) for row in self.nodes])

  def open(self, row, col):
    # Returns nothing
    pass

  def isOpen(self, row, col):
    # Returns boolean
    pass

  def numberOfOpenSites(self):
    # Returns int
    pass

  def percolates(self):
    # Returns boolean
    pass


p = Percolation(5)
