import time
n = 10
while n > 0:
    print(n)
    time.sleep(.5)
    n -=1
    continue
print("Takeoff!")
while  n < 10:
    n +=1
    print(n)
    time.sleep(.5)
print("launch successful!!!")        
