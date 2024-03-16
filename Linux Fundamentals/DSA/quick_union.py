class QuickUnion:
    def __init__(self, n):
        self.arr = [x for x in range(n)]

    def root(self, index):
        while True:
            if index == self.arr[index]:
                return(index)
                break
            else:
                index = self.arr[index]
        # Recursion, class isnt waiting properly therefore returning false
        # if index == self.arr[index]:
        #     return(index)
        # else:
        #     self.root(self.arr[index])

    def find(self, p, q):
        return self.root(p) == self.root(q)
        
    def union(self, p, q):
        root = self.root(p)
        self.arr[root] = self.root(q)
        # self.arr[p] = self.root(q)
        print(self.arr)

t = QuickUnion(10)
t.union(4,3)
t.union(3,8)
t.union(6,5)
t.union(9,4)
t.union(2,1)
t.union(5,0)
t.union(7,2)
t.union(6,1)
t.union(7,3)