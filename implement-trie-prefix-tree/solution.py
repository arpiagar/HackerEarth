#https://leetcode.com/problems/implement-trie-prefix-tree/

class Node:
    def __init__(self,val,endNode=False, childMap=None ):
        self.val = val
        if childMap:
            self.childMap = childMap
        else:
            self.childMap = {}
        self.endNode = endNode

class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie_map = {}


    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: None
        """
        self.insertWithMap(word, self.trie_map) # apple

    def insertWithMap(self, word, node_map): #
        if not word: # {}
            return
        endNode = False
        if len(word) == 1:
            endNode = True
        firstElem = word[0]  # a
        if firstElem not in node_map:
            obj = Node(firstElem,endNode)  # {a: Node(a)}
            node_map[firstElem] = obj
            self.insertWithMap(word[1:], obj.childMap) #  a -> {p -> {p} -> {l} -> {e}}
        else:
            next_node_map = node_map[firstElem].childMap
            if endNode:
                node_map[firstElem].endNode = True
            self.insertWithMap(word[1:], next_node_map)
        return




    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        if not word: #
            return False
        firstElem = word[0] # a
        if firstElem not in self.trie_map:
            return False
        startNode = self.trie_map[firstElem] #a
        for i in range(1, len(word)): # pple
            elem = word[i] # p
            if elem not in startNode.childMap: #
                return False
            startNode = startNode.childMap[elem]
        if startNode.endNode:
            return True
        return False



    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        word = prefix
        if not word:
            return True
        firstElem = word[0]
        if firstElem not in self.trie_map:
            return False
        startNode = self.trie_map[firstElem]
        for i in range(1, len(word)):
            elem = word[i]
            if elem not in startNode.childMap:
                return False
            startNode = startNode.childMap[elem]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
