from time import sleep
from threading import Thread, Semaphore
import random
from timeit import Timer

footman=Semaphore(4)
forks=[Semaphore(1) for i in range(5)]
rng=random.Random()

def p_footman(id):
    for i in range(10):
        thinking(id)             
        getForks(id)
        eating(id)
        putForks(id)
        sleeping(id)
        
def p_lefthand(id):
    for i in range(10):
        thinking(id)             
        l_getForks(id)
        eating(id)
        putForks(id)
        sleeping(id)
def p_tanenbaum(id):
    for i in range(10):
        thinking(id)             
        get_fork(id)
        eating(id)
        put_fork(id)
        sleeping(id)        
        
def thinking(id):
    #print(id, 'is thinking...')
    slp=rng.random()/100
    #print(slp)
    sleep(slp)
    
def eating(id):
    #print(id, 'is eating')
    slp=rng.random()/100
    #print(slp)
    sleep(slp)
def sleeping(id):
    #print(id, 'is sleeping')
    slp=rng.random()/100
    sleep(slp)

def getForks(id):
    footman.acquire()
    forks[(id+1)%5].acquire()
    #print(id,'grabbed left fork',(id+1)%5)
    forks[id].acquire()
    #print(id,'grabbed right fork',id)
def putForks(id):
    forks[(id+1)%5].release()
    #print(id,'release left fork',(id+1)%5)
    forks[id].release()
    #print(id,'release right fork',id)
    footman.release()
def l_getForks(id):
    if(id==0):
        forks[id].acquire()
        #print(id,'grabbed right fork',id)
        forks[(id+1)%5].acquire()
        #print(id,'grabbed left fork',(id+1)%5)
    else:
        forks[(id+1)%5].acquire()
        #print(id,'grabbed left fork',(id+1)%5)
        forks[id].acquire()
        #print(id,'grabbed right fork',id)
def right(i):
    return i
    
def left(i):
    return (i+1)%5
    
def get_fork(i):
    mutex.acquire()
    state[i] = 'hungry'
    test(i)
    mutex.release()
    sem[i].acquire()
def put_fork(i):
    mutex.acquire()
    state[i] = 'thinking'
    test(right(i))
    test(left(i))
    mutex.release()
def test(i):
    if state[i] == 'hungry' \
       and state[left(i)] != 'eating' \
       and state[right(i)] != 'eating':
        state[i] = 'eating'
        print(i,'grab all the forks')
        sem[i].release()
    
#for i in range(5):
 #   t=Thread(target=philosopher,args=[i])
  #  t.start()
def totime_footman():
    ts=[Thread(target=p_footman,args=[i]) for i in range(5)]
    for t in ts: t.start()
    for t in ts: t.join()
def totime_lefthand():
    ts=[Thread(target=p_lefthand,args=[i]) for i in range(5)]
    for t in ts: t.start()
    for t in ts: t.join()
def totime_tanenbaum():
    ts=[Thread(target=p_tanenbaum,args=[i]) for i in range(5)]
    for t in ts: t.start()
    for t in ts: t.join()

if __name__=='__main__':
    t1=Timer('totime_footman()','from __main__ import totime_footman') 
    print t1.timeit(100)
    t2=Timer('totime_lefthand()','from __main__ import totime_lefthand') 
    print t2.timeit(100)
    t3=Timer('totime_tanenbaum()','from __main__ import totime_tanenbaum') 
    print('tanenbaum time is',t2.timeit(100))