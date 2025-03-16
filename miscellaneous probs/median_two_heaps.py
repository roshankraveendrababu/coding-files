import heapq
class Heap:
    def __init__(self):
        self.min_heap=[] #stores values lesser than median in an max_heap
        self.max_heap=[] #stores values greater than median in an min_heap
    def find_median(self):
        if len(self.min_heap)>len(self.max_heap):
            return -1*self.min_heap[0]
        elif len(self.min_heap)<len(self.max_heap):
            return self.max_heap[0]
        else:
            return (-1*self.min_heap[0]+self.max_heap[0])/2
        
    def insert(self,val):
        heapq.heappush(self.min_heap,-1*val)
        if self.min_heap and self.max_heap and -1*self.min_heap[0]>self.max_heap[0]:
            val=-1*heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap,val)
        if len(self.min_heap)>len(self.max_heap)+1:
            val=self.min_heap[0]*-1
            heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap,val)
        elif len(self.max_heap)>len(self.min_heap)+1:
            val=heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap,-1*val)
        return self.find_median()
    
if __name__=="__main__":
    heap=Heap()
    arr=list(map(int, input().split()))
    ans=[]
    for i in range(len(arr)):
        ans.append(heap.insert(arr[i]))
    print(ans)

