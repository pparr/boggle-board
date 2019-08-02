import numpy as np
import string
import nltk
from tree import Tree, Node

class Board(object):

    def __init__(self, boardSize=4):
        letterSet = list(string.ascii_uppercase.replace('Q', ''))
        letterSet.append('QU')
        letterSet.sort()  
        self.letterSet = letterSet
        self.boardSize = boardSize
        self.currentLetters = None
        self.adjacencies = None

         # set up the path to the dictionary for the corpus
        nltk.data.path.append('./words/')

    '''
    Returns a psuedo random board with replacement
    '''
    def getRandomBoard(self):
        
        board = np.random.choice(self.letterSet, self.boardSize * self.boardSize, replace=True)
        self.currentLetters = board
        print('CURRENT LETTERS ' + str(board))

        board.resize((self.boardSize, self.boardSize))
        self.currentLetters = board 
        return board

    def solver(self, adjLists):
        solutions = []
        
        # Get the set of all words in the corpus. Set is more performant than list here.
        corpus = set(w.lower() for w in nltk.corpus.words.words())
        
        # load words into tree. Don't load anything shorter than 3 or longer than 
        # current letter set plus 1(ie 4x4 board would be 16 characters w/o QU or 17 with)
        #  max because we can only visit that letter once)
        tree = Tree()
        for w in corpus:
            if len(w) < 3:
                continue
            if len(w) > (self.boardSize * self.boardSize) + 1:
                continue
            first = Node(w[0])
            subsequent = w[1:]
            parent = tree.addNode(first)
            last = None
            for c in subsequent:
                child = tree.addNode(Node(c), parent)
                parent = child
                last = child
            # mark the end of a word for later
            if last is not None:
                last.endsWord = True

        # walk the word tree with the letters on the board, 
        # building up strings by adjacencies. 
        visited = []
        sols = []
        #pos in self.currentLetters: # board in order
        
        # Not working yet.
        '''
        for idx, val in np.ndenumerate(self.currentLetters):
            #idx position
            #val letter
            self.findStrings(idx, tree.root.children[0], visited)
        '''
         # just returning something for now so I can pass them to the front end
        return ['solution1', 'solution2', 'solution3']

    '''
    Not functional yet, but the idea is to walk the tree that contains
    the loaded corpus, comparing it to the patterns of strings we
    have available on the board. If we find a match, add it to solutions
    '''
    def findStrings(self, idx, currentPosition, visited):
        if currentPosition.endsWord:
            sol.append(visited)
        for pos, adjs in self.adjacencies['adjacencies'][idx].items():
            # adjs is the list of positions
            for adj in adjs:
                if adj not in visited:
                    nextnode = None
                    currentLetter = self.currentLetters[adj]
                    if currentLetter in currentPosition.children:
                        nextnode = currentPosition.children.index(currentLetter)
                    # account for QU
                    if currentLetter == 'Q':
                        nextnode = currentPosition.children.index('U')
                        if not nextnode:
                            return
                    if nextnode is None:
                        return
                    self.findStrings(adj, nextnode, visited.append(currentLetter))

        '''
        parent = None
        for key, val in adjLists.items(): # all the dictionaries
            for k, v in val.items():    # each dictionary
                current = tree.addNode(self.currentLetters[k], parent)
                parent = current
                for i in v: # each adjacent position
                    adj = tree.addNode(self.currentLetters[i], parent)
        for p in tree.traverse(tree.root):
            print(p)
        '''
        '''
            # simple example of finding words with corpus
            #newWord = {'foo', 'fool', 'foolh', 'foolha', 'foolhar', 'foolhard', 'foolhardy'}
            #found = corpus.intersection(newWord)

            #test startswith for finding partial matches as a means of 
            # stopping earlier if no matches in corpus 
            #found = list(w.startswith('add') for w in corpus)
            #if True in found:
            #    print("found")
        '''

    '''
    Builds up a dictionary of dictionaries of adjacencies for all positions on the board
    '''
    def AdjacencyMatrix(self):
        board = np.full((self.boardSize, self.boardSize), False, dtype=bool)
        
        adjList = {'adjacencies': {}}
        for idx, value in np.ndenumerate(board):
            adjList['adjacencies'][idx] = (self.getAdj(idx[0], idx[1]))
            
        print(adjList)
        self.adjacencies = adjList
        return adjList

    
    '''
    Gets adjacent positions in all legal directions
    '''
    def getAdj(self, row, col):
        adj = []
        adjDict = {}
        rowAbove = row - 1
        rowBelow = row + 1
        colLeft = col - 1
        colRight = col + 1
        if row > 0:
            adj.append((rowAbove, col))
            if col > 0:
                adj.append((rowAbove, colLeft))
            if col + 1 < self.boardSize:
                adj.append((rowAbove, colRight))
        if row + 1 < self.boardSize:
            adj.append((rowBelow, col))
            if col > 0:
                adj.append((rowBelow, colLeft))
            if col + 1 < self.boardSize:
                adj.append((rowBelow, colRight))
        if col > 0:
            adj.append((row, colLeft))
        if col + 1 < self.boardSize:
            adj.append((row, colRight))
        #return adj
        adjDict[(row, col)] = adj
        return adjDict

if __name__=="__main__":
    pass 
    '''
    board = Board()
    currentBoard = board.getRandomBoard()
    adjList = board.AdjacencyMatrix()
    solutions = board.solver(adjList)
    '''
    
    