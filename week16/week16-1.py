#1160. Find Words That Can Be Formed by Characters
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        ans=0
        H={}
        for c in chars:
            if c in H:H[c]+=1
            else:H[c]=1
        for word in words: #words很多字，word是其中一個字
        #裡面要查查看，能不能用chars來組合出word這個字
            wordH={}#中間要做比對，看能不能成功
            for c in word:
                if c in wordH:wordH[c]+=1
                else:wordH[c]=1
            bad=0
            for c in wordH:#能不能用chars來組合出word這個字
                if(c not in H)or wordH[c]>H[c]:
                    bad=1 #沒在裡面 or 不夠用
            if bad==0:ans+=len(word) #如果成功了，ans就增加
        return ans