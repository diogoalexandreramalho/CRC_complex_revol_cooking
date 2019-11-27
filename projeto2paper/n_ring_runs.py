import random
import matplotlib.pyplot as plt
import os
import sys

def main():
    neighbors=[2,4,6,8,10,16,24,32]
    robots=[0,10,20,30,40]
    runRobots=False
    choice=input("n for neighbors run, r for robots run: ")
    while choice not in ['r','n']:
        choice=input("n for neighbors run, r for robots run")
    if choice=='n':
        choice=neighbors
    else:
        choice=robots
        runRobots=True
    
    ps=[0 for i in range(len(choice))]
    qs=[0 for i in range(len(choice))]
    finished=0
    for i in range(len(choice)):
        try:
            newpid=os.fork()
        except OSError:
            exit("Could not create a child process")
        if newpid==0:
            args=[sys.executable,"/mnt/c/Users/andre/OneDrive/Tecnico/CRC/CRC_complex_revol_cooking/projeto2paper/ring_run.py"]
            if runRobots:
                args+=["-r",str(choice[i])]
            else:
                args+=["-n",str(choice[i])]
            os.execv(sys.executable,args)
    while finished!=len(choice):
        f=os.waitpid(0,0)
        if f[1]==0:
            finished+=1
        else:
            exit("Error in one child")
    for i in range(len(choice)):
        nome_ficheiro='ring_run_'
        if runRobots:
            nome_ficheiro+=str(choice[i])+'_robot'+"4_neighbors"
        else:
            nome_ficheiro+='0_robots'+str(choice[i])+"_neighbors"
        f=open(nome_ficheiro,'r')
        t=f.readline().split()
        ps[i]=float(t[0])
        qs[i]=float(t[1])
        f.close()
    plt.scatter(choice,ps)
    plt.scatter(choice,qs)
    plt.show()

if __name__== "__main__":
  main()