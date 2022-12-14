import numpy as np
PATH = "real.txt"


class Rope:
    def __init__(self, x, y):
        self.h=np.array([x,y])
        self.t=np.array([x,y])
        self.visited=set()
        
    def move(self, direction, steps):
        print("Direction[%s] - Steps[%i]" % (direction, steps))
        for i in range(steps):
            self._move_h(direction)
            self._update_t()

    def _move_h(self, direction):
        if direction == 'D':
            self.h=(self.h[0],self.h[1]-1)
        elif direction == 'U':
            self.h=(self.h[0],self.h[1]+1)
        elif direction == 'L':
            self.h=(self.h[0]-1,self.h[1])
        elif direction == 'R':
            self.h=(self.h[0]+1,self.h[1])
        else:
            print("Error - direction [%s] not recognized", direction)

    def _update_t(self):
        """TODO swap left and right"""
        print("========")
        print("current t:")
        print(self.t)
        print("current h:")
        print(self.h)
        print("Diff: ")
        diff=(self.h-self.t)
        print(diff)
        if abs(diff[0]) > 2 or abs(diff[1]) > 2:
            print("wowowowowowow")
            exit(1)
        if diff[0]==2 and diff[1]==0:
            # horizontal update - right
            self.t=np.array((self.h[0]-1, self.t[1]))
            print("update horz-right: ")
            print(self.t)
            diff=(self.h-self.t)
            assert(diff[0]==1 and diff[1]==0)
        elif diff[0]==-2 and diff[1]==0:
            # horizontal update - left
            self.t=np.array((self.h[0]+1, self.t[1]))
            print("update horz-left: ")
            print(self.t)
            diff=(self.h-self.t)
            assert(diff[0]==-1 and diff[1]==0)
        elif diff[1]==2 and diff[0]==0:
            # vertical update - up
            self.t=np.array((self.t[0], self.h[1]-1))
            print("update vert-up: ")
            print(self.t)
            diff=(self.h-self.t)
            assert(diff[0]==0 and diff[1]==1)
        elif diff[1]==-2 and diff[0]==0:
            # vertical update - down
            self.t=np.array((self.t[0], self.h[1]+1))
            print("update vert-down: ")
            print(self.t)
            diff=(self.h-self.t)
            assert(diff[0]==0 and diff[1]==-1)
        elif diff[0]==2 and diff[1]==1 or diff[0]==1 and diff[1]==2:
            # diag update - top right
            self.t=np.array((self.t[0]+1, self.t[1]+1))
            print("update diag-top-right: ")
            print(self.t)
            if diff[0]==2:
                diff=(self.h-self.t)
                assert(diff[0]==1 and diff[1]==0)
            else:
                diff=(self.h-self.t)
                assert(diff[0]==0 and diff[1]==1)
        elif diff[0]==2 and diff[1]==-1 or diff[0]==1 and diff[1]==-2:
            # diag update - bottom right
            self.t=np.array((self.t[0]+1, self.t[1]-1))
            print("update diag-bootom-right: ")
            print(self.t)
            if diff[0]==2:
                diff=(self.h-self.t)
                assert(diff[0]==1 and diff[1]==0)
            else:
                diff=(self.h-self.t)
                assert(diff[0]==0 and diff[1]==-1)
        elif diff[0]==-2 and diff[1]==-1 or diff[0]==-1 and diff[1]==-2:
            # diag update - bottom left
            self.t=np.array((self.t[0]-1, self.t[1]-1))
            print("update diag-bootom-left: ")
            print(self.t)
            if diff[0]==-2:
                diff=(self.h-self.t)
                assert(diff[0]==-1 and diff[1]==0)
            else:
                diff=(self.h-self.t)
                assert(diff[0]==0 and diff[1]==-1)
        elif diff[0]==-2 and diff[1]==1 or diff[0]==-1 and diff[1]==2:
            # diag update - top left
            self.t=np.array((self.t[0]-1, self.t[1]+1))
            print("update diag-top-left: ")
            print(self.t)
            print("Ok")
            print(diff)
            if diff[0]==-2:
                diff=(self.h-self.t)
                assert(diff[0]==-1 and diff[1]==0)
            else:
                diff=(self.h-self.t)
                assert(diff[0]==0 and diff[1]==1)
        # add to set
        (x,y)=self.t
        d=(x,y)
        if d not in self.visited:
            print("Adding place: " + str(d) + " Count: " + str(len(self.visited)+1))
            self.visited.add(d)
            
    def print_final(self):
        print(self.h)
        print(self.t)
        print(len(self.visited))
        # Create an N by N grid filled with *
        first=max(self.visited, key=lambda x: x[0])[0]
        second=max(self.visited, key=lambda x: x[1])[1]
        x_min=list(self.visited)[0][0]
        x_max=list(self.visited)[0][0]
        y_min=list(self.visited)[0][1]
        y_max=list(self.visited)[0][1]
        for a,b in self.visited:
            if a > x_max:
                x_max=a
            elif a < x_min:
                x_min=a
            if b > y_max:
                y_max = b
            elif b < y_min:
                y_min = b
        print("x_min: [%i]" % x_min)
        print("x_max: [%i]" % x_max)
        print("y_min: [%i]" % y_min)
        print("y_max: [%i]" % y_max)
        N=first if (first>second) else second
        grid = [["*" for _ in range(N+1)] for _ in range(N+1)]

        # Loop over the list of tuples and update the grid
        #for x, y in self.visited:
         #   grid[x][y] = "#"

        # Loop over the grid and print each row on a separate line
        #for row in grid:
         #   print(" ".join(row))
        
with open(PATH, "r") as file:
    data = file.readlines()
    rope=Rope(10000, 10000)
    for cmd in data:
        cmd=cmd.split(' ')
        rope.move(cmd[0].rstrip(), int(cmd[1].rstrip()))
    rope.print_final()
