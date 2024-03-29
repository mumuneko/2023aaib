#1704. Determine if String Halves Are Alike
class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        N=len(s) #字串的長度 ex.s="textbook"
        a=s[:N//2]#前半段 a=text
        b=s[N//2:]#後半段 b=book
        motherA=0 #a的母音有幾個
        motherB=0 #b的母音有幾個
        for c in a: #在a裡面的每一個字母c逐一檢查
            if c=='a' or c=='e' or c=='i' or c=='o' or c=='u':#小寫字母
                motherA +=1
            if c=='A' or c=='E' or c=='I' or c=='O' or c=='U':#大寫字母
                motherA +=1
        for c in b: #在裡面的每一個字母c逐一檢查
            if c=='a' or c=='e' or c=='i' or c=='o' or c=='u':#小寫字母
                motherB +=1
            if c=='A' or c=='E' or c=='I' or c=='O' or c=='U':#大寫字母
                motherB +=1
        if motherA==motherB: return True
        else:return False