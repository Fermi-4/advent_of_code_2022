import os
import re
import queue

PATH = "real.txt"

class MyFile:
    def __init__(self, name, size):
        self.name = name
        self.size = size

class MyDir:
    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        self.dirs = []
        self.files = []

    def get_parent(self):
        return self.parent

    def get_size(self):
        size = 0
        for f in self.files:
            size+=f.size
        for d in self.dirs:
            size+=d.get_size()
        return size

    def _reach_up(self, count):
        if self.parent:
            count = self.parent._reach_up(count+1)
        return count
    
    def add_file(self, name, size):
        file = MyFile(name, size)
        self.files.append(file)
    
    def create_sub_directory(self, name):
        subdir = MyDir(name, self)
        self.dirs.append(subdir)
        return subdir
    
    def get_child_directory(self, name):
        """Creates subdir if doesn't exist and returns it"""
        for d in self.dirs:
            if d.name == name:
                return d
        return self.create_sub_directory(name)
        
    
            
    
    
cmd_re = re.compile(r"\$\s*cd\s*(.+)")
file_re = re.compile(r"^([0-9]+)\s*(.+)")
dir_re = re.compile(r"^dir\s*(.+)")

root = MyDir("/", None)
current = root
with open(PATH, "r") as file:
    lines = file.readlines()
    for line in lines:
        print(line)
        """Handle cd command"""
        match = cmd_re.search(line)
        if match:
            target_dir = match.group(1)
            if target_dir == current.name:
                print("Already at %s - skipping..." % target_dir)
            elif target_dir == '..':
                parent = current.get_parent()
                if parent:
                    current = parent
                else:
                    print("parent is None, cant go back!")
            else:
                current = current.get_child_directory(target_dir)
            print(current.name)
        """Handle file line"""
        match = file_re.search(line)
        if match:
            name = match.group(2)
            size = int(match.group(1))
            current.add_file(name, size)
        """Handle dir line"""
        match = dir_re.search(line)
        if match:
            name = match.group(1)
            print("creating subdir %s - current dir %s" % (name, current.name))
            current.create_sub_directory(name)


# part 2
total_disk_space=70000000
update_size=30000000
current_size=root.get_size()
free_space=total_disk_space-current_size
target_removal_amount=update_size-free_space

q = queue.Queue()
q.put(root)
at_most=100000
indent=" "
found=[]
while not q.empty():
    current = q.get()
    for d in current.dirs:
        q.put(d)
    if current.get_size() >= target_removal_amount:
        found.append(current)
s=None
for d in found:
    if s:
        if s.get_size() > d.get_size():
            s=d
    else:
        s=d
print("Target dir size: %i" % s.get_size())

            
            
