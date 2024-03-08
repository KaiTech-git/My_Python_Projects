
class Tower():
    def __init__(self,n_elem:int = 0):
        if n_elem > 0:
            self.elements = [x for x in range(1,n_elem+1)][::-1]
        else:
            self.elements=[]
    def pop(self):
        return self.elements.pop()
    def add(self,element):
        self.elements.append(element)
    def top_disk(self):
        try:
            return self.elements[-1]
        except:
            return 100
    def __str__(self):
        return str(self.elements)
    
def hanoi_alg_rec(begin:Tower, temp:Tower, end:Tower, n:int):
    
    if n == 1:
        end.add(begin.pop())

    else:
        hanoi_alg_rec(begin = begin,temp = end,end = temp, n=n-1)
    
        end.add(begin.pop())
        
        hanoi_alg_rec(begin = temp,temp = begin,end = end, n=n-1)

        return

    
        
if __name__ == "__main__":
        tw_begin = Tower(10)
        tw_temp = Tower(0) 
        tw_end = Tower(0)
        
        hanoi_alg_rec(tw_begin, tw_temp, tw_end, len(tw_begin.elements))
        
        print(tw_begin)
        print(tw_temp)
        print(tw_end)