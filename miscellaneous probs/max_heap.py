class Heap:
    def __init__(self):
        self.heap=[]

    def parent(self,index):
        return (index-1)//2
    
    def left_child(self,index):
        return (index*2)+1
    
    def right_child(self,index):
        return (index*2)+2
    

    def insert_swap(self,index):
        if index==0:
            return
        parent_val=self.heap[self.parent(index)]
        if parent_val<self.heap[index]:
            self.heap[self.parent(index)],self.heap[index]=self.heap[index],self.heap[self.parent(index)]
        self.insert_swap(self.parent(index))
    
    def insert(self,val):
        self.heap.append(val)
        self.insert_swap(len(self.heap)-1)

    def remove(self):
        if not self.heap:
            return None
        val=self.heap[0]
        if len(self.heap)==1:#edge case: when cant assign an value when we have popped the only element
            self.heap.pop()
        else:
            self.heap[0]=self.heap.pop()
            self.remove_facilitate(0)
        return val


    def remove_facilitate(self,index):
        curr_val=self.heap[index]
        left_val=0
        right_val=0
        if self.left_child(index)<len(self.heap):
            left_val=self.heap[self.left_child(index)]
        if self.right_child(index)<len(self.heap):
            right_val=self.heap[self.right_child(index)]
        min_index=self.heap.index(max(curr_val,max(left_val,right_val)))
        if index!=min_index:
            self.heap[index],self.heap[min_index]=self.heap[min_index],self.heap[index]
            self.remove_facilitate(min_index)

if __name__=="__main__":
    heap=Heap()
    arr=list(map(int,input().split()))
    for i in range(len(arr)):
        heap.insert(arr[i])
    print(heap.heap)
    ans=[]
    while len(heap.heap):
        ans.append(heap.remove())
    print(ans)

    

    