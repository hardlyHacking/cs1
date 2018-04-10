# bfs.py
# Emily Freebairn
# November 17, 2011
# Minor changes by THC.
# Runs breadth-first-search using the Vertex class.

from collections import deque

# Run bfs and find the path from the Vertex start to the Vertex goal.
# Return that path as a list of Vertex objects.  If there is no path, return None.
def bfs(start, goal):
    frontier = deque()      # the queue of vertices we're going to visit next
    frontier.append(start)  # put the start vertex in our list of those to visit
    
    back_pointer = {}
    back_pointer[start] = None   # the start vertex has no back_pointer
    
    # Keep going while there's at least one visited vertex that we have not
    # explored from yet.
    while len(frontier) > 0: 
        vertex = frontier.popleft()
        
        if vertex == goal: 
            # If we're done, retrace the path from the goal to the start.
            path = []        
            while vertex != None: # only our start should have a None back_pointer along our path
                path.append(vertex)
                vertex = back_pointer[vertex]
            return path
        
        else:   # keep exploring
            for neighbor in vertex.adjacent:
                # Visit the vertex only if it hasn't been visited yet.  It has been
                # visited if and only if it has a back_pointer.
                if not neighbor in back_pointer:
                    # Set up the back_pointer.  This will only happen once for each vertex, 
                    # since a vertex is put in the frontier and visited only once.
                    back_pointer[neighbor] = vertex
                    frontier.append(neighbor)
                    
    # If we get here, we've run out of vertices to explore before reaching the goal.
    return None