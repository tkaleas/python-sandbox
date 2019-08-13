#!/usr/bin/python

# Implementation of Kevin Bacon
import queue

## Actor Node

## BaconSearch
class ActorNode(object):
    def __init__(self, name):
        self.name = name
        self.linked = set()
    
    def linkActors(self,otherActor):
        self.linked.add(otherActor.name)
        otherActor.linked.add(self.name)

class BaconGraph(object):
    def __init__(self):
        self.nodes = {}         # List of Dict here?
    
    def createGraph(self, movieDict):
        # Create Actor Graph
        for key in list(movieDict.keys()):
            actors = movieDict[key]
            for actorName1 in actors:
                for actorName2 in actors:
                    if actorName1 != actorName2:
                        if actorName1 not in self.nodes:
                            self.nodes[actorName1] = ActorNode(actorName1)
                        if actorName2 not in self.nodes:
                            self.nodes[actorName2] = ActorNode(actorName2)

                        actorNode1 = self.nodes[actorName1]
                        actorNode2 = self.nodes[actorName2]
                        actorNode1.linkActors(actorNode2)

    def getBaconNumber(self, actorName):
        baconNumberMap = {}

        #initialized bacon numbers to -1
        for key in self.nodes:
            actorNode = g.nodes[key]
            baconNumberMap[actorNode.name] = -1

        q = queue.Queue()
        curActorNode = self.nodes["Kevin Bacon"]
        q.put(curActorNode)

        while(not q.empty()):
            #Pop Node
            node = q.get()
            #Return if Actor Found
            if node.name == actorName:
                return baconNumberMap[actorName] + 1
            # add adjacent nodes to list
            for otherActor in node.linked:
                if  baconNumberMap[otherActor] < 0:
                    baconNumberMap[otherActor] = baconNumberMap[node.name] + 1
                    q.put(self.nodes[otherActor])

        return -1

## Test With a Movie List
movielist = {}
with open("movies.txt") as f:
    for line in f:
        l = line.split()
        movieName = l.pop(0)
        movielist[movieName] =  [ x+' '+y for x,y in zip(l[0::2], l[1::2]) ]

print(movielist)

g = BaconGraph()

g.createGraph(movielist)

for key in g.nodes:
    node = g.nodes[key]
    print(node.name)
    print(node.linked)

print(g.getBaconNumber("Kevin Bacon"))
print(g.getBaconNumber("Tom Hanks"))
print(g.getBaconNumber("Josh Brolin"))
print(g.getBaconNumber("Gary Sinise"))
print(g.getBaconNumber("Demi Moore"))
print(g.getBaconNumber("John Cusack"))
print(g.getBaconNumber("Elisabeth Shue"))
print(g.getBaconNumber("Audrey Tautou"))