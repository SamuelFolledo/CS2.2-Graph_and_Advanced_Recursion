

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


# MODULE 2 - Adjacency List
def create_adjacency_list(locations):
  '''Returns a dictionary adjacency list of edges'''
  adjacency_list = {}
  for location in locations:
    cleaned_location = location.replace('\n', '')
    location_pair = cleaned_location.split(', ')
    start = location_pair[0]
    end = location_pair[1]
    if start in adjacency_list:
      adjacency_list[start].append(end)
    else:
      adjacency_list[start] = [end]
  return adjacency_list

adjacency_list = create_adjacency_list(lines)

def is_there_a_path(adjacency_list, location_start, location_end):
  '''Uses a traversal algorithm to check if a path exists from 
  location start to location end, returns True if a path exists, 
  False if not'''
  if location_end in adjacency_list[location_start]:
    return True
  return False

print("Adjacency list:", adjacency_list)
# print(is_there_a_path(adjacency_list, "Dawnstar", "Markarth"))

