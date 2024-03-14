class QuickFind:
    def __init__(self, arr, p, q):
        self.arr = arr
        self.p = p
        self.q = q
    def find(self):
        print('hi')
        if self.arr[self.p] == self.arr[self.q]:
            return true
        else:
            return false
    def union(self):
        old_id_value = self.arr[self.p]
        updated_id_value = self.arr[self.q]
        for i in range(len(self.arr) - 1):
            if self.arr[i] == old_id_value:
                self.arr[i] = updated_id_value
        print(self.arr)


test = QuickFind([0,1,1,8,8,0,0,1,8,8],6,1)
print(test.union())