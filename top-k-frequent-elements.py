import heapq
nums=[100,1,2,1,1,3,2,2,3,3,4,7,4,7,100]        #input array
k=3
heap=[]
count={}
for n in nums:                                  #count frequency of each number
    count[n]=1+count.get(n,0)
for n,c in count.items():                       #store (-frequency number) for max heap
    heap.append((-c,n))
print(heap)
heapq.heapify(heap)                             #convert list into heap

ans=[]
for i in range(k):                              #extracting top k frequent elements
    freq,num=heapq.heappop(heap)
    ans.append(num)
print(ans)