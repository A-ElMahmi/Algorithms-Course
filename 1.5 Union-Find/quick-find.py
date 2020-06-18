class QuickFind:

  points = []

  def __init__(self, totalElements):
    for i in range(totalElements):
      self.points.append(i)

  def union(self, p, q):
    if self.points[p] == self.points[q]:
      return

    for i in self.points:
      if i == self.points[q]:
        self.points = 1





