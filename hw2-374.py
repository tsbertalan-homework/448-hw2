# -*- coding: utf-8 -*-
# <nbformat>2</nbformat>

# <codecell>

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

f = plt.figure(figsize=(8,6))
a = f.add_subplot(1, 1, 1)
f, a = giveFig(Pf(),       fig=f, ax=a, color='k-.')
f, a = giveFig(Pf(A=200),  fig=f, ax=a, color='k-')
f, a = giveFig(Pf(N0=200), fig=f, ax=a, color='k,')
f, a = giveFig(Pf(K=200),  fig=f, ax=a, color='k--')
f, a = giveFig(Pf(H=0),    fig=f, ax=a, color='r--')
f, a = giveFig(Pf(A=3e3),  fig=f, ax=a, color='b--')   # overlaps the H=0 plot
a.legend(loc='best')
f.suptitle('CBE 448, HW2, #3.7.4')
f.savefig('hw2-374-multi.pdf')
#plt.show()

# <codecell>

# (d)
fig = figure(figsize=(8,6))
ax = fig.add_subplot(1, 1, 1)

x = np.arange(-3, 2, 0.001)
shortx = np.arange(-1, 2, 0.01)
f1 = lambda x: x * (1 - x)
y1 = f1(x)

h = 1.1
a = 2.0
f2 = lambda x: h * x / (a + x)
y2 = f2(x)
ax.plot(x, y2, 'k--', label=r"$f_2(x)=hx/(a+x)$, with $a=%.1f$, $h=%.1f$" % (a, h))
h = 2.0
a = 1.1
f2 = lambda x: h * x / (a + x)
y2 = f2(shortx)
ax.plot(shortx, y2, 'k-.', label=r"$f_2(x)=hx/(a+x)$, with $a=%.1f$, $h=%.1f$" % (a, h))

ax.set_title(r"supercritical pitchfork around $x=0$ and $h=a$ for $\frac{dx}{dt}=f_1(x)-f_2(x:h,a)$")
ax.plot(x, y1, 'k-', label=r"$f_1(x)=x(1-x)$")

ax.set_ylim((-5, 1))
ax.set_xlim((-1.99, 1))
#ax.set_ylim((0, 1))
#ax.set_xlim((0, 1))
ax.legend(loc="best")

# <codecell>

# 3.7.4 (e)
fig = figure(figsize=(8,6))
ax = fig.add_subplot(1, 1, 1)

x = np.arange(-.8, 2, 0.001)
y1 = f1(x)

a = .1
delta = 0.1
h = (a + 1.) ** 2 / 4. + delta

f2 = lambda x: h * x / (a + x)
y2 = f2(x)
ax.plot(x, y2, 'k-.', label=r"$f_2(x)=hx/(a+x)$, with $a=%.1f$, $h=%.3f$" % (a, h))

h = (a + 1.) ** 2 / 4. - delta
f2 = lambda x: h * x / (a + x)
y2 = f2(x)
ax.plot(x, y2, 'k--', label=r"$f_2(x)=hx/(a+x)$, with $a=%.1f$, $h=%.3f$" % (a, h))

ax.set_title(r"saddle node at $h=a$ for $\frac{dx}{dt}=f_1(x)-f_2(x:h,a)$")
ax.plot(x, y1, 'k-', label=r"$f_1(x)=x(1-x)$")
ax.axvline(0, color='r')
ax.set_ylim((-.1, .5))
ax.set_xlim((-.1, 1.5))
ax.legend(loc="best")

# <codecell>

# 3.7.4 (f)

fig = figure()
ax = fig.add_subplot(1, 1, 1)
# x-axis is a; y-axis is h
fh = lambda a: (1. + a) ** 2 / 4.
ax.set_xlim(0, 2)
ax.set_ylim(0, fh(2))

delta = 0.025
a1 = np.arange(0, 1, delta)
a2 = np.arange(1, 2.1, delta)
atot = np.arange(0, 2, delta)

ax.plot(atot,atot, 'k')
ax.plot(a1, fh(a1), 'k')
ax.fill_between(a1, a1, fh(a1), facecolor='black', alpha=0.5)
#ax.fill_between(a2, np.zeros((len(a2),)), a2, facecolor='black', alpha=0.5)
ax.set_xlabel(r'$a$')
ax.set_ylabel(r'$h$')
ax.scatter([1], [1], color='k')
ax.set_title('parameter space: conditions for multiple steady-states                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      ')
a = 1.5
h = 1.4
D1 = 1 + 2*a + a**2 - 4*h
print D1
print (1 - a + D1 ** .5) / 2
print (1 - a - D1 ** .5) / 2

# <codecell>


