class QuickUnion:

  nodes = []

  def __init__(self, totalElements):
    for i in range(totalElements):
      self.nodes.append(i)
  
  def __repr__(self):
    return "QuickUnion{}".format(tuple(self.nodes))

  # My implementation
  # def findRoot(self, i):
  #   for _ in self.nodes:
  #     root = self.nodes[self.nodes[i]]
  #     if self.nodes.index(root) == root: 
  #       break
  #   return root

  # Courses implementation
  def findRoot(self, i):
    while i != self.nodes[i]:
      i = self.nodes[i]
    return i
  
  def union(self, p, q):
    if self.connected(p, q): return
    self.nodes[q] = self.findRoot(p)

  def connected(self, p, q):
    return self.findRoot(p) == self.findRoot(q)
      

with open("tinyUF.txt", "r") as f:
  data = f.read().split("\n")
  links = [tuple(i.split(" ")) for i in data[1:-1]]
  
qu = QuickUnion(int(data[0]))
for p, q in links:
  qu.union(int(p), int(q))