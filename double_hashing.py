# // Time Complexity :
# // Space Complexity :
# // Did this code successfully run on Leetcode :
# // Any problem you faced while coding this :


# // Your code here along with comments explaining your approach


class MyHashSet:

    def __init__(self):
        self.bucketSize = 1000
        self.bucket = [None] * self.bucketSize

    def hashP(self, key: int) -> int:
        return key % self.bucketSize

    def hashS(self, key: int) -> int:
        return key // self.bucketSize

    def add(self, key: int) -> None:
        h1 = self.hashP(key)
        h2 = self.hashS(key)

        if self.bucket[h1] is None:
            self.bucket[h1] = [False] * self.bucketSize
        self.bucket[h1][h2] = True

    def remove(self, key: int) -> None:
        h1 = self.hashP(key)
        h2 = self.hashS(key)

        if self.bucket[h1] is not None:
            self.bucket[h1][h2] = False

    def contains(self, key: int) -> bool:
        h1 = self.hashP(key)
        h2 = self.hashS(key)

        if self.bucket[h1] is None:
            return self.bucket[h1][h2]

# Test the MyHashSet class
# hash_set = MyHashSet()
# hash_set.add(1)
# hash_set.add(2)
# hash_set.add(3)
# hash_set.remove(2)

# print(hash_set.contains(1))  # True
# print(hash_set.contains(2))  # False
