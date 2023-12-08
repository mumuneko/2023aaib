#偶數對戰N//2，奇數是(n-1)//2
#持續比，直到冠軍出來
class Solution:
    def numberOfMatches(self, n: int) -> int:
        return n-1