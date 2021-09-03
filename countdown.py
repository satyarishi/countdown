import time
def countdown(n):
    while n > 0:
        print(n)
        time.sleep(.5)
        n -=1
        continue
    print("HERE WE GOOOOOOO!")
    while  n < 10:
        n +=1
        print(n)
        time.sleep(.5)
    print("launch successful!!!")
countdown(10)    