from itertools import cycle
#for music in cycle(['waltz','tango','foxtrot']):
 #   print(music)
from threading import Thread,Semaphore
from time import sleep
import random
from timeit import Timer
rng=random.Random()
leaderEnter=Semaphore(0)
followerEnter=Semaphore(0)
speaking=Semaphore(0)
l_priority=[Semaphore(0) for i in range(5)]
f_priority=[Semaphore(0) for i in range(10)]
count=0
songchange=Semaphore(1)
afterleader=Semaphore(0)
beforefollower=Semaphore(0)
mutex=Semaphore(1)

def band():
    print('_______________________')
    print('change song')
    print('_______________________')
    songchange.release()
def cycle():
    for music in cycle(['waltz', 'tango', 'foxtrot']):
        start_music(music)
        end_music(music)

def leader(id):
    lp=id
    global count
    while True:
        if lp==0:
            sleep(rng.random())
            songchange.acquire()
            songchange.release()
            l_enter_floor(id)
            beforefollower.release()
            leaderEnter.release()
            followerEnter.acquire()
            print('leader',id,'is with')
            speaking.release()
            sleep(1)
            for j in range(5):
                l_priority[(id+j)%5].release()
            l_dance(id)
            l_leave_floor(id)
            afterleader.release()
            lp=5
        else:
            l_priority[id].acquire()
            lp=lp-1
            #print('leader',id,'priority',lp)
        

def follower(id):
   fp=id
   global count
   #for i in range(50):
   while True:
       if fp==0:
           sleep(rng.random())
           songchange.acquire()
           songchange.release()
           beforefollower.acquire()
           f_enter_floor(id)
           mutex.acquire()
           count=count+1
           mutex.release()
           if(count==10):
               songchange.acquire()
           followerEnter.release()
           leaderEnter.acquire()
           speaking.acquire()
           print('follower',id)  
           sleep(1)
           for j in range(10):
               f_priority[(id+j)%10].release() 
           f_dance(id)
           afterleader.acquire()
           f_leave_floor(id)
           if(count==10):
               band()
               count=0
           fp=10           
       else:
           f_priority[id].acquire()
           fp=fp-1
           #print('follower',id,'priority',fp)
           
           
           
def wait_in_the_line(id):
    print(id,'is waiting in the line')
def l_enter_floor(id):
    print('leader',id,'is entered the floor')
def f_enter_floor(id):
    print('follower',id,'is entered the floor')
def pair_up(lid,fid):
    print(lid,'and',fid,'are matched')
def l_dance(id):
    print('leader',id,'is dancing')
    sleep(rng.random())
def f_dance(id):
    print('follower',id,'is dancing')
    sleep(rng.random())
def l_leave_floor(id):
    print('leader',id,'is leaving the floor')
def f_leave_floor(id):
    print('follower',id,'is leaving the floor')
def back_to_the_line(id):
    print(id,'is back to the line')
    
    
    
#for i in range(5):
 #   ts=Thread(target=leader,args=[i])
  #  ts.start()
   # t=Thread(target=follower,args=[i])
#    t.start()
#tsk = []
for i in range(5):    
    thread1 = Thread(target = leader, args=[i])
    thread1.start()
  #  tsk.append(thread1)
for j in range(10):
    thread2 = Thread(target = follower,args=[j])
    thread2.start()
    #thread2.join()  
   # tsk.append(thread2)
   