class LRUCache:

    def __init__(self, capacity: int):
        self.d={} #key, Node pointer
        self.length=0
        self.capacity=capacity
        self.head=ListNode(0,0)
        self.tail=ListNode(0,0)
        self.head.next=self.tail #recently visited
        self.tail.prev=self.head #least recently visited

    def get(self, key: int) -> int:
        if key in self.d:
            cur_node=self.d[key]
            #delete
            cur_node.prev.next=cur_node.next
            cur_node.next.prev=cur_node.prev
            #add from head
            cur_node.next=self.head.next
            self.head.next=cur_node
            cur_node.next.prev=cur_node
            cur_node.prev=self.head
            #update dict
            self.d[key]=cur_node
            return cur_node.val
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
        
        if key in self.d:
            #delete from linkedlist
            prev_node=self.d[key]
            prev_node.prev.next=prev_node.next
            prev_node.next.prev=prev_node.prev
            #add new node and update list
           
        else:
            if self.length==self.capacity: #full
                #remove the last one O(n)
                remove_node=self.tail.prev
                del self.d[remove_node.key]
                remove_node.prev.next=self.tail
                self.tail.prev=remove_node.prev
                #add new node and update list
            else:
                self.length+=1
     #add from the head to list and update dict

        new_node=ListNode(value,key)
        new_node.next=self.head.next
        self.head.next=new_node
        new_node.next.prev=new_node
        new_node.prev=self.head
        self.d[key]=new_node


class ListNode:
    def __init__(self, val:int, key,next=None, prev=None):
        self.val=val
        self.key=key
        self.next=next
        self.prev=prev