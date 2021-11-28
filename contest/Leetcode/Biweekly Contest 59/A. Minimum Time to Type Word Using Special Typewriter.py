class Solution:
    def minTimeToType(self, word: str) -> int:
        pointer = "a"
        ans = len(word)
        for i in word:
            curr = ord(i) - ord("a")
          
            po  = ord(pointer) - ord("a")
 
            ans += min((curr-po) % 26,(po- curr) %26)
                       
            pointer = i
        return ans