# // Time Complexity : O(1)
# // Space Complexity : 
# // Did this code successfully run on Leetcode : yes 
# // Any problem you faced while coding this :


# // Your code here along with comments explaining your approach

# intution : to have corresponding stack with minValue , in the min value on each push 
# only min value  is pushed into minStack , if not its pushed into stack 

class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        stack.append(val)
        ## if there is no value in minstack or it the value is <= top of minstack then append

        if not self.minstack and val <= self.minStack[-1]:
            self.minStack.append(val) 


    def pop(self) -> None:
        # you have to pop stack anyways , but condition to pop minstack is if the popped value of stack is equal to top value of minStack  
        if self.stack.pop() == self.minStack[-1]:
            self.minStack.pop()
# return top element with O(1)
    def top(self) -> int:
        return stack[-1]
# return minimum element with O(1) 
    def getMin(self) -> int:
        return minStack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()