import copy
import math
import random

q=[]
visited=[]
def generate_children(curr_state):
    temp=copy.deepcopy(curr_state)
    potential_next=temp[1]
    for i in range(len(potential_next)):
        temp1=copy.deepcopy(potential_next)
        if temp1[i]==0:
            temp1[i]=1
        else:
            temp1[i]=0
        q.append([heuristic(temp1),temp1])


def search():
    global q
    global visited
    t=1000
    curr_state=q[0]
    del q[0]
    while(t>=0):
        if curr_state[0]==5:
            print("found")
            print(curr_state)
            exit()
        generate_children(curr_state)
        while len(q)>0:
            potential_next_state=q[0]
            del q[0]
            delta_E=potential_next_state[0]-curr_state[0]
            p=1/(1+math.exp(-delta_E/t))
            num=random.random()#random.uniform
            if num<=p:
                curr_state=potential_next_state
                q=[]

        t=t-10
    exit()


def heuristic(s):
    a=s[0]
    b=s[1]
    c=s[2]
    d=s[3]
    exp=[(not a or b),(c or d),((not c) or (not d)),((not b) or (not d)),((not a) or (not d))]
    return sum(exp)

def main():
    s=[0,0,0,0]
    q.append([heuristic(s),s])
    search()
    print(heuristic(s))
   
if __name__ == "__main__":
    main()