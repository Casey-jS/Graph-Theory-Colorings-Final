import copy

# Final course project for CIS325
# (Discreet Mathematics - Graph Theory)


# param1: graph (dict) : graph
# param2: colors (dict) : the labeling of the vertices
# return: (bool) : true if the graph is proper
def is_proper(graph, colors):
    for vertex in graph:
        for neighbor in graph[vertex]:
            if colors[vertex] == colors[neighbor]:
                return False
    return True 

# Outputs all possible vertex colorings
# using at most 3 colors
# param: graph (dict) : graph
# return: (list[dict]) : all possible vertex colorings using at most 3 colors
def three_color(graph):

    num_vertices = len(graph)
    coloring = []

    # recursively returns list of all color permutations
    def list_perms(length, colors=[]):
        if length == 0: return colors
        else:
            length -= 1
            return list_perms(length, [1] + colors) + list_perms(length, [2] + colors) + list_perms(length, [3] + colors)

    # list of all vertices
    vertices = []
    for v in graph: vertices.append(v)

    # list of all color permutations
    colors = list_perms(num_vertices)
    
    # separates list into list of lists
    def get_sublists(lst):
        for i in range(0, len(lst), num_vertices):
            yield lst[i:i + num_vertices]

    colors = get_sublists(colors)

    for lst in colors:
        d = {}
        # assign a color to each vertex
        i = 0
        for color in lst:
            d[vertices[i]] = color
            i += 1
    
        dcopy = copy.deepcopy(d)
        coloring.append(dcopy)

    return coloring

# Param: graph (dict) : graph
# return: (bool) : true if the graph is 3-colorable
def is_three_color(graph):
    if len(graph) < 4: return True
    
    def greedy(graph, order):
        coloring = {}
        for vertex in order: coloring[vertex] = 0 # initialize all colors to 0

        def color(neighbors):
            colors = []
            for neighbor in neighbors: colors.append(coloring[neighbor])

            for color in range(1, len(graph)):
                if color not in colors: return color
            return max(c for c in colors) + 1

        for vertex in order: coloring[vertex] = color(graph[vertex])
        return coloring

    vertices = []

    for vertex in graph:
        vertices.append(vertex)
    coloring = greedy(graph, vertices)

    for vertex in coloring:
        if coloring[vertex] > 3:
            return False
    return True

# param: graph (dict) : weighted graph
# return: (bool) : true if the graph is a proper edge coloring
def is_proper_edge(graph):

    edge_colors = [] # list of lists

    for vertex in graph:
        colors = []
        for neighbor_list in graph[vertex]: 
            colors.append(neighbor_list[1]) # add color to colors list
        edge_colors.append(colors) # add list to list of lists
        
    for colors in edge_colors:
        if len(colors) != len(set(colors)): # check for duplicates in each sublist
            return False
    return True

# param1: graph (dict) : graph
# param2: order (list[str]) : ordering of the vertices
# return: (dict) : returns the coloring obtained from the greedy algorithm
def greedy(graph, order):
    coloring = {}

    for vertex in order: coloring[vertex] = 0 # initialize all colors to 0

    def color(neighbors):
        colors = []
        for neighbor in neighbors: colors.append(coloring[neighbor])

        for color in range(1, len(graph)):
            if color not in colors: return color
        return max(c for c in colors) + 1

    for vertex in order: coloring[vertex] = color(graph[vertex])
    return coloring
