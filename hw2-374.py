# -*- coding: utf-8 *-*
import numpy as np
from matplotlib import pyplot as plt

def Pf(
r = 0.5,
H = 10,
K = 80,
A = 40,
N0 = None
):
    if N0 == None: N0 = K / 2
    return {
        'r': r,
        'H': H,
        'K': K,
        'A': A,
        'N0': N0,
        }

dNdt = lambda N, r, K, H, A: r * N * (1 - N / K) - H * N / (A + N)

tmax = 40
dt = 0.1

P_l = []
P_l.append(Pf(N0=0))
P_l.append(Pf())
P_l.append(Pf(A=200))
P_l.append(Pf(N0=200))
t = np.arange(0, tmax, dt)

figs = []
axes = []

def giveFig(P, fig=None, ax=None, color=None):
    exec ', '.join(P) + ',  = P.values()'
    if fig == None:
        fig = plt.figure()
        ax = fig.add_subplot(1, 1, 1)
    N = []
    Nprev = N0

    for j in t:
        N.append(Nprev + dt * dNdt(Nprev, r, K, H, A))
        Nprev = N[-1]
    label = r"$N_0=%i$, $A=%i$, $H=%i$, $K=%i$, $r=%.2f$" % (N0, A, H, K, r)
    if color == None:
        ax.plot(t, N, label=label)
    else:
        ax.plot(t, N, color, label=label)
    return (fig, ax)

f, a = giveFig(Pf(), color='k-.')
f, a = giveFig(Pf(A=200),  fig=f, ax=a, color='k-')
f, a = giveFig(Pf(N0=200), fig=f, ax=a, color='k,')
f, a = giveFig(Pf(K=200),  fig=f, ax=a, color='k--')
f, a = giveFig(Pf(H=0),    fig=f, ax=a, color='r--')
f, a = giveFig(Pf(A=3e3),  fig=f, ax=a, color='b--')   # overlaps the H=0 plot
a.legend(loc='best')
f.suptitle('CBE 448, HW2, #3.7.4')
f.savefig('hw2-374-multi.pdf')
#plt.show()

#for i, P in enumerate(P_l):
    ## unpack the parameters into the local namespace:
    #exec ', '.join(P) + ',  = P.values()'
    #print P

    #figs.append(plt.figure())
    #axes.append(figs[i].add_subplot(1, 1, 1))
    #N = []
    #Nprev = N0
    #for j in t:
        #N.append(Nprev + dt * dNdt(Nprev, r, K, H, A))
        #Nprev = N[-1]
    #axes[i].plot(t, N)
    #axes[i].set_title(r"$N_0 = %i$" % N0 + '\n' + r"$K=%i$, $A=%i$, $r=%.2f$, $H=%i$" % (K, A, r, H))
    #figs[i].savefig("hw2-374-N0-%i-A%iH%iK%ir%.2f.png" % (N0, A, H, K, r))
##plt.show()
#



