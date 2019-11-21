import random
import matplotlib.pyplot as plt
import os
import sys

def main():
    robots=[0,10,20,30,40]
    ps=[0 for i in range(len(robots))]
    qs=[0 for i in range(len(robots))]
    finished=0
    for i in range(len(robots)):
        try:
            newpid=os.fork()
        except OSError:
            exit("Could not create a child process")
        if newpid==0:
            args=[sys.executable,"/mnt/c/Users/andre/OneDrive/Tecnico/CRC/CRC_complex_revol_cooking/projeto2paper/ring_run_robot.py",str(robots[i])]
            os.execv(sys.executable,args)
    while finished!=len(robots):
        f=os.waitpid(0,0)
        if f[1]==0:
            finished+=1
        else:
            exit("Error in one child")
    for i in range(len(robots)):
        nome_ficheiro='robot_run_'+str(robots[i])
        f=open(nome_ficheiro,'r')
        t=f.readline().split()
        ps[i]=float(t[0])
        qs[i]=float(t[1])
        f.close()
    plt.scatter(robots,ps)
    plt.scatter(robots,qs)
    plt.show()

if __name__== "__main__":
  main()