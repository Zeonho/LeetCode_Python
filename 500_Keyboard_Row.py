class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        
        def checkCharacter(word, row):
            for c in word:
                if c not in row:
                    return False
            return True
        
        
        row1 = "qwertyuuiop"
        row2 = "asdfghjkl"
        row3 = "zxcvbnm"
        
        ret = []
        
        for word in words:
            if (checkCharacter(word.lower(), row1)):
                ret.append(word)
            elif (checkCharacter(word.lower(), row2)):
                ret.append(word)
            elif (checkCharacter(word.lower(), row3)):
                ret.append(word)
        
        return ret
