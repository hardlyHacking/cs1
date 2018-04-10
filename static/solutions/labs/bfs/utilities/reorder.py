class Neighbor:
    def __init__(self, number, dist):
        self.number = number
        self.dist = dist
        
    def __lt__(self, other):
        return self.dist < other.dist

def load_graph(file_name):
    graph = open(file_name, 'r') # open the file for reading only

    # put lines from file into list for easy access
    lines = []
    for line in graph:
        lines.append(line)
    
    graph.close()
    return lines

def dist_sq(x1, y1, x2, y2):
    dx = x1 - x2
    dy = y1 - y2
    return dx*dx + dy*dy

lines = load_graph("dartmouth_graph.txt")

nodes = []

for line in lines:
    parts = line.split(";")
    number = int(parts[0])
    connect = parts[1].split(",")
    neighbors = []
    for c in connect:
        neighbors.append(int(c.strip()))
    loc = parts[2].split(",")
    location = []
    for l in loc:
        location.append(int(l.strip()))
    nodes.append([neighbors, location])
    
#for node in nodes:
#    print node[0], node[1]

outfile = open("new_graph.txt", "w")

i = 0
for node in nodes:
    adj = []
    for neighbor in node[0]:
        neigh = Neighbor(neighbor, dist_sq(node[1][0], node[1][1],
                                       nodes[neighbor][1][0], nodes[neighbor][1][1]))
        adj.append(neigh)
        
    adj.sort()
    
    outfile.write(str(i) + ";")
    for j in range(len(adj)):
        outfile.write(" " + str(adj[j].number))
        if j < len(adj) - 1:
            outfile.write(",")
        else:
            outfile.write("; ")
    outfile.write(str(node[1][0]) + ", " + str(node[1][1]) + "\n")
#    print str(i) + ":",
#    for neighbor in adj:
#        print neighbor.number, neighbor.dist,
#        print ","
#    print ""
    i += 1
    
outfile.close()

