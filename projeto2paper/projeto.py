import random
import matplotlib.pyplot as plt
import os
import sys
def main():
    neighbors=[4,8,16,32]
    ps=[0,0,0,0]
    qs=[0,0,0,0]
    finished=0
    for i in range(len(neighbors)):
        try:
            newpid=os.fork()
        except OSError:
            exit("Could not create a child process")
        if newpid==0:
            args=[sys.executable,"/mnt/c/Users/andre/OneDrive/Tecnico/CRC/CRC_complex_revol_cooking/projeto2paper/neighbor_run.py",str(neighbors[i])]
            os.execv(sys.executable,args)
            exit()
    while finished!=len(neighbors):
        f=os.waitpid(0,0)
        if f[1]==0:
            finished+=1
        else:
            exit("Error in one child")
    for i in range(len(neighbors)):
        nome_ficheiro='neighbor_run_'+str(neighbors[i])
        f=open(nome_ficheiro,'r')
        t=f.readline().split()
        ps[i]=float(t[0])
        qs[i]=float(t[1])
        f.close()
    plt.scatter(neighbors,ps)
    plt.scatter(neighbors,qs)
    plt.show()

if __name__== "__main__":
  main()