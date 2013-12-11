from math import sqrt,pi,e

def kernels(spec, parameter):
    if spec == "tricubic": return lambda d: _tc_kernel(d, parameter)
    if spec == "gaussian": return lambda d: _gs_kernel(d, parameter)
    raise Exception("Unknown kernel specified!")

def _tc_kernel(d, w):
    return max(0, (1 - (abs(d)/w)**3)**3)

def _gs_kernel(d, sd):
    a = 1.0/(sd * sqrt(2*pi))
    b = -0.5 * (abs(d) / sd)**2
    return a * e**(b)
