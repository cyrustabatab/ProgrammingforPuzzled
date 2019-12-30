

class SuffixTrie:
    
    END_SYMBOL = "*"

    def __init__(self,word):
        self.root = {}
        self._getSuffixes(word)

    def _getSuffixes(self,word):

        for i in reversed(range(len(word))):
            self.add(i,word)

    def add(self,index,word):
        
        current = self.root
        for i in range(index,len(word)):
            c = s[i]
            if c not in current:
                current[c] = {}

            current = current[c]

        current[SuffixTrie.END_SYMBOL] = True
    
    def __contains__(self,suffix):

        current = self.root

        for c in suffix:
            if c not in current:
                return False

            current = current[c]

        return Trie.END_SYMBOL in current


if __name__ == "__main__":
    
    s = 'diving'

    trie = SuffixTrie(s)

    print(trie.root)
            


         

class Trie:
    
    END_SYMBOL = "*"
    def __init__(self):
        self.root = {}

    def add(self,word):
        current = self.root

        for c in word:
            if c not in current:
                current[c] = {}

            current = current[c]


        current[Trie.END_SYMBOL] = True
    
    def autocomplete(self,w):
        results = []
        current = self.root

        for c in w:
            if c not in current:
                break
            current = current[c]
        else:
            self.getWordsFrom(current,w,results)
        
        return results

    def getWordsFrom(self,node,w,result):
        if Trie.END_SYMBOL in node:
            results.append(w)

        for c in node:
            if c != Trie.END_SYMBOL:
                self.getWordsFrom(node[c],w + c,results)


    def __contains__(self,word):
        current = self.root
        for c in word:
            if c not in current:
                return False
            current = current[c]

        return Trie.END_SYMBOL in current

    def delete(self,word):
        current = self.root
        for c in word:
            if c not in current:
                return 
            
            current = current[c]


        if Trie.END_SYMBOL not in current:
            return

        del current[Trie.END_SYMBOL]

        if len(current) > 0:
            return

        self.removeLastNodeMultipleChildren(word)

    def removeLastNodeMultipleChildren(self,word):
        current = self.root
        lastNodeMultipleChildren = None
        childToBreak = None
        
        for i,c in enumerate(word[:-1]):
            if c not in current:
                return

            current = current[c]

            hasMultipleChildren = False
            count = 0
            for char in current:
                if char != Trie.END_SYMBOL: 
                    count += 1
                    if count == 2:
                        hasMultipleChildren = True
                        break

            if hasMultipleChildren or Trie.END_SYMBOL in current:
                lastNodeMultipleChildren = current
                childToBreak = word[i + 1]

        if lastNodeMultipleChildren:
            del lastNodeMultipleChildren[childToBreak]
        else:
            del self.root[word[0]]


