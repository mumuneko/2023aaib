# 1 2 4 8 16 32 128 256
class Solution:
    def isPowerOfTwo(self,n: int) -> bool:
        #還沒寫完，勿送出。(現在已寫完)若n是負數，就會是錯誤的
        if n <= 0:return False #現在成功了
        while n>1:#因為1是2^0不用再除了
            if n%2 !=0:#竟然餘數不是0
                return False #失敗
            n=n//2
        #經過樓上的檢查，都沒有出錯的話
        return True #就是成功