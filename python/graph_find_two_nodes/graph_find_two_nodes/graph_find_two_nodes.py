# From Cracking the Coding Interview 4.1
# Given a directed graph and two nodes (s and e), disn an algorithm to find out whether there is a route from s to e

class Node:
    def __init__(self, name):
        self.name = name
        self.children = []
        self.visited = False

    def addChild(self, child):
        self.children.append(child)

    def visit(self):
        self.visited = True

def checkNode(s, e):
    s.visit()
    visited = False
    for i in s.children:
        if i == e:
            return True
        elif not i.visited:
            visited = checkNode(i, e)
            if visited:
                break

    return visited


s = Node("s")
m1 = Node("m1")
e = Node("e")
m2 = Node("m2")
m3 = Node("m3")

s.addChild(m1)
m1.addChild(m2)
m1.addChild(m3)
m2.addChild(e)

print(checkNode(s, e))



