# 6.00.2x Problem Set 5
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
    def __hash__(self):
        # Override the default hash method
        # Think: Why would we want to do this?
        return self.name.__hash__()

class Edge(object):
    def __init__(self, src, dest):
        self.src = src
        self.dest = dest
    def getSource(self):
        return self.src
    def getDestination(self):
        return self.dest
    def __str__(self):
        return '{0}->{1}'.format(self.src, self.dest)

class WeightedEdge(Edge):

    def __init__(self, src, dest, total_dist, outdoor_dist):
        Edge.__init__(self, src, dest)
        self.total_dist = total_dist
        self.outdoor_dist = outdoor_dist

    def getTotalDistance(self):
        return self.total_dist

    def getOutdoorDistance(self):
        return self.outdoor_dist

    def __str__(self):
        return '{0}->{1} ({2}, {3})'.format(self.src, self.dest, self.total_dist, self.outdoor_dist)

class Digraph(object):
    """
    A directed graph
    """
    def __init__(self):
        # A Python Set is basically a list that doesn't allow duplicates.
        # Entries into a set must be hashable (where have we seen this before?)
        # Because it is backed by a hashtable, lookups are O(1) as opposed to the O(n) of a list (nifty!)
        # See http://docs.python.org/2/library/stdtypes.html#set-types-set-frozenset
        self.nodes = set([])
        self.edges = {}

    def addNode(self, node):
        if node in self.nodes:
            # Even though self.nodes is a Set, we want to do this to make sure we
            # don't add a duplicate entry for the same node in the self.edges list.
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
                res = '{0}{1}->{2}\n'.format(res, k, d)
        return res[:-1]

class WeightedDigraph(Digraph):

    def __init__(self):
        Digraph.__init__(self)

    def addEdge(self, edge):
        src = edge.getSource()
        dest = edge.getDestination()
        total_dist = float(edge.getTotalDistance())
        autdoor_dist = float(edge.getOutdoorDistance())
        if not(src in self.nodes and dest in self.nodes):
            raise ValueError('Node not in graph')
        self.edges[src].append([dest, (total_dist, autdoor_dist)])

    def childrenOf(self, node):
        return [n[0].getName() for n in self.edges[node]]

    def __str__(self):
        res = ''
        for s in self.edges:
            for d in self.edges[s]:
                res += str(s) + '->' + str(d[0]) + ' (' + str(d[1][0]) + ', ' + str(d[1][1]) + ')\n'
        return res[:-1]

    def distEdges(self, edge):
        # [[j, (51.0, 17.0)], [m, (79.0, 63.0)]]
        for e in self.edges[Node(edge[0])]:
            if e[0] == Node(edge[1]):
                return e[1][0]
        return False

    def outEdges(self, edge):
        # [[j, (51.0, 17.0)], [m, (79.0, 63.0)]]
        for e in self.edges[Node(edge[0])]:
            if e[0] == Node(edge[1]):
                return e[1][1]
        return False

# h = Node('h')
# j = Node('j')
# k = Node('k')
# m = Node('m')
# ag = Node('g')
# g = WeightedDigraph()
# g.addNode(h)
# g.addNode(j)
# g.addNode(k)
# g.addNode(m)
# g.addNode(ag)
# randomEdge = WeightedEdge(h, j, 51, 17)
# g.addEdge(randomEdge)
# randomEdge = WeightedEdge(k, m, 12, 11)
# g.addEdge(randomEdge)
# randomEdge = WeightedEdge(j, k, 65, 57)
# g.addEdge(randomEdge)
# randomEdge = WeightedEdge(k, j, 54, 6)
# g.addEdge(randomEdge)
# randomEdge = WeightedEdge(h, m, 79, 63)
# g.addEdge(randomEdge)
# randomEdge = WeightedEdge(j, k, 58, 17)
# g.addEdge(randomEdge)
# randomEdge = WeightedEdge(m, j, 93, 80)
# g.addEdge(randomEdge)
# randomEdge = WeightedEdge(k, h, 17, 14)
# g.addEdge(randomEdge)
# print g.childrenOf(h)#: [j, m]
# print g.childrenOf(j)#: [k, k]
# print g.childrenOf(k)#: [m, j, h]
# print g.childrenOf(m)#: [j]
# print g.childrenOf(ag)#: []
# print g.__dict__
# print g.distEdges([h, m])
# print g.outEdges([h, m])