class Node(object):
    def __init__(self, value):
        self.value = value
        self.children = {}
        self.terminal = False
    
    def add_child(self, value):
        if value not in self.children:
            self.children[value] = Node(value)
    
    def get_child(self, val):
        return self.children[val]
        
    def __contains__(self, obj):
        if isinstance(obj, Node):
            return obj.value in self.children
        if isinstance(obj, basestring):
            return obj in self.children
        return False
        
    def __eq__(self, other):
        if not isinstance(other, Node):
            return False
        return other.value == self.value
    
    def __hash__(self):
        return hash(self.value)
    
    def __repr__(self):
        return "Node(" + self.value + ")"

    def __str__(self, level=1):
        return "\n".join([self.value or '-'] + [" "*level + n.__str__(level=level+1) for c,n in self.children.items()])

class WordDictionary(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.tree = Node(None)

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        node = self.tree
        for c in word:
            if c not in node:
                node.add_child(c)
            node = node.get_child(c)
        node.terminal = True

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could
        contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        queue = [(x, 0) for c, x in self.tree.children.items()]
        while queue:
            #print queue
            item, level = queue.pop(0)
            if level >= len(word):
                continue
            if self.match(item.value, word[level]):
                if item.terminal and len(word) == level + 1:
                    return True
                queue.extend([(x, level + 1) for c, x in item.children.items()])
        return False
    
    def match(self, ch, pat):
        if pat == '.':
            return True
        return ch == pat

        
# Your WordDictionary object will be instantiated and called as such:
wordDictionary = WordDictionary()
wordDictionary.addWord("a")
wordDictionary.addWord("a")
print wordDictionary.search("aa")
print wordDictionary.search(".a")
print wordDictionary.search("a.")
