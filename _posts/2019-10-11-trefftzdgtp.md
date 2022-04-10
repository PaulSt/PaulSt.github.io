---
layout: post
title:  "Space-time Trefftz-DG on tent pitched meshes"
categories: NGSolve
---

Two examples of the current Trefftz-DG method using tent pitching. 

A wave hitting a corner, producing a singularity: 

<img src="/assets/sing.gif" width="50%" align="middle"/>

A wave in inhomogeneous material:

<img src="/assets/material.gif" width="50%" align="middle"/>

I am still a little torn about the current way of steering things from python, because it is quite rigid, but at least it is possible to start tent pitching using Trefftz-DG for the accoustic wave equation.

We start by importing and setting some parameters:
```python
from trefftzngs import *
import netgen.gui
from ngsolve import *
D = initmesh.dim
t = CoordCF(D)
order = 4
t_start = 0
t_step = 0.01
initmesh = # your space mesh 
```
We create the WaveTents object, which will handle everything, and set initial and boundary conditions 
```python
sq = sqrt(0.5);
# Simple example use solution for initial cond. + dirichlet/neumann bndc. 
# supply fct + derivatives
bdd = CoefficientFunction((
    sin( t+sq*(x+y) ), # used to reconstruct the 2nd order solution
    sq*cos(t+sq*(x+y)), # init. cond. / Neumann bc
    sq*cos(t+sq*(x+y)),
    cos(t+sq*(x+y)) # init. cond. / Dirichlet bc
    ))
TT=WaveTents(order,initmesh,c,bdd) # set boundary condition
TT.SetWavefront(bdd,t_start) # set initial cond.
```
Now we set up the GridFunction to draw, provided by GetWave(), and then we are ready to start the iteration.
```python
gfu = TT.GetWave()
Draw(gfu,initmesh,'sol',autoscale=False,min=-0.025,max=0.05)

with TaskManager():
    for t in range(0,80):
        TT.EvolveTents(t_step)
        gfu.vec.data = TT.GetWave().vec.data
        Redraw() 

        t_start += t_step
        print("time: " + str(t_start))
```
It is also possible to use neumann bdc
```python
for i in range(0,len(initmesh.GetBoundaries())):
   initmesh.ngmesh.SetBCName(i,"neumann")
```
