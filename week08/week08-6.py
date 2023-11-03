a=[9,8,7,6,5,4,3,2,1,0]
N=len(a)
print(a) #排之前，印一下
class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        #現在還沒寫完，先把week-3的兩兩比較寫出來
        N=len(arr)#小心，題目不是a是arr

        #for k in range(N):
        #   for i in range(1,N):
        #        if arr[i]<arr[i-1]:
        #            arr[i],arr[i-1]=arr[i-1],arr[i]
        arr.sort()

        for i in range(1,N):
            if arr[i]-arr[i-1] !=arr[1]-arr[0]:
                return False
        return True