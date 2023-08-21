# FIFO : first item we insert is the first one we tack out 

class Queue:
    
    def  __init__(self):
        self.queue = []
    
    # O(1) running time 
    def is_empty(self):
        return self.queue == []
    
    # ? this operation has O(1) running time 
    def enqueue(self,data):
        self.queue.append(data)

    # todo O(N) linear running time  how to solve this problem ? // use Doubly linked list   
    def dequeue(self):
        if self.queue_size() < 1:
            return (-1) 
        data = self.queue[0]
        del self.queue[0]
        return data
    
    # ! O(1)  constant running time  
    def peek(self):
        return self.queue[0]
    
    # ! O(1) constant running time  
    def queue_size(self):
        return len(self.queue)
    
queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print('Size : %d' % queue.queue_size())
print('Dequeue : %d' % queue.dequeue())
print('Size : %d' % queue.queue_size())
