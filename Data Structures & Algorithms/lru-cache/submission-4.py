class LRUCache:

    def __init__(self, capacity: int):
        self.d={} #key, Node pointer
        self.capacity=capacity
        self.head=ListNode(0,0)
        self.tail=ListNode(0,0)
        self.head.next=self.tail #recently visited
        self.tail.prev=self.head #least recently visited

    def delete_node(self, cur_node):
        #2links
        cur_node.prev.next=cur_node.next
        cur_node.next.prev=cur_node.prev

    def insert_from_the_head(self, cur_node):
        #4 links
        cur_node.next=self.head.next
        self.head.next=cur_node
        cur_node.next.prev=cur_node
        cur_node.prev=self.head
    def get(self, key: int) -> int:
        if key in self.d:
            #get node
            cur_node=self.d[key]
            #delete
            self.delete_node(cur_node)
            #add from head
            self.insert_from_the_head(cur_node)
            #update dict
            # self.d[key]=cur_node
            return cur_node.val
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
        
        if key in self.d: #key in cache
            #delete from linkedlist
            prev_node=self.d[key]
            self.delete_node(prev_node)
            #add new node and update list
           
        
        elif len(self.d)==self.capacity: #key not in cache, and cache is full 
            #remove the last one O(n)
            remove_node=self.tail.prev
            del self.d[remove_node.key]
            self.delete_node(remove_node)

            
     #add from the head to list and update dict
        new_node=ListNode(value,key)
        self.insert_from_the_head(new_node)
        self.d[key]=new_node


class ListNode:
    def __init__(self, val:int, key,next=None, prev=None):
        self.val=val
        self.key=key
        self.next=next
        self.prev=prev