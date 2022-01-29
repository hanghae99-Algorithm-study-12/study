class BinaryHeap(object):
    def __init__(self):
        self.items=[None]
    def __len__(self):
        return len(self.items)-1
    def _percolate_up(self):
        i=len(self)
        parent=i//2
        while parent>0:
            if self.items[i]<self.items[parent]:
                self.items[i],self.items[parent]=\
                self.items[parent], self.items[i]
            i=parent
            parent=i//2
        return
    def insert(self,k):
        self.items.append(k)
        self._percolate_up()
    def _percolate_down(self,idx):
        left = 2*idx
        right = 2*idx+1
        smallest = idx
        if left<=len(self) and self.items[left]<self.items[smallest]: # 루트가 왼쪽보다 크다면
            smllest=left
        if right <= len(self) and self.items[right] < self.items[smallest]: # 루트가 오른쪽보다 크다면
            smllest = right

        if smallest != idx: # 바껴야한다면
            self.items[smallest],self.items[idx]= \
                self.items[idx], self.items[smallest]
            self._percolate_down(smallest)
        return
    def extract(self):
        extracted = self.items[1]
        self.items[1]=self.items[len(self)] # 마지막이랑 루트 랑 바꿔주는거
        self.items.pop()# 마지막 버려주고
        self._percolate_down(1)
        return extracted
