import time
from multiprocessing import Process
import os
from multiprocessing import current_process


def info(title):
    print(title)
    print('module name:', __name__)
    print('parent process:', os.getppid())
    print('process id:', os.getpid())
    print('process id:', current_process())
    time.sleep(4)

def f(name):
    print('process id:', os.getpid())
    print('hello', name)
    time.sleep(10)

if __name__ == '__main__':

    ps = []
    for i in range(2):
        p = Process(target=f, args=(f'bob{i}',))
        p.start()
        ps.append(p)

    for p in ps:
        # p.start()
        p.join()