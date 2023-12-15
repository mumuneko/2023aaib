#大標題
##小標題
1. 第1步
2. 第2步
  - 沒有數字的1
  - 沒有數字的2
  - 可以寫**程式碼** `print('Hello')` 要用數字123左邊的反撇
  
  
#慢慢理解set()怎麼用
s ={1,2,3,4,} #第1種，用大括號
print(s)
s=set((1,3,5,7)) #第2種，用set()裡面放你一開始要加入的東西
print(s)
s=set([1,2,4,3]) #類第2種的，set()裡面也可以放方括號list陣列的東西
print(s)
s=set('Hello') #類第2種的，set()裡面也可以放字串會把他一個個拆開
print(s)

#下面試試.add()和.remove()
s.add(100)
print(s)
s.remove('H')
print(s)