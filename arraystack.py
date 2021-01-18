from exceptions import Empty

#array based stack
class ArrayStack:
    """LIFO stack implementation using a Python List as underlying storage"""
    
    def __init__(self):
        """Create an empty stack"""
        self._data = [] #non-public list instance
    
    def __len__(self):
        """Return the number of elements in the stack"""
        return len(self._data)
    def is_empty(self):
        """Return True if the stack is empty"""
        return len(self._data)==0
    
    def push(self, e):
        """Add element e to the top of the stack"""
        self._data.append(e)  #new item stored at end of the list
        
    def top(self):
        """Return (but do not remove) the element at the top of the stack
        
        Raise Empty exception if the stack is empty"""
        
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data[-1] #the last item in the list
    
    def pop(self):
        """Remove and return the element from the top of the stack (i.e. LIFO)
        
        Raise Empty exception if the stack is empty"""
        
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data.pop() #remove the last item from the list
    