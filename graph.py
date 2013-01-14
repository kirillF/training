# 6.00 Problem Set 10
# Graph optimization
#
# A set of data structures to represent graphs
#

class Node(object):
    def __init__(self, name):
        self.name = str(name)
    def getName(self):
        return self.name
    def __str__(self):
        return self.name
    def __repr__(self):
        return self.name
    def __eq__(self, other):
        return self.name == other.name
    def __ne__(self, other):
        return not self.__eq__(other)

class Edge(object):
    def __init__(self, src, dest):
        self.src = src
        self.dest = dest
    def getSource(self):
        return self.src
    def getDestination(self):
        return self.dest
    def __str__(self):
        return '%s->%s' % (str(self.src), str(self.dest))

class Digraph(object):
    """
    A directed graph
    """
    def __init__(self):
        self.nodes = set([])
        self.edges = {}
    def addNode(self, node):
        if node in self.nodes:
            raise ValueError('Duplicate node')
        else:
            self.nodes.add(node)
            self.edges[node] = []
    def addEdge(self, edge):
        src = edge.getSource()
        dest = edge.getDestination()
        if not(src in self.nodes and dest in self.nodes):
            raise ValueError('Node not in graph')
        self.edges[src].append(dest)
    def childrenOf(self, node):
        return self.edges[node]
    def hasNode(self, node):
        return node in self.nodes
    def __str__(self):
        res = ''
        for k in self.edges:
            for d in self.edges[str(k)]:
                res = '%s%s->%s\n' % (res, str(k), str(d))
        return res[:-1]

# class MITGraph - subclass of Digraph
# including weights, that describes distance between buildings and
# distance neede to go outdoors

class MITEdge(Edge):
    def __init__(self, src, dest, dist, out):
        self.dist = dist
        self.out = out
        Edge.__init__(self, src, dest)

    def getDistance(self):
        return self.dist
    def getOutdoor(self):
        return self.out
    def __str__(self):
        return "%s->(%s, %s)%s" %( str(self.src), str(self.dist), str(self.out), str(self.dest))

class MITGraph(Digraph):
    """
    A directed graph represrnting MIT Campus
    """
    def __init__(self):
        Digraph.__init__(self)
        
    def addEdge(self, edge):
        src = edge.getSource()
        dst = edge.getDestination()
        if not(src in self.nodes and dst in self.nodes):
            raise ValueError('Node not in graph')
        self.edges[src].append([dst,edge.getDistance(),edge.getOutdoor()])

    def childrenOf(self, node):
        return self.edges[str(node)]

    def __str__(self):
        res = ''
        for k in self.edges:
            for d in self.edges[str(k)]:
                res = '%s%s->(%d,%d)%s\n' % (res, str(k), d[1], d[2], str(d[0]))
        return res[:-1]
