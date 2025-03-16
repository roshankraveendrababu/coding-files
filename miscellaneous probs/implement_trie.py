class TrieNode:
    def __init__(self):
        self.children={}
        self.word=False

class Trie:
    def __init__(self):
        self.root=TrieNode()
    
    def insert(self,word):
        curr=self.root
        for letter in word:
            if letter not in curr.children:
                curr.children[letter]=TrieNode()
            curr=curr.children[letter]
        curr.word=True

    def search_word(self,word):
        curr=self.root
        for letter in word:
            if letter not in curr.children:
                return False
            curr=curr.children[letter]
        return curr.word
    
    def search_prefix(self,prefix):
        curr=self.root
        for letter in prefix:
            if letter not in curr.children:
                return False
            curr=curr.children[letter]
        return True
    
#driver code
if __name__=="__main__":
    trie=Trie()
    sentence=list(input().split())
    for word in sentence:
        trie.insert(word)
    
    print(trie.search_word(sentence[1]))
    print(trie.search_word("roshan"))
    print(trie.search_prefix(sentence[2][:2]))
    print(trie.search_prefix("bujji"))
    