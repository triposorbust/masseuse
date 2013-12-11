from masseuse.kernels import kernels
from math import e,pi,sqrt
import unittest
import random

class TricubicKernelSpec(unittest.TestCase):
    def test_kernel(self):
        w = 3.0
        tc = kernels("tricubic", w)
        ds = [-3.0, -2.0, -1.0, 0.0, 1.0, 2.0, 3.0]
        computed = map(tc, ds)
        expected = [(1 - (abs(d)/w)**3)**3 for d in ds]
        for expect,compute in zip(expected,computed):
            self.assertAlmostEqual(expect, compute)

class GaussianKernelSpec(unittest.TestCase):
    def test_kernel(self):
        sd = 1.0
        gs = kernels("gaussian", sd)
        ds = [-3.0, -2.0, -1.0, 0.0, 1.0, 2.0, 3.0]
        computed = map(gs, ds)
        expected = [1.0/(sd*sqrt(2*pi)) * e**(-0.5 * (d/sd)**2)
                    for d in ds]
        for expect,compute in zip(expected,computed):
            self.assertAlmostEqual(expect, compute)
