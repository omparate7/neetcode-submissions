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

    def remove(self,target):
        target.prev.next = target.next
        target.next.prev = target.prev

    def insert(self,target):
        self.mru.next = target
        target.prev = self.mru
        target.next = None
        self.mru = self.mru.next

    def get(self, key: int) -> int:
        if key in self.map:

            target = self.map[key]

            if target != self.mru:
                self.remove(target)
                self.insert(target)

            return target.val

        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.map:

            self.map[key].val = value
            target = self.map[key]

            if target!= self.mru:
                self.remove(target)
                self.insert(target)
        
        else:
            self.insert(ListNode(key,value))
            self.map[key] = self.mru

            if(len(self.map)>self.size):

                del self.map[self.lru.next.key]
                self.remove(self.lru.next)

            

            
            


