import heapq
nums=[100,1,2,1,1,3,2,2,3,3,4,7,4,7,100]
k=3
heap=[]
count={}
for n in nums:
    count[n]=1+count.get(n,0)
for n,c in count.items():
    heap.append((-c,n))
print(heap)
heapq.heapify(heap)

ans=[]
for i in range(k):
    freq,num=heapq.heappop(heap)
    ans.append(num)
print(ans)

