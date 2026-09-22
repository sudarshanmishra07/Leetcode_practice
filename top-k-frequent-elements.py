import heapq
nums=[1,1,1,1,2,2,2,3,3,3,100]
k=2
heap=[]
count={}
for n in nums:
    count[n]=1+count.get(n,0)
for n,c in count.items():
    heap.append((-c,n))
heapq.heapify(heap)

ans=[]
for i in range(k):
    num=heapq.heappop(heap)
    ans.append(num)
print(ans)

