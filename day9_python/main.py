import numpy as np
PATH = "test2.txt"


class RopeNode:
    def __init__(self, id, x, y, n):
        self.loc=np.array([x,y])
        self.next=n
        self.visited=set()
        self.id=id

    def set_next(self, node):
        self.next=node

    def get_loc_r(self, locations):
        """return list of loc"""
        if self.next:
            self.next.get_loc_r(locations)
        locations.append(self.loc)
        return locations
        
    
    def get_count(self):
        return len(self.visited)

    def get_tail_visited(self):
        if self.next:
            return self.next.get_tail_visited()
        return self.visited
    
    def print_data_r(self):
        print("%s - %i" % (self.id, len(self.visited)))
        if self.next:
            self.next.print_data_r()
    
    def move(self, direction, steps):
        print("Direction[%s] - Steps[%i]" % (direction, steps))
        for i in range(steps):
            self._move_h(direction)
            if self.next:
                self.next._notify(self)
                
    def _move_h(self, direction):
        if direction == 'D':
            self.loc[1]=self.loc[1]-1
        elif direction == 'U':
            self.loc[1]=self.loc[1]+1
        elif direction == 'L':
            self.loc[0]=self.loc[0]-1
        elif direction == 'R':
            self.loc[0]=self.loc[0]+1
        else:
            print("Error - direction [%s] not recognized", direction)
            
    def _notify(self, node):
        self._update(node._get_loc())

    def _get_loc(self):
        return self.loc

    def _update(self, target):
        diff=(target-self.loc)
        print("ID:" + self.id + " DIFF:" + str(diff))
        assert(abs(diff[0]) < 4 and abs(diff[1]) < 4)
        if diff[0]==2 and diff[1]==0:
            # horizontal update - right
            self.loc[0]=self.loc[0]+1
            diff=(target-self.loc)
            assert(diff[0]==1 and diff[1]==0)
        elif diff[0]==-2 and diff[1]==0:
            # horizontal update - left
            self.loc[0]=self.loc[0]-1
            diff=(target-self.loc)
            assert(diff[0]==-1 and diff[1]==0)
        elif diff[1]==2 and diff[0]==0:
            # vertical update - up
            self.loc[1]=self.loc[1]+1
            diff=(target-self.loc)
            assert(diff[0]==0 and diff[1]==1)
        elif diff[1]==-2 and diff[0]==0:
            # vertical update - down
            self.loc[1]=self.loc[1]-1
            diff=(target-self.loc)
            assert(diff[0]==0 and diff[1]==-1)
        elif diff[0]==2 and diff[1]==1 or diff[0]==1 and diff[1]==2 or diff[0]==2 and diff[1]==2:
            # diag update - top right
            self.loc[0]=self.loc[0]+1
            self.loc[1]=self.loc[1]+1
            if diff[0]==2 and diff[1]==1:
                diff=(target-self.loc)
                assert(diff[0]==1 and diff[1]==0)
            elif diff[0]==2 and diff[1]==2:
                diff=(target-self.loc)
                assert(diff[0]==1 and diff[1]==1)
            else:
                diff=(target-self.loc)
                assert(diff[0]==0 and diff[1]==1)
        elif diff[0]==2 and diff[1]==-1 or diff[0]==1 and diff[1]==-2:
            # diag update - top right
            self.loc[0]=self.loc[0]+1
            self.loc[1]=self.loc[1]-1
            if diff[0]==2:
                diff=(target-self.loc)
                assert(diff[0]==1 and diff[1]==0)
            else:
                diff=(target-self.loc)
                assert(diff[0]==0 and diff[1]==-1)
        elif diff[0]==-2 and diff[1]==-1 or diff[0]==-1 and diff[1]==-2:
            self.loc[0]=self.loc[0]-1
            self.loc[1]=self.loc[1]-1
            if diff[0]==-2:
                diff=(target-self.loc)
                assert(diff[0]==-1 and diff[1]==0)
            else:
                diff=(target-self.loc)
                assert(diff[0]==0 and diff[1]==-1)
        elif diff[0]==-2 and diff[1]==1 or diff[0]==-1 and diff[1]==2:
            self.loc[0]=self.loc[0]-1
            self.loc[1]=self.loc[1]+1
            if diff[0]==-2:
                diff=(target-self.loc)
                assert(diff[0]==-1 and diff[1]==0)
            else:
                diff=(target-self.loc)
                assert(diff[0]==0 and diff[1]==1)
        if tuple(self.loc) not in self.visited:
            self.visited.add(tuple(self.loc))
        if self.next:
            self.next._notify(self)



def print_grid(loc, x,y, offset):
    s=False
    print("Locations")
    for l in loc:
        print("%i - %i" % (l[0], l[1]))
    for i in range(offset,x):
        for j in range(offset,y):
            for l in loc:
                if l[0] == i and l[1] == j:
                    print("#", end="")
                    s=True         
                    break
            if not s:
                print("-", end="")
            s=False
        print("")
        


with open(PATH, "r") as file:
    data = file.readlines()
    startx=100
    starty=100
    head=RopeNode('head', startx, starty, None)
    prev=head
    for i in reversed(range(0,9)):
        next=RopeNode(str(i), startx, starty, None)
        prev.set_next(next)
        prev=next
    head.print_data_r()
    for cmd in data:
        print(cmd)
        cmd=cmd.split(' ')
        head.move(cmd[0].rstrip(), int(cmd[1].rstrip()))
        loc=[]
        head.get_loc_r(loc)
        #print_grid(loc, 150, 150, 75)
    tail_list=list(head.get_tail_visited())
    print_grid(tail_list, 150, 150, 75)
    head.print_data_r()
