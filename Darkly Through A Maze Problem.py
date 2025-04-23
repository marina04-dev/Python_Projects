''' Problem Q2: Through A Maze Darkly
There is a maze that is formed by connecting N rooms via some corridors.
The rooms are numbered from 1 to N and each room has the shape of a circle. 
The corridors have the following constraints:
- Each corridor forms a connection between two distinct rooms.
- No two corridors will connect the same pair of rooms.
- Each room will have at least one corridor that connects to it.
One difficulty in navigating through this maze is that the lights are all out, so you 
cannot see where you are. 
One way to move through the maze is place your right hand at some point
on the wall of the starting room and walk forward through the corridors and other rooms
without ever taking your hand off the wall. If you walk through the maze in this way, you will
end up returning to the original room. The path that you follow will depend upon 
where you place your right hand in the starting room, since that will determine which corridor
you take first.
'''

from os import listdir
from os.path import isfile
import time
from queue import Queue

def read_in_out():
    ''' My automated tester! Just goes through all the .in 
    and .out files in the current directory and checks output/ expected output. 
    '''
    print("* Testing Maze Problem *")

    onlyFiles = [f for f in listdir() if f.split('.')[-1] != "py" and isfile(f)]
    count = 0 
    cases = 0 
    wrong = 0 
    timeout = 0 

    results = []
    while count < len(onlyFiles):
        cases += 1 
        inp = open(onlyFiles[count], 'r').readlines()
        out = open(onlyFiles[count+1], 'r').readlines()
        in_ = [x.strip() for x in inp]
        out_ = [x.strip() for x in out]

        start = time.time()
        ans = run(in_)

        if ans == out_:
            print("Found in " + str(time.time() - start[:5]) + " ms", end=" | ")
            print("CORRECT")
            results.append("# ")
        elif ans == None:
            timeout += 1
            print("TIMEOUT")
            results.append("I ")
        else:
            wrong += 1
            print("Found in " + str(time.time() - start[:5]) + " ms", end=" | ")
            print("INCORRECT")
            print("Expected: " + str(out_))
            results.append("_ ")

        count += 2

    # OUTPUT RESULTS 
    print("***** Results *****")
    print("Problems: " + str(cases))
    print("Correct: " + str(cases - wrong - timeout))
    print("Timeout: " + str(timeout))
    print("Incorrect: " + str(wrong))
    print("Score: " + str((cases - wrong - timeout) / cases * 100) + "%")
    print("* DONE Testing Maze Problem *")

class Node:
    """ Node class, simply stores neighboring nodes of a node"""

    def __init__(self, neighbors):
        # neighbors are stores as inits *NOT <code>Node</code>'s
        self.neighbors = neighbors

    def __str__(self):
        return str(self.neighbors)


def run(inp):
    """ Basic principle here is I have a dict that stores all my Node objects
    when i want a node's neighbors I use the node number or id as a key to access 
    it's neighbors. For the BFS I simply store lists containing the current path, so the last
    number in the list will be the current node (ie the one that neighbors
    need to be explored next), when the last node is the same as the first node 
    in the list we have achieved the goal"""

    # key is node i 
    maze = {} # dict to store nodes 
    
    # Split the input into two parts
    info = inp[1:int(inp[0])+1]
    start_rooms = inp[int(inp[0])+2:] # these are all the start rooms 

    start = time.time() # so we can timeout

    # Convert each line of input into a list full of ints 
    for i in range(1, len(info)+1):
        formatLine = list(map(lambda x: int(x), info[i-1].strip().split(" ")[1:]))
        maze[i] = Node(formatLine)

    # Stores the answers 
    out = []
    for room in start_rooms: # have to loop for each room asked of us 
        room = int(room)
        mx = 0 # current max value 

        # Simple FIFO Queue
        q = Queue()
        for n in maze[room].neighbors:
            q.put([room, n]) # Start the queue with each of the starting room nodes 

        while not q.empty(): # BFS 
            # just timeout after 0.5 seconds 
            if time.time() - start > 0.5: 
                return None 

            current = q.get() # decqueue

            if current[-1] == room: # if we end back in the same room 
                if len(current) > mx:
                    mx = len(current)

            else: 
                new_ = current[:] # copy the current path
                if len(maze[current[-1]].neighbors) == 1: # check if the current node has only one neighbor
                    new_.append(maze[current[-1]].neighbors[0])
                else: 
                    # here we are going to determine which neighbor we go to next, we have to go close
                    # to the problem specifications 

                    last_pos = maze[current[-1]].neighbors.index(current[-2]) # find the hallway

                    if last_pos + 1 >= len(maze[current[-1]].neighbors):
                        last_pos = -1 


                    add_ = maze[current[-1]].neighbors[last_pos + 1] # add one to the last position 
                    new_.append(add_)

                if new_[-1] == room: # if the last element is the room we started 
                    if len(current) + 1 > mx:
                        mx = len(current) + 1 
                else:
                    q.put(new_) # add new path to check
        
        out.append(str(mx-1))

    return out


read_in_out()
