class Heap:
    def __init__(self):
        self.min_heap=[]#to store the values larger than the median
        self.max_heap=[]# to store the values smaller than the median

    def add_min_heap(self,val):
        self.min_heap.append(val)
        index=len(self.min_heap)-1
        while index>0:
            parent=(index-1)//2
            if self.min_heap[parent]>self.min_heap[index]:
                self.min_heap[parent],self.min_heap[index]=self.min_heap[index],self.min_heap[parent]
            index=parent

    def remove_min_heap(self):
        val=self.min_heap[0]
        if len(self.min_heap)==1:#edge case: when cant assign an value when we have popped the only element
            self.min_heap.pop()
        else:
            self.min_heap[0]=self.min_heap.pop()
            self.remove_facilitate_min(0)
        return val


    def remove_facilitate_min(self,index):
        
        min_index = index
        if (index * 2) + 1 < len(self.min_heap) and self.min_heap[(index * 2) + 1] < self.min_heap[min_index]:
            min_index = (index * 2) + 1
        if (index * 2) + 2 < len(self.min_heap) and self.min_heap[(index * 2) + 2] < self.min_heap[min_index]:
            min_index = (index * 2) + 2

        if index!=min_index:
            self.min_heap[index],self.min_heap[min_index]=self.min_heap[min_index],self.min_heap[index]
            self.remove_facilitate_min(min_index)

    def add_max_heap(self,val):
        self.max_heap.append(val)
        index=len(self.max_heap)-1
        while index>0:
            parent=(index-1)//2
            if self.max_heap[parent]<self.max_heap[index]:
                self.max_heap[parent],self.max_heap[index]=self.max_heap[index],self.max_heap[parent]
            index=parent

    def remove_max_heap(self):
        val=self.max_heap[0]
        if len(self.max_heap)==1:
            self.max_heap.pop()
        else:
            self.max_heap[0]=self.max_heap.pop()
            self.remove_facilitate_max(0)
        return val
    
    def remove_facilitate_max(self,index):
        
        max_index = index
        if (index * 2) + 1 < len(self.min_heap) and self.min_heap[(index * 2) + 1] >self.min_heap[max_index]:
            max_index = (index * 2) + 1
        if (index * 2) + 2 < len(self.min_heap) and self.min_heap[(index * 2) + 2] > self.min_heap[max_index]:
            max_index = (index * 2) + 2
        if index!=max_index:
            self.max_heap[index],self.max_heap[max_index]=self.max_heap[max_index],self.max_heap[index]
            self.remove_facilitate_max(max_index)

    def insert(self,val):
        self.add_max_heap(-1*val)
        if self.min_heap and self.max_heap[0]>self.min_heap[0]:
            val=self.remove_max_heap()
            self.add_min_heap(-1*val)
        if len(self.max_heap)>len(self.min_heap)+1:
            val=self.remove_max_heap()
            self.add_min_heap(-1*val)
        if len(self.min_heap)>len(self.max_heap)+1:
            val=self.remove_min_heap()
            self.add_max_heap(-1*val)
        return self.find_median()
    

    def find_median(self):
        if len(self.min_heap)>len(self.max_heap):
            return self.min_heap[0]
        elif len(self.min_heap)<len(self.max_heap):
            return -1*self.max_heap[0]
        else:
            return (self.min_heap[0]+(-1*self.max_heap[0]))/2.0
        
#driver code
if __name__ == "__main__":
    heap=Heap()
    arr=list(map(int, input().split()))
    ans=[]
    for i in range(len(arr)):
        ans.append(heap.insert(arr[i]))
    print(ans)