import numpy as np
from numpy.random import random_sample
from scipy.stats import norm



def gen_random_dist(mean_bin_masses, bin_stdevs):
     """Generate a random discrete pmf based on a given pmf and given variance.

     Keyword arguments:
     mean_bin_masses -- an array representing a discrete pmf to use for the random draws
     bin_stdevs -- an array standard deviations to use for generating the random pmf

     """
     random_dist = np.zeros(mean_bin_masses.size, dtype='float')
     for i in range(mean_bin_masses.size):
          mass = norm.rvs(loc=mean_bin_masses[i], scale=bin_stdevs[i])
          if mass < 0:
               mass=0.0
          random_dist[i] = mass
     # Normalize so that it sums to 1:
     random_dist = random_dist / random_dist.sum() 
     return random_dist


## Currently 8 bins (arbitrarily)
binprobs = np.array([0.05,0.1,0.15,0.3,0.2,0.1,0.05,0.05])
## Constant variance. This could be an array of different variances.
binvars = np.ones(8) / 40




