class QuickFind:
    def __init__(self, n):
        self.arr = [x for x in range(n)]

    def find(self,p,q):
        print(self.arr[p] == self.arr[q])
        
    def union(self,p,q):
        old = self.arr[p]
        new = self.arr[q]
        for i in range(len(self.arr)):
            if self.arr[i] == old:
                self.arr[i] = new
        print(self.arr)

t = QuickFind(5)
t.find(1,3)
t.union(1,2)
t.union(3,1)
t.union(4,0)