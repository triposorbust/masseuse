from math import sqrt,pi,e

def kernels(spec, parameter):
    if spec == "tricubic": return lambda d: _tc_kernel(d, parameter)
    if spec == "gaussian": return lambda d: _gs_kernel(d, parameter)
    raise Exception("Unknown kernel specified!")

def _tc_kernel(d, w):
    d = float(d)
    w = float(w)
    return max(0.0, (1.0 - (abs(d)/w)**3)**3)

def _gs_kernel(d, sd):
    d = float(d)
    sd = float(sd)
    a = 1.0/(sd * sqrt(2*pi))
    b = -0.5 * (abs(d) / sd)**2
    return a * e**(b)
