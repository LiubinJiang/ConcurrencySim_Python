#golfer
from threading import Thread, Semaphore
from time import sleep
import random
rng=random.Random()
stash=25
balls_on_field=0
checkspot=Semaphore(1)
fieldball=Semaphore(1)
callcart=Semaphore(1)
freeze=Semaphore(1)

def cart():
    global stash
    global balls_on_field
    freeze.acquire()
    stash=stash+balls_on_field
    print('-------------------------------------')
    print('all balls on field is picked up',stash)
    balls_on_field=0
    freeze.release()


def golfer(id):
    global stash
    global balls_on_field
    #while True:
    for a in range(5): 
        checkspot.acquire()
        if(stash>=5):
            print("golfer",id,"finds stash is sufficient")
            stash=stash-5
            basket=5
            print('golfer',id,'basket refilled')
            checkspot.release()
            for i in range (5):
                freeze.acquire()
                freeze.release()
                fieldball.acquire()
                basket=basket-1
                balls_on_field =balls_on_field+1
                #fieldball.release()
                print('golfer',id,'is hitting the ball',i)
                print('balls on the field now is',balls_on_field)
                fieldball.release()
                slp=rng.random()
                print(slp)
                sleep(slp)
            print('golfer',id,'finish a basket')
        else:
            print('golfer',id,'finds stash is not sufficient')
            tCart=Thread(target=cart)
            tCart.start()
            checkspot.release()
            
        #checkspot.release()

for i in range(5):
    t=Thread(target=golfer,args=[i])
    t.start()