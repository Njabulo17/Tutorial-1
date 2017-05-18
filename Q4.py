# -*- coding: utf-8 -*-
"""
Created on Thu May 18 07:26:12 2017

@author: Njabulo Mbanjwa, CP tut3 Question4
"""

import numpy as np

def simulate_lorentz(x,a=2.5,b=1,c=5):#a = sig, b=amp, c=cent

    dat=a/(b+(x-c)**2)
    dat+=np.random.randn(x.size)
    return dat

#get a trial step. Take gaussian random numbers and scale by an input vector
def get_trial_offset(sigs):
    return sigs*np.random.randn(sigs.size)


class Lorentz:

    def __init__(self,x,a=2.5,b=1,c=5,offset=0):

        self.x=x
        self.y=simulate_lorentz(x,a,b,c)+offset
        self.err=np.ones(x.size)
        self.a=a
        self.b=b
        self.c=c
        self.offset=offset

    def get_chisq(self,vec):
        a=vec[0]
        b=vec[1]
        c=vec[2]
        off=vec[3]
        pred=off+a/(b+(self.x-c)**2)
        chisq=np.sum(  (self.y-pred)**2/self.err**2)
        return chisq

def run_mcmc(data,start_pos,nstep,scale=None):
    nparam=start_pos.size
    params=np.zeros([nstep,nparam+1])
    params[0,0:-1]=start_pos
    cur_chisq=data.get_chisq(start_pos)
    cur_pos=start_pos.copy()

    if scale==None:

        scale=np.ones(nparam)

    for i in range(1,nstep):
        new_pos=cur_pos+get_trial_offset(scale)
        new_chisq=data.get_chisq(new_pos)

        if new_chisq<cur_chisq:

            accept=True

        else:

            delt=new_chisq-cur_chisq
            prob=np.exp(-0.5*delt)

            if np.random.rand()<prob:

                accept=True

            else:

                accept=False

        if accept: 

            cur_pos=new_pos
            cur_chisq=new_chisq

        params[i,0:-1]=cur_pos
        params[i,-1]=cur_chisq
    return params


if __name__=='__main__':

 #get a realization of a gaussian, with noise added
    x=np.arange(-5,5,0.01)
    dat=Lorentz(x,b=2.5)

    #pick a random starting position, and guess some errors
    guess=np.array([0.3,1.2,0.3,-0.2])
    scale=np.array([0.1,0.1,0.1,0.1])
    nstep=100000
    chain=run_mcmc(dat,guess,nstep,scale)
    nn=np.round(0.2*nstep)
    chain=chain[nn:,:]
    #pull true values out, compare to what we got
    param_true=np.array([dat.a,dat.b,dat.c,dat.offset])

    for i in range(0,param_true.size):

        val=np.mean(chain[:,i])

        scat=np.std(chain[:,i])

print ([param_true[i],val,scat])
