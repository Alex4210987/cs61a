import tensorflow as tf
import threading
import math
num_threads = 10
stop_event = threading.Event()

def find_abc(target=1141, index=0):
    n = 1
    n3 = []
    maxn = 1000
    # read maxn from input
    while maxn:
        n3.append(tf.pow(n, 3))
        n += 1
        maxn -= 1
    start = int(index * len(n3) / num_threads)-5 # incase of missing
    if start < 0:
        start = 0
    end = int((index + 1) * len(n3) / num_threads)
    for a in range(start, end):
        for b in range(0, n-1):
            
                c=
                if stop_event.is_set():
                    #print("Thread stopped")
                    return
                if tf.reduce_all(n3[a] + n3[b] == target * n3[c]):
                    print(a, b, c)
                    stop_event.set()
                    return
                else:
                    print(a, b, c ,"wrong!")
    return

def create_and_start_threads(num_threads):
    threads = []
    for i in range(num_threads):
        thread = threading.Thread(target=find_abc, args=(1141,i))
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()

if __name__ == '__main__':
    tf.device('/GPU:0')
    create_and_start_threads(num_threads)
    print("Done")
