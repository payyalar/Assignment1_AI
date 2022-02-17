import sys


def go_up(st):
    """The blank tile is moved to the top of the board. Returns a list of new states."""
    ns = st[:]
    i = ns.index(0)
    if i not in [0, 3, 6]:
        # change values.
        temp = ns[i - 1]
        ns[i - 1] = ns[i]
        ns[i] = temp
        return ns
    else:
        return None


def go_down(st):
    """Places the blank tile at the bottom of the board. Returns a list of new states."""
    ns = st[:]
    i = ns.index(0)
    if i not in [2, 5, 8]:
        # change values
        temp = ns[i + 1]
        ns[i + 1] = ns[i]
        ns[i] = temp
        return ns
    else:
        return None


def go_left(st):
    """Places the blank at the left of the board. Returns a list of new states."""
    ns = st[:]
    i = ns.index(0)
    if i not in [0, 1, 2]:
        # change values.
        temp = ns[i - 3]
        ns[i - 3] = ns[i]
        ns[i] = temp
        return ns
    else:
        return None


def go_right(st):
    """Places the blank tile at the right of the board. Returns a list of new states."""
    ns = st[:]
    i = ns.index(0)
    if i not in [6, 7, 8]:
        # change values.
        temp = ns[i + 3]
        ns[i + 3] = ns[i]
        ns[i] = temp
        return ns
    else:
        return None


def node_create(st, pr, opr, dep, cost):
    return Node(st, pr, opr, dep, cost)


def node_expand(node):
    """Returns a list of expanded nodes"""
    exp_nod = []
    exp_nod.append(node_create(go_up(node.st), node, "u", node.dep + 1, 0))
    exp_nod.append(node_create(go_down(node.st), node, "d", node.dep + 1, 0))
    exp_nod.append(node_create(go_left(node.st), node, "l", node.dep + 1, 0))
    exp_nod.append(node_create(go_right(node.st), node, "r", node.dep + 1, 0))
    # Remove the nodes from the list that aren't possible. 
    exp_nod = [node for node in exp_nod if node.st != None]  
    return exp_nod


def bfs(start, goal):
    """Performs a breadth first search from the start state to the goal"""
    goal=goal
    init_node=node_create(start,None,None,0,0)
    fr=[]
    fr.append(init_node)
    curr=fr.pop(0)
    path=[]
    display=[]
    while(curr.st!=goal):
        fr.extend(node_expand(curr))
        curr=fr.pop(0)
    while(curr.pr!=None):
        path.insert(0,curr.opr)
        display.append(curr.st)
        curr=curr.pr
        
    for i in range(len(display)-1,-1,-1):
        show_state(display[i])
    return path
    pass


def dfs(start, goal, dep=10):
    init_node=node_create(start,None,None,0,0)
    fr_stack=[]
    fr_stack.append(init_node)
    curr=fr_stack.pop(0)
    path=[]
    display=[]
    while(curr.st!=goal):
        temp=node_expand(curr)
        for item in temp:
            fr_stack.append(item)
        curr=fr_stack.pop(0)
        if(curr.dep>10):
            return None
    while(curr.pr!=None):
        path.insert(0,curr.opr)
        display.append(curr.st)
        curr=curr.pr
    for i in range(len(display)-1,-1,-1):
            show_state(display[i])
    return path



def uniform_cost(start,goal):
    init_node=node_create(start,None,None,0,0)
    fr=[]
    path=[]
    display=[]
    fr.append(init_node)
    curr=fr.pop(0)
    while(curr.st!=goal):
        temp=node_expand(curr)
        for item in temp:
            item.dep+=curr.dep
            fr.append(item)
        fr.sort(key =lambda x: x.dep)
        curr=fr.pop(0)
        
    while(curr.pr!=None):
        path.insert(0,curr.opr)
        display.append(curr.st)
        curr=curr.pr
    for i in range(len(display)-1,-1,-1):
        show_state(display[i])
        
    return path


def show_state(st):
    print( "-------------")
    print( "| %i | %i | %i |" % (st[0], st[3], st[6]))
    print( "-------------")
    print( "| %i | %i | %i |" % (st[1], st[4], st[7]))
    print( "-------------")
    print( "| %i | %i | %i |" % (st[2], st[5], st[8]))
    print( "-------------")


class Node:
    def __init__(self, st, pr, opr, dep, cost):
        self.st = st
        self.pr = pr
        self.opr = opr
        self.dep = dep
        self.cost = cost

        self.heuristic=None
print("puzzle solving using BFS algorithm\n")
#DEFINE START AND GOAL VALUES 
start_st = [1,8,7,3,0,2,4,5,6]
gl_st = [1, 8, 7, 2, 0, 6, 3, 4, 5]


result = bfs(start_st, gl_st)


if result == None:
    print( "Solution not possible")
elif result == [None]:
    print( "Start node is the final goal")
else:
    print(result)
    print(len(result), " moves")

    
print("puzzle solving using DFS algorithm\n")
#DEFINE START AND GOAL VALUES 
start_st = [1,8,7,3,0,2,4,5,6]
gl_st = [1, 8, 7, 2, 0, 6, 3, 4, 5]


result = dfs(start_st, gl_st)


if result == None:
    print( "Solution not possible")
elif result == [None]:
    print( "Start node is the final goal")
else:
    print(result)
    print(len(result), " moves")

    
print("puzzle solving using uniform_cost algorithm\n")
#DEFINE START AND GOAL VALUES IN COLUMN WISE
start_st = [1,8,7,3,0,2,4,5,6]
gl_st = [1, 8, 7, 2, 0, 6, 3, 4, 5]


result = uniform_cost(start_st, gl_st)


if result == None:
    print( "Solution not possible")
elif result == [None]:
    print( "Start node is the final goal")
else:
    print(result)
    print(len(result), " moves")



