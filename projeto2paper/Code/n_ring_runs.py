import random
import matplotlib.pyplot as plt
import os
import sys

def main():
    neighbors=[2,4,6,8,16,24,32]
    robots=[0,10,20,30,40]
    epsilon=[0.001,0.002,0.01,0.02,0.1,0.2,0.4]
    population=[100,200,500,1000,2000,4000,8000]
    choice=input("press 'n' for neighbors run, 'r' for robots run, 'p' for population run and 'e' for epsilon run: ")
    while choice not in ['r','n','e','p']:
        choice=input("press 'n' for neighbors run, 'r' for robots run, 'p' for population run and 'e' for epsilon run: ")
    if choice=='n':
        choice=neighbors
    elif choice=='r':
        choice=robots
    elif choice=='p':
        choice=population
    else:
        choice=epsilon
    ps=[0 for i in range(len(choice))]
    qs=[0 for i in range(len(choice))]
    perroru=[0 for i in range(len(choice))]
    perrord=[0 for i in range(len(choice))]
    qerroru=[0 for i in range(len(choice))]
    qerrord=[0 for i in range(len(choice))]
    finished=0
    for i in range(len(choice)):
        try:
            newpid=os.fork()
        except OSError:
            exit("Could not create a child process")
        if newpid==0:
            args=[sys.executable,"ring_run.py"]
            if choice==robots:
                args+=["-r",str(choice[i])]
            elif choice==neighbors:
                args+=["-n",str(choice[i])]
            elif choice==population:
                args+=["-p",str(choice[i])]
            else:
                args+=["-e",str(choice[i])]
            os.execv(sys.executable,args)
    while finished!=len(choice):
        f=os.waitpid(0,0)
        if f[1]==0:
            finished+=1
        else:
            exit("Error in one child")
    for i in range(len(choice)):
        nome_ficheiro='ring_run_'
        if choice==robots:
            nome_ficheiro+='100_population_'+str(choice[i])+'_robots_4_neighbors_0.001_epsilon'
        elif choice==neighbors:
            nome_ficheiro+='100_population_0_robots_'+str(choice[i])+'_neighbors_0.001_epsilon'
        elif choice==population:
            nome_ficheiro+=str(choice[i])+'_population_0_robots_4_neighbors_0.001_epsilon'
        else:
            nome_ficheiro+='100_population_0_robots_4_neighbors_'+str(choice[i])+'_epsilon'
        f=open(nome_ficheiro,'r')
        t=f.readline().split()
        ps[i]=float(t[0])
        qs[i]=float(t[1])
        perrord[i]=ps[i]-float(t[2])
        perroru[i]=float(t[3])-ps[i]
        qerrord[i]=qs[i]-float(t[4])
        qerroru[i]=float(t[5])-qs[i]
        f.close()
    fig,axs=plt.subplots(nrows=2)
    ax=axs[0]
    ax.errorbar(choice,ps,yerr=[perrord,perroru],fmt='o')
    ax.set_title('Ps')
    ax=axs[1]
    ax.errorbar(choice,qs,yerr=[qerrord,qerroru],fmt='o')
    ax.set_title('Qs')
    plt.show()

if __name__== "__main__":
  main()