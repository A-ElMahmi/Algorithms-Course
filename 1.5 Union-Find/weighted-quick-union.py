class WeightedQuickUnion:

  nodes = []
  size = []

  def __init__(self, totalElements):
    for i in range(totalElements):
      self.nodes.append(i)
      self.size.append(1)
  
  def __repr__(self):
    return "QuickUnion{}".format(tuple(self.nodes))

  def findRoot(self, i):
    while i != self.nodes[i]:
      self.nodes[i] = self.nodes[self.nodes[i]] 
      i = self.nodes[i]
    return i
  
  def union(self, p, q):
    if self.connected(p, q): return
    
    p, q = self.findRoot(p), self.findRoot(q)
    if self.size[p] > self.size[q]:
      self.nodes[q] = p
      self.size[p] += self.size[q]
    else:
      self.nodes[p] = q
      self.size[q] += self.size[p]

  def connected(self, p, q):
    return self.findRoot(p) == self.findRoot(q)
      

with open("mediumUF.txt", "r") as f:
  data = f.read().split("\n")
  links = [tuple(i.split(" ")) for i in data[1:-1]]
  
qu = WeightedQuickUnion(int(data[0]))
for p, q in links:
  qu.union(int(p), int(q))
