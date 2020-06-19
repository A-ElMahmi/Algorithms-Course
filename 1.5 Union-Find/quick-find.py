class QuickFind:

  points = []

  def __init__(self, totalElements):
    for i in range(totalElements):
      self.points.append(i)

  def __repr__(self):
    return "QuickFind{}".format(tuple(self.points))

  def union(self, p, q):
    if self.points[p] == self.points[q]: return
    for i, j in enumerate(self.points):
      if j == self.points[q]:
        self.points[i] = self.points[p]

  def connected(self, p, q):
    return self.points[p] == self.points[q]


with open("tinyUF.txt", "r") as f:
  data = f.read().split("\n")
  links = [tuple(i.split(" ")) for i in data[1:-1]]
  
qf = QuickFind(int(data[0]))
for p, q in links:
  qf.union(int(p), int(q))