class ListNode:

    def __init__(self,key=0,val=0,prev=None,next=None):
        self.val = val
        self.key = key
        self.prev = prev
        self.next = next

class LRUCache:

    def __init__(self, capacity: int):
        self.size = capacity
        self.map = {}
        self.dll = ListNode()
        self.lru = self.dll
        self.mru = self.dll

    def get(self, key: int) -> int:
        if key in self.map:
            target = self.map[key]
            if target != self.mru:
                target.prev.next = target.next
                target.next.prev = target.prev

                self.mru.next = target
                target.prev = self.mru
                target.next = None
                self.mru = self.mru.next
            return self.map[key].val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            self.map[key].val = value
            target = self.map[key]
            if target!= self.mru:
                target.prev.next = target.next
                target.next.prev = target.prev

                self.mru.next = target
                target.prev = self.mru
                target.next = None
                self.mru = self.mru.next
        
        elif( self.size > len(self.map)):
            self.mru.next = ListNode(key,value,self.mru) 
            self.mru = self.mru.next
            self.map[key] = self.mru
        else:
            self.mru.next = ListNode(key,value,self.mru) 
            self.mru = self.mru.next
            self.map[key] = self.mru

            del self.map[self.lru.next.key]
            self.lru.next = self.lru.next.next
            self.lru.next.prev = self.lru

            

            
            


