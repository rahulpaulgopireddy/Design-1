
# // Time Complexity :
# add: O(n)
# remove : O(n)
# contains : O(n)
# as we are iterate through linkedList its not optimum 
# // Space Complexity : O(1 )
# // Did this code successfully run on Leetcode : yes
# // Any problem you faced while coding this :


# // Your code here along with comments explaining your approach



# collision is handled by linear chaining , so linkedList is assaigned to every key 
# define LinkedList class to create a LinkedList 
# 10**4 array is created with a LinkedList of value 0

# on add , index or currentnode is searched for by take modulus of keu with len of the set

class ListNode:

    def __init__(self,key):
        self.key = key
        self.next = None
        

class MyHashSet:

    def __init__(self):
        
      self.set = [ListNode(0) for i in range(10**4) ]

    def add(self, key: int) -> None:

        curr = self.set[key % len(self.set)]
        while curr.next:
            # return if key already present or else continue to iterate
            if curr.next.key == key:
                return 
            curr = curr.next
            # add new node to current listnode
        curr.next = ListNode(key)
        

    def remove(self, key: int) -> None:
        curr = self.set[key % len(self.set)]

        while curr.next:
            # if key is found current node.next value is updated and return or else continue to iterate
            if curr.next.key == key:
                curr.next = curr.next.next
                return
            curr = curr.next
        

    def contains(self, key: int) -> bool:
        #  to find current node 
        curr = self.set[key % len(self.set)]
        # if key is found return boolean true or else continue to iterate till key is found
        while curr.next:
            if curr.next.key == key:
                return True
            curr = curr.next
        return False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)