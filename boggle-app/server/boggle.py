import numpy as np
import string
import nltk

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
       
        # TODO This needs to be recursive and probably use a tree-based solution
        # instead of lists to simplify traversal
        # Currently, this only gets into the adj list for each primary value
        for key, val in adjLists.items(): # all the dictionaries
            for k, v in val.items():    # each dictionary
                print('Dictionary Key ' + str(k))
                for i in v: # each adjacent
                    print('Adjacent Value ' + str(i))
                    #found = tree_traverse(adjLists, i) // not implemented see TODO
                    #print("found" + str(found))

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
        # just returning something for now so I can pass them to the front end
        return ['solution1', 'solution2', 'solution3']

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
    adjList = board.AdjacencyMatrix(currentBoard)

    solutions = board.solver(adjList)
    '''
    