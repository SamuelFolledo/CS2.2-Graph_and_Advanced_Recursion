

# MODULE 1 - Edge List
''' 
CONCEPTUAL QUESTIONS
# 1. What are the two main components of a graph?
• Vertex (node)
• Edge (connection - directed or undirected)
# 2. What are two different types of graphs and what makes them unique?
• Connected which has a path between every pair of vertices meawhile Disconnected graph has some unreachable vertices. 
'''

def create_edge_list(locations):
  '''
  Takes in a list of locations and 
  outputs an edge list in the form 
  [[from, to], [from, to]]
  '''
  edge_list = []
  for location in locations:
    cleaned_location = location.replace('\n', '')
    edge_list.append(cleaned_location.split(', '))
  return edge_list

lines = ["Dawnstar, Falkreath", "Dawnstar, Markarth", "Markarth, Morthal", 
        "Morthal, Dawnstar", "Riften, Solitude", "Solitude, Morthal", 
        "Solitude, Markarth", "Solitude, Dawnstar", "Solitude, Falkreath", 
        "Falkreath, Whiterun", "Whiterun, Windhelm"]
print("Edge list:", create_edge_list(lines))


