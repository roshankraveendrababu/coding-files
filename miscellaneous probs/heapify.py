class Heapify:
    def __init__(self):
        self.heap=[]


    def parent(self,index):
        return (index-1)//2
    
    def left_child(self,index):
        return (index*2)+1
    
    def right_child(self,index):
        return (index*2)+2
    

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

    def sort_arr(self,arr):
        curr=(len(arr))//2
        self.heap=arr
        while curr:
            i=curr
            self.remove_facilitate(i)
            curr-=1
        return self.heap