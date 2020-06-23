import random

class Percolation:

  nodes = []
  nodeSize = []

  def __init__(self, nodesLength):
    if nodesLength <= 0:
      raise ValueError
    self.nodes = [[0 for y in range(nodesLength)] for x in range(nodesLength)]
    self.nodeSize = [[1 for y in range(nodesLength)] for x in range(nodesLength)]

  def __repr__(self):
    return "\n".join([str(row) for row in self.nodes])

  def __str__(self):
    return "\n".join([" ".join(["0" if col == 0 else "1" for col in row]) for row in self.nodes])

  def run(self):
    while self.percolates():
      print("\n", repr(self), sep="")
      while True:
        randX, randY = random.randint(0, 3), random.randint(0, 3)
        if not self.isOpen(randX, randY):
          break
      self.open(randX, randY)

  def union(self, p, q):
    if self.connected(self.nodes, p, q): return

    p, q = self.findRoot(self.nodes, *p), self.findRoot(self.nodes, *q)
    if self.nodeSize[p[0]][p[1]] > self.nodeSize[q[0]][q[1]]:
      self.nodes[q[0]][q[1]] = p
      self.nodeSize[p[0]][p[1]] += self.nodeSize[q[0]][q[1]]
    else:
      self.nodes[p[0]][p[1]] = q
      self.nodeSize[q[0]][q[1]] += self.nodeSize[p[0]][p[1]]

  def connected(self, grid, p, q):
    return self.findRoot(self.nodes, *p) == self.findRoot(self.nodes, *q)
  
  def findRoot(self, grid, row, col):
    if grid[row][col] == 0:
      return
      
    while (row, col) != grid[row][col]:
      grid[row][col] = grid[grid[row][col][0]][grid[row][col][1]]
      row, col = grid[row][col]
    return row, col
  
  def open(self, row, col):
    if self.isOpen(row, col):
      return

    noOpenSites = True
    if row > 0 and self.nodes[row-1][col] != 0:
        self.nodes[row][col] = (row, col)
        self.union((row-1, col), (row, col))
        noOpenSites = False
    if row < len(self.nodes)-1 and self.nodes[row+1][col] != 0:
        self.nodes[row][col] = (row, col)
        self.union((row+1, col), (row, col))
        noOpenSites = False
    if col > 0 and self.nodes[row][col-1] != 0:
        self.nodes[row][col] = (row, col)
        self.union((row, col-1), (row, col))
        noOpenSites = False
    if col < len(self.nodes)-1 and self.nodes[row][col+1] != 0:
        self.nodes[row][col] = (row, col)
        self.union((row, col+1), (row, col))
        noOpenSites = False
    
    if noOpenSites:
      self.nodes[row][col] = (row, col)

  def isOpen(self, row, col):
    return self.nodes[row][col] != 0

  def numberOfOpenSites(self):
    return sum([len(row)-row.count(0) for row in self.nodes])

  def percolates(self):
    nodesCopy = self.nodes.copy()
    firstNode, lastNode = (0, 0), (0, len(nodesCopy)-1)
    for i, _ in enumerate(nodesCopy[0]):
      nodesCopy[0][i] = firstNode
    for i, _ in enumerate(nodesCopy[-1]):
      nodesCopy[-1][i] = lastNode

    return self.connected(nodesCopy, firstNode, lastNode)



if __name__ == "__main__":
  p = Percolation(4)
  p.run()
