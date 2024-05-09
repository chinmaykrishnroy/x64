class Graph:
  def __init__(self, vertices):
    self.V = vertices
    self.graph = [[] for _ in range(vertices)]

  def add_edge(self, u, v):
    self.graph[u].append(v)
    self.graph[v].append(u)
  
  def is_safe(self, v, c, color):
   for i in self.graph[v]:
     if color[i] == c:
       return False
     else:
      return True 
     
  def graph_color_util(self, m, color, v):
    if v == self.V:
      return True
    for c in range(1, m+1):
      if self.is_safe(v, c, color):
        color[v] = c
        if self.graph_color_util(m, color, v+1):
          return True
        color[v] = 0
    return False
  
  def graph_color(self, m):
    color = [0] * self.V
    if not self.graph_color_util(m, color, 0):
      print("Solution does not exist")
      return False
    for i in range(self.V):
      print("Vertex" , i , ":", "Color" , color[i])
    return True
  
g = Graph(5)
g.add_edge(0,1)
g.add_edge(0,2)
g.add_edge(1,2)
g.add_edge(1,3)
g.add_edge(2,3)
g.add_edge(3,4)
g.graph_color(3)