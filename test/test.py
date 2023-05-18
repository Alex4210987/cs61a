#计算x^3+y^3=1141的正有理数解
#a^3+b^3=1141*c^3, a,b,c为正有理数
#用数组存储n^3的值，然后遍历数组，找到合适的a\b\c
from math import pow, log10
from fractions import Fraction
import threading
num_threads=4
stop_event = threading.Event()
#use list to store a,b,c
ans=[[],[],[]]
n = 1
n3 = []
maxn = 100000000
    #read maxn from input
piece=maxn/10000
while maxn:
    n3.append(pow(n, 3))
    n += 1
    maxn -= 1
def find_abc(target=1141,index=0):
    start = int(index * len(n3) / num_threads)-5#incase of missing
    if start < 0:
        start = 0
    end = int((index + 1) * len(n3) / num_threads)
    
    for a in range(start, end):
        #print("a is",a)
        if a % piece == 0:
            print("\n",index, "thread: ", a, "/", 10000*piece, "finished","\n")
        for b in range(0, n-1):
            #for c in range(0, n-1):
            #if stop_event.is_set():
                #print("Thread stopped")
                #return
            c=pow((n3[a]+n3[b])/target,1/3)    
            if abs(c-int(c))<=0.000001:
            #if c.is_integer():
                #print("a is",a,"b is",b,"c is", c,"correct!")
                #print("\n\n")
                #add abc to list ans
                ans[0].append(a)
                ans[1].append(b)
                ans[2].append(c)
                #stop_event.set()
                return
            #else:
                #print("a is",a,"b is",b,"c is", c,"wrong!")
                #print("\n")
    #print(index, "thread ended")
    return

def fra(a,b,c):
        fra1=Fraction(a,c)
        fra2=Fraction(b,c)
        sum=fra1**3+fra2**3
        return sum

def print_ans():
    #print("a is",ans[0],"b is",ans[1],"c is", ans[2],"correct!")
    for i in range(len(ans[0])):
        print("a is",ans[0][i],"b is",ans[1][i],"c is", ans[2][i],"correct!")
        a=round(ans[0][i])
        b=round(ans[1][i])
        c=round(ans[2][i])
        print("fra is",fra(a,b,c))
    return

def create_and_start_threads(num_threads):
    threads = []
    for i in range(num_threads):
        thread = threading.Thread(target=find_abc, args=(1141,i))
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()

# 创建并启动线程
create_and_start_threads(num_threads)

print_ans()

print("Done")
