#Leet code-1436. Destination City
class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        notAns=set()
        for a,b in paths: #先巡第一次
            notAns.add(a) #出發點不是答案
        for a,b in paths: #第2輪
            if b not in notAns: #b不在出發裡，就是答案
                return b #若b不是，不是答案