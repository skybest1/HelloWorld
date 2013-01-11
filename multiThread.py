import threading
import os,sys
from time import sleep,ctime
loops=[4,2]

def loop(nloop,nsec):
    print "loop",nloop,"start at:",ctime()
    sleep(nsec)
    print "loop",nloop,"end at",ctime()
#----------------------------------------------------------------------
#----------------------------------------------------------------------
def deamonloop():
    """"""
    while True:
        print "this is deamon loop!"
        sleep(3)
 
def main():
    """"""
    print "start at:",ctime()
    threads=[]
    nloops=range(len(loops))
    for i in nloops:
        t=threading.Thread(target=loop,args=(i,loops[i]))
        threads.append(t)
    t=threading.Thread(target=deamonloop)
    t.setDaemon(False)
    threads.append(t)
    for t in threads:
        t.start()
    print "all done at",ctime()
    pid=os.fork()
    if pid>0:
        sys.exit()
    #this is our child process
    print "another process!"
    
    

if __name__=="__main__":
    main()