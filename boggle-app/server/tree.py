class Node:
    def __init__(self, value, parent=None):
        self.value = value
        self.children = []
        self.endsWord = False
 
    def __repr__(self):
        return str(self)
 
    def __str__(self):
        return str(self.value)
 
    def __iter__(self):
        yield self.value
        yield from self.children
 
class Tree:
    def __init__(self):
       self.root = Node('$')
       self.parent = None 
 
    def addNode(self, value, parent=None):
        node = Node(value)

        if parent is None:
            node.parent = self.root
            self.root.children.append(node)
        else: 
            node.parent = parent
            parent.children.append(node)
        return node

    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)
 
    def __repr__(self):
        return str(self)
 
    '''
    Traverses tree from current node and returns
    all possible paths
    '''
    def traverse(self, currentNode, pathList=[]):
        pathList.append(currentNode)
        if len(currentNode.children) == 0:
            yield pathList
        else:
            for child in currentNode.children:
                yield from self.traverse(child, pathList)
                pathList.pop()
