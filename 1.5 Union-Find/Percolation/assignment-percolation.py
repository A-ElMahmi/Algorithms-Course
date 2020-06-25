import random, copy

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

  def __call__(self):
    while not self.percolates():
      print("\n", str(self), sep="")
      while True:
        randX, randY = random.randint(0, len(self.nodes)-1), random.randint(0, len(self.nodes)-1)
        if not self.isOpen(randX, randY):
          break
      self.open(randX, randY)
    print("\n", str(self), sep="")

  def union(self, grid, p, q):
    if self.connected(grid, p, q): return

    p, q = self.findRoot(grid, *p), self.findRoot(grid, *q)
    if self.nodeSize[p[0]][p[1]] > self.nodeSize[q[0]][q[1]]:
      grid[q[0]][q[1]] = p
      self.nodeSize[p[0]][p[1]] += self.nodeSize[q[0]][q[1]]
    else:
      grid[p[0]][p[1]] = q
      self.nodeSize[q[0]][q[1]] += self.nodeSize[p[0]][p[1]]

  def connected(self, grid, p, q):
    return self.findRoot(grid, *p) == self.findRoot(grid, *q)
  
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

    self.nodes[row][col] = (row, col)
    if row > 0 and self.nodes[row-1][col] != 0:
        self.union(self.nodes, (row-1, col), (row, col))
    if row < len(self.nodes)-1 and self.nodes[row+1][col] != 0:
        self.union(self.nodes, (row+1, col), (row, col))
    if col > 0 and self.nodes[row][col-1] != 0:
        self.union(self.nodes, (row, col-1), (row, col))
    if col < len(self.nodes)-1 and self.nodes[row][col+1] != 0:
        self.union(self.nodes, (row, col+1), (row, col))
    
    
  def isOpen(self, row, col):
    return self.nodes[row][col] != 0

  def numberOfOpenSites(self):
    return sum([len(row)-row.count(0) for row in self.nodes])

  def percolates(self):
    nodesCopy = copy.deepcopy(self.nodes)
    for row in (0, len(nodesCopy)-1):
      for col, val in enumerate(nodesCopy[row]):
        if val == 0:
          nodesCopy[row][col] = (row, col)
    
    for row in (0, len(nodesCopy)-1):
      for col, _ in enumerate(nodesCopy[row][:-1]):
        self.union(nodesCopy, (row, col), (row, col+1))

    return self.connected(nodesCopy, (0, 0), (len(nodesCopy)-1, 0))
      


if __name__ == "__main__":
  p = Percolation(5)
  p()