
from HanoiTower_recur import Tower

def element_transfer (tower1:Tower, tower2:Tower):
    if tower1.top_disk() > tower2.top_disk():
        tower1.add(tower2.pop())
    else:
        tower2.add(tower1.pop())
    
def hanoi_alg_iter(begin:Tower, temp:Tower, end:Tower):
    tw_hight = len(begin.elements)
    while len(end.elements) != tw_hight:
        if tw_hight % 2 == 0:
            tw_list=[(begin, temp), (begin, end), (temp, end)]
            for tw1, tw2 in tw_list:
                element_transfer(tw1, tw2)
                if len(end.elements) == tw_hight:
                    break

        else:
            tw_list=[(begin, end), (begin, temp), (temp, end)]
            for tw1, tw2 in tw_list:
                element_transfer(tw1, tw2)
                if len(end.elements) == tw_hight:
                    break            
              
if __name__ == "__main__":
        tw_begin = Tower(7)
        tw_temp = Tower(0) 
        tw_end = Tower(0)
        
        hanoi_alg_iter(tw_begin, tw_temp, tw_end)
        
        print(tw_begin)
        print(tw_temp)
        print(tw_end)
        
        